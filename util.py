from doku_python_library.src.model.token import TokenB2BResponse
from doku_python_library.src.model.va.create_va_request import CreateVARequest
from doku_python_library.src.model.va.total_amount import TotalAmount
from doku_python_library.src.model.general.request_header import RequestHeader
from doku_python_library.src.model.va.additional_info import AdditionalInfo
from doku_python_library.src.model.va.additional_info_response import AdditionalInfoResponse
from doku_python_library.src.services.token_service import TokenService
from doku_python_library.src.model.va.create_va_response import CreateVAResponse
from doku_python_library.src.model.va.virtual_account_config import VirtualAccountConfig

class Util:

    CLIENT_ID: str = "clientId"
    PUBLIC_KEY: str = "publicKey"
    PRIVATE_KEY: str = "privateKey"
    TOKEN_B2B: str = "tokenb2b"
    SECRET_KEY: str = "secretKey"

    @staticmethod
    def generate_request_header() -> RequestHeader:
        return RequestHeader(
            x_timestamp="",
            x_signature="",
            x_partner_id="",
            x_external_id="",
            authorization="",
            channel_id=""
        )

    @staticmethod
    def generate_tokenb2b_response(response_code: str) -> TokenB2BResponse:
        return TokenB2BResponse(
            responseCode=response_code,
            responseMessage="Successful",
            accessToken= Util.TOKEN_B2B,
            tokenType= "Bearer",
            expiresIn=890
        )

    @staticmethod
    def generate_create_va_request() -> CreateVARequest:
        return CreateVARequest(
        partner_service_id= "    1899",
        virtual_acc_name= "Toru Yamashitas",
        trx_id= TokenService.get_timestamp(),
        virtual_acc_trx_type= "C",
        total_amount= TotalAmount(value="150000.00", currency="IDR"),
        additional_info= AdditionalInfo(channel="VIRTUAL_ACCOUNT_BANK_CIMB", virtual_account_config= VirtualAccountConfig(
            reusable_status=False,
            )),
        expired_date="2025-07-11T10:55:00+07:00",
        customer_no="20240715001",
        virtual_account_no="    189920240715001"
    )
    
    @staticmethod
    def generate_create_va_response(response_code: str) -> CreateVAResponse:
        return CreateVAResponse(
            responseCode=response_code,
            responseMessage="Successful",
            virtualAccountData=None
        )