from doku_python_library.src.model.va.create_va_request import CreateVARequest
from doku_python_library.src.model.va.create_va_response import CreateVAResponse
from doku_python_library.src.services.va_service import VaService
from doku_python_library.src.model.general.request_header_dto import RequestHeaderDto
from doku_python_library.src.services.token_service import TokenService

class VaController:
    
    @staticmethod
    def create_va(is_production: bool, client_id: str, token_b2b: str, create_va_request: CreateVARequest, secret_key: str) -> CreateVAResponse:
        external_id: str = VaService.generate_external_id()
        timestamp: str = TokenService.get_timestamp()
        request_header: RequestHeaderDto = VaService.create_va_request_header(
            create_va_request= create_va_request,
            secret_key= secret_key,
            client_id= client_id,
            token_b2b= token_b2b,
            timestamp= timestamp,
            external_id=external_id
        )
        return VaService.creat_va(create_va_request=create_va_request, request_header= request_header, is_production= is_production)

    