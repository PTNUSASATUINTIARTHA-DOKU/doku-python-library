from doku_python_library.src.model.va.create_va_request import CreateVARequest
from doku_python_library.src.model.va.create_va_response import CreateVAResponse
from doku_python_library.src.services.va_service import VaService
from doku_python_library.src.model.general.request_header import RequestHeader
from doku_python_library.src.services.token_service import TokenService
from doku_python_library.src.commons.config import Config
from doku_python_library.src.model.va.update_va_request import UpdateVaRequest
from doku_python_library.src.model.va.update_va_response import UpdateVAResponse
from doku_python_library.src.model.va.check_status_va_request import CheckStatusRequest
from doku_python_library.src.model.va.check_status_va_response import CheckStatusVAResponse
from doku_python_library.src.model.va.delete_va_response import DeleteVAResponse
from doku_python_library.src.model.va.delete_va_request import DeleteVARequest
from doku_python_library.src.commons.snap_utils import SnapUtils
from doku_python_library.src.model.inquiry.inquiry_response_body import InquiryResponseBody

class VaController:
    
    @staticmethod
    def create_va(is_production: bool, client_id: str, token_b2b: str, create_va_request: CreateVARequest, secret_key: str) -> CreateVAResponse:
        external_id: str = SnapUtils.generate_external_id()
        timestamp: str = TokenService.get_timestamp()
        signature: str = TokenService.generate_symmetric_signature(
            http_method= "POST",
            endpoint= Config.CREATE_VA,
            token_b2b= token_b2b,
            request= create_va_request.create_request_body(),
            timestamp= timestamp,
            secret_key= secret_key
        )
        request_header: RequestHeader = VaService.generate_request_header(
            channel_id= "SDK",
            client_id= client_id,
            token_b2b= token_b2b,
            timestamp= timestamp,
            external_id=external_id,
            signature= signature
        )
        return VaService.creat_va(create_va_request=create_va_request, request_header= request_header, is_production= is_production)

    @staticmethod
    def do_update_va(update_va_request: UpdateVaRequest, secret_key: str, client_id: str, token_b2b: str, is_production: bool) -> UpdateVAResponse:
        timestamp: str = TokenService.get_timestamp()
        endpoint: str = Config.UPDATE_VA
        method: str = "PUT"
        signature: str = TokenService.generate_symmetric_signature(
            http_method= method,
            endpoint= endpoint,
            token_b2b= token_b2b,
            request= update_va_request.create_request_body(),
            timestamp= timestamp,
            secret_key= secret_key
        )
        external_id: str = SnapUtils.generate_external_id()
        request_header: RequestHeader = VaService.generate_request_header(
            channel_id= "SDK",
            client_id= client_id,
            token_b2b= token_b2b,
            timestamp= timestamp,
            external_id= external_id,
            signature= signature
        )
        return VaService.do_update_va(request_header= request_header, update_va_request= update_va_request, is_production=is_production)
    
    @staticmethod
    def do_check_status_va(check_status_request: CheckStatusRequest, secret_key: str, client_id: str, token_b2b: str, is_production: bool) -> CheckStatusVAResponse:
        timestamp: str = TokenService.get_timestamp()
        endpoint: str = Config.CHECK_STATUS_VA
        method: str = "POST"
        signature: str = TokenService.generate_symmetric_signature(
            http_method= method,
            endpoint= endpoint,
            token_b2b= token_b2b,
            request= check_status_request.create_request_body(),
            timestamp= timestamp,
            secret_key= secret_key
        )
        external_id: str = SnapUtils.generate_external_id()
        request_header: RequestHeader = VaService.generate_request_header(
            channel_id= "SDK",
            client_id= client_id,
            token_b2b= token_b2b,
            timestamp= timestamp,
            external_id= external_id,
            signature= signature
        )
        return VaService.do_check_status_va(request_header= request_header, check_status_request= check_status_request, is_production= is_production)
    
    @staticmethod
    def do_delete_payment_code(delete_va_request: DeleteVARequest, secret_key: str, client_id: str, token_b2b: str, is_production: bool) -> DeleteVAResponse:
        timestamp: str = TokenService.get_timestamp()
        endpoint: str = Config.DELETE_VA
        method: str = "DELETE"
        signature: str = TokenService.generate_symmetric_signature(
            http_method= method,
            endpoint= endpoint,
            token_b2b= token_b2b,
            request= delete_va_request.create_request_body(),
            timestamp= timestamp,
            secret_key= secret_key
        )
        external_id: str = SnapUtils.generate_external_id()
        request_header: RequestHeader = VaService.generate_request_header(
            channel_id= "SDK",
            client_id= client_id,
            token_b2b= token_b2b,
            timestamp= timestamp,
            external_id= external_id,
            signature= signature
        )
        return VaService.do_delete_payment_code(request_header= request_header, delete_va_request= delete_va_request, is_production= is_production)
    
    @staticmethod
    def direct_inquiry_request_mapping(header: dict, snap_format: dict) -> dict:
        return VaService.direct_inquiry_request_mapping(header=header, snap_format=snap_format)
    

    @staticmethod
    def direct_inquiry_response_mapping(v1_data: str) -> InquiryResponseBody:
        return VaService.direct_inquiry_response_mapping(v1_data=v1_data)