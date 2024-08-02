from doku_python_library.src.model.va.create_va_request import CreateVARequest
from doku_python_library.src.model.va.create_va_response import CreateVAResponse
from doku_python_library.src.services.token_service import TokenService
import requests, uuid, json, xmltodict
from doku_python_library.src.commons.config import Config
from doku_python_library.src.model.general.request_header import RequestHeader
from doku_python_library.src.model.va.update_va_request import UpdateVaRequest
from doku_python_library.src.model.va.update_va_response import UpdateVAResponse
from doku_python_library.src.model.va.check_status_va_request import CheckStatusRequest
from doku_python_library.src.model.va.check_status_va_response import CheckStatusVAResponse
import xml.etree.ElementTree as ET
from doku_python_library.src.model.va.virtual_account_data import VirtualAccountData
from doku_python_library.src.commons.va_channel_enum import VaChannelEnum
from doku_python_library.src.model.va.delete_va_request import DeleteVARequest
from doku_python_library.src.model.va.delete_va_response import DeleteVAResponse

class VaService:

    @staticmethod
    def generate_external_id() -> str:
        return uuid.uuid4().hex + TokenService.get_timestamp()

    @staticmethod
    def generate_request_header(channel_id: str, client_id: str, 
                                 token_b2b: str, timestamp: str, external_id: str, signature: str) -> RequestHeader:
        header: RequestHeader = RequestHeader(
            x_timestamp= timestamp,
            x_signature= signature,
            x_partner_id= client_id,
            authorization= token_b2b,
            x_external_id= external_id,
            channel_id= channel_id
        )
        return header

    @staticmethod
    def creat_va(create_va_request: CreateVARequest, request_header: RequestHeader, is_production: bool) -> CreateVAResponse:
        try:
            url: str = Config.get_base_url(is_production=is_production) + Config.CREATE_VA

            headers: RequestHeader = request_header.to_json()

            response = requests.post(url=url, json=create_va_request.create_request_body(), headers=headers)
            response_json = response.json()
            va_response: CreateVAResponse = CreateVAResponse(**response_json) 
            return va_response
        except Exception as e:
            print("Failed Parse Response "+str(e))
    
    @staticmethod
    def do_update_va(request_header: RequestHeader, update_va_request: UpdateVaRequest, is_production: bool) -> UpdateVAResponse:
        try:
            url: str = Config.get_base_url(is_production=is_production) + Config.UPDATE_VA

            headers: RequestHeader = request_header.to_json()

            response = requests.put(url=url, json=update_va_request.create_request_body(), headers=headers)
            response_json = response.json()
            va_response: UpdateVAResponse = UpdateVAResponse(**response_json) 
            return va_response
        except Exception as e:
            print("Failed Parse Response "+str(e))
    
    @staticmethod
    def do_check_status_va(request_header: RequestHeader, check_status_request: CheckStatusRequest, is_production: bool) -> CheckStatusVAResponse:
        try:
            url: str = Config.get_base_url(is_production=is_production) + Config.CHECK_STATUS_VA

            headers: RequestHeader = request_header.to_json()

            response = requests.post(url=url, json=check_status_request.create_request_body(), headers=headers)
            response_json = response.json()
            va_response: CheckStatusVAResponse = CheckStatusVAResponse(**response_json) 
            return va_response
        except Exception as e:
            print("Failed Parse Response "+str(e))

    @staticmethod
    def do_delete_payment_code(request_header: RequestHeader, delete_va_request: DeleteVARequest, is_production: bool) -> DeleteVAResponse:
        try:
            url: str = Config.get_base_url(is_production=is_production) + Config.DELETE_VA

            headers: RequestHeader = request_header.to_json()

            response = requests.delete(url=url, json=delete_va_request.create_request_body(), headers=headers)
            response_json = response.json()
            delete_va_response: DeleteVAResponse = DeleteVAResponse(**response_json) 
            return delete_va_response
        except Exception as e:
            print("Failed Parse Response "+str(e))

    @staticmethod
    def snap_v1_converter(snap_format: dict,) -> dict:
       v1_channel_id = ""
       channel = snap_format["additionalInfo"]["channel"]
       if channel == VaChannelEnum.VIRTUAL_ACCOUNT_BCA.value:
           v1_channel_id = "29"
       elif channel == VaChannelEnum.VIRTUAL_ACCOUNT_BANK_MANDIRI.value:
           v1_channel_id = "08"
       elif channel == VaChannelEnum.VIRTUAL_ACCOUNT_BRI.value:
           v1_channel_id = "34"
       elif channel == VaChannelEnum.VIRTUAL_ACCOUNT_BNI.value:
           v1_channel_id = "38"
       elif channel == VaChannelEnum.VIRTUAL_ACCOUNT_BANK_DANAMON.value:
           v1_channel_id = "33"
       elif channel == VaChannelEnum.VIRTUAL_ACCOUNT_BANK_PERMATA.value:
           v1_channel_id = "05"
       elif channel == VaChannelEnum.VIRTUAL_ACCOUNT_MAYBANK.value:
           v1_channel_id = "44"
       elif channel == VaChannelEnum.VIRTUAL_ACCOUNT_BNC.value:
           v1_channel_id = "-"
       elif channel == VaChannelEnum.VIRTUAL_ACCOUNT_BTN.value:
           v1_channel_id = "43"
       elif channel == VaChannelEnum.VIRTUAL_ACCOUNT_BSI.value:
           v1_channel_id = "-"
       elif channel == VaChannelEnum.VIRTUAL_ACCOUNT_BANK_CIMB.value:
           v1_channel_id = "32"
       elif channel == VaChannelEnum.VIRTUAL_ACCOUNT_SINARMAS.value:
           v1_channel_id = "21"
       elif channel == VaChannelEnum.VIRTUAL_ACCOUNT_DOKU.value:
           v1_channel_id = "47"
       elif channel == VaChannelEnum.VIRTUAL_ACCOUNT_BSS.value:
           v1_channel_id = "-"
       v1_form_data: dict = {
        "MALLID": snap_format["partnerServiceId"],
        "PAYMENTCHANNEL": v1_channel_id,
        "PAYMENTCODE": snap_format["virtualAccountNo"],
        "STATUSTYPE": "/",
        "OCOID": snap_format["inquiryRequestId"]
        }
       
       return v1_form_data
    
    @staticmethod
    def v1_snap_converter(v1_data: str) -> dict:
        dict_response = xmltodict.parse(v1_data)
        remove_key = dict_response["INQUIRY_RESPONSE"]
        v1_rc = remove_key["RESPONSECODE"]
        snap_format = {}
        if v1_rc == "0000":
            snap_format["responseCode"] = "2002400"
        elif v1_rc == "3000" or v1_rc == "3001" or v1_rc == "3006":
            snap_format["responseCode"] = "4042412"
        elif v1_rc == "3002":
            snap_format["responseCode"] = "4042414"
        elif v1_rc == "3004":
            snap_format["responseCode"] = "4032400"
        elif v1_rc == "9999":
            snap_format["responseCode"] = "5002401"
        virtual_account_data = {
            "virtualAccountName": remove_key["NAME"] if remove_key["NAME"] is not None else None,
            "virtualAccountEmail": remove_key["EMAIL"] if remove_key["EMAIL"] is not None else None,
            "virtualAccountNo": remove_key["PAYMENTCODE"] if remove_key["PAYMENTCODE"] is not None else None,
            "totalAmount": {
                "value": remove_key["AMOUNT"] if remove_key["AMOUNT"] is not None else None,
                "currency": "IDR" if remove_key["CURRENCY"] is not None and remove_key["CURRENCY"] == "360" else None if remove_key["PURCHASECURRENCY"] is not None and remove_key["PURCHASECURRENCY"] == "360" else None
            },
            "additionalInfo": {
                "trxId": remove_key["TRANSIDMERCHANT"] if remove_key["TRANSIDMERCHANT"] is not None else None,
                "minAmount": remove_key["MINAMOUNT"] if remove_key["MINAMOUNT"] is not None else None,
                "maxAmount": remove_key["MAXAMOUNT"] if remove_key["MAXAMOUNT"] is not None else None,
            }
        }
        snap_format["virtualAccountData"] = virtual_account_data
        return snap_format