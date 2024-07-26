from doku_python_library.src.model.va.create_va_request import CreateVARequest
from doku_python_library.src.model.va.create_va_response import CreateVAResponse
from doku_python_library.src.services.token_service import TokenService
import requests, uuid, json, xmltodict
from doku_python_library.src.commons.config import Config
from doku_python_library.src.model.general.request_header_dto import RequestHeaderDto
from doku_python_library.src.model.va.update_va import UpdateVADto
from doku_python_library.src.model.va.update_va_response import UpdateVAResponse
from doku_python_library.src.model.va.check_status_va import CheckStatusDto
from doku_python_library.src.model.va.check_status_va_response import CheckStatusVAResponse
import xml.etree.ElementTree as ET
from doku_python_library.src.model.va.virtual_account_data import VirtualAccountData

class VaService:

    @staticmethod
    def generate_external_id() -> str:
        return uuid.uuid4().hex + TokenService.get_timestamp()

    @staticmethod
    def generate_request_header(channel_id: str, client_id: str, 
                                 token_b2b: str, timestamp: str, external_id: str, signature: str) -> RequestHeaderDto:
        header: RequestHeaderDto = RequestHeaderDto(
            x_timestamp= timestamp,
            x_signature= signature,
            x_partner_id= client_id,
            authorization= token_b2b,
            x_external_id= external_id,
            channel_id= channel_id
        )
        return header

    @staticmethod
    def creat_va(create_va_request: CreateVARequest, request_header: RequestHeaderDto, is_production: bool) -> CreateVAResponse:
        try:
            url: str = Config.get_base_url(is_production=is_production) + Config.CREATE_VA

            headers: RequestHeaderDto = request_header.to_json()

            response = requests.post(url=url, json=create_va_request.create_request_body(), headers=headers)
            response_json = response.json()
            va_response: CreateVAResponse = CreateVAResponse(**response_json) 
            return va_response
        except Exception as e:
            print("Failed Parse Response "+str(e))
    
    @staticmethod
    def do_update_va(request_header: RequestHeaderDto, update_va_request: UpdateVADto, is_production: bool) -> UpdateVAResponse:
        try:
            url: str = Config.get_base_url(is_production=is_production) + Config.UPDATE_VA

            headers: RequestHeaderDto = request_header.to_json()

            response = requests.put(url=url, json=update_va_request.create_request_body(), headers=headers)
            response_json = response.json()
            va_response: UpdateVAResponse = UpdateVAResponse(**response_json) 
            return va_response
        except Exception as e:
            print("Failed Parse Response "+str(e))
    
    @staticmethod
    def do_check_status_va(request_header: RequestHeaderDto, check_status_request: CheckStatusDto, is_production: bool) -> CheckStatusVAResponse:
        try:
            url: str = Config.get_base_url(is_production=is_production) + Config.CHECK_STATUS_VA

            headers: RequestHeaderDto = request_header.to_json()

            response = requests.post(url=url, json=check_status_request.create_request_body(), headers=headers)
            response_json = response.json()
            va_response: CheckStatusVAResponse = CheckStatusVAResponse(**response_json) 
            return va_response
        except Exception as e:
            print("Failed Parse Response "+str(e))

    @staticmethod
    def snap_v1_converter(snap_format: dict,) -> dict:
       v1_form_data: dict = {
        "MALLID": snap_format["partnerServiceId"],
        "PAYMENTCHANNEL": snap_format["additionalInfo"]["channel"],
        "PAYMENTCODE": snap_format["virtualAccountNo"],
        "STATUSTYPE": "/",
        "OCOID": snap_format["inquiryRequestId"]
        }
       
       return v1_form_data
    
    @staticmethod
    def v1_snap_converter(v1_data: str) -> dict:
        dict_response = xmltodict.parse(v1_data)
        remove_key = dict_response["INQUIRY_RESPONSE"]

        snap_format = {}
        virtual_account_data = {
            "virtualAccountName": remove_key["NAME"] if remove_key["NAME"] is not None else None,
            "virtualAccountEmail": remove_key["EMAIL"] if remove_key["EMAIL"] is not None else None,
            "virtualAccountNo": remove_key["PAYMENTCODE"] if remove_key["PAYMENTCODE"] is not None else None,
            "totalAmount": {
                "value": remove_key["AMOUNT"] if remove_key["AMOUNT"] is not None else None,
                "currency": remove_key["CURRENCY"] if remove_key["CURRENCY"] is not None else None if remove_key["PURCHASECURRENCY"] is not None else None
            },
            "additionalInfo": {
                "trxId": remove_key["TRANSIDMERCHANT"] if remove_key["TRANSIDMERCHANT"] is not None else None,
                "minAmount": remove_key["MINAMOUNT"] if remove_key["MINAMOUNT"] is not None else None,
                "maxAmount": remove_key["MAXAMOUNT"] if remove_key["MAXAMOUNT"] is not None else None,
            }
        }
        snap_format["virtualAccountData"] = virtual_account_data
        return snap_format