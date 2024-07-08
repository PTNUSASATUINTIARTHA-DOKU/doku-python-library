from doku_python_library.src.model.va.create_va_request import CreateVARequest
from doku_python_library.src.model.va.create_va_response import CreateVAResponse
from doku_python_library.src.services.va_service import VaService
from doku_python_library.src.model.general.request_header_dto import RequestHeaderDto
from doku_python_library.src.services.token_service import TokenService
from doku_python_library.src.commons.config import Config
from doku_python_library.src.model.va.update_va import UpdateVADto
from doku_python_library.src.model.va.update_va_response import UpdateVAResponse

class VaController:
    
    @staticmethod
    def create_va(is_production: bool, client_id: str, token_b2b: str, create_va_request: CreateVARequest, secret_key: str) -> CreateVAResponse:
        external_id: str = VaService.generate_external_id()
        timestamp: str = TokenService.get_timestamp()
        signature: str = TokenService.generate_symmetric_signature(
            http_method= "POST",
            endpoint= Config.CREATE_VA,
            token_b2b= token_b2b,
            request= create_va_request.create_request_body(),
            timestamp= timestamp,
            secret_key= secret_key
        )
        request_header: RequestHeaderDto = VaService.generate_request_header(
            channel_id= create_va_request.additional_info.channel,
            client_id= client_id,
            token_b2b= token_b2b,
            timestamp= timestamp,
            external_id=external_id,
            signature= signature
        )
        return VaService.creat_va(create_va_request=create_va_request, request_header= request_header, is_production= is_production)

    @staticmethod
    def do_update_va(update_va_request: UpdateVADto, secret_key: str, client_id: str, token_b2b: str, is_production: bool) -> UpdateVAResponse:
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
        external_id: str = VaService.generate_external_id()
        request_header: RequestHeaderDto = VaService.generate_request_header(
            channel_id= update_va_request.additional_info.channel,
            client_id= client_id,
            token_b2b= token_b2b,
            timestamp= timestamp,
            external_id= external_id,
            signature= signature
        )
        return VaService.do_update_va(request_header= request_header, update_va_request= update_va_request, is_production=is_production)