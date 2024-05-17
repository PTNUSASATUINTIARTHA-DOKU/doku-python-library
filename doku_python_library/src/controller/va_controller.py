from doku_python_library.src.commons.config import Config
from doku_python_library.src.services.token_service import TokenService
from doku_python_library.src.model.va.create_va_request import CreateVARequest
from doku_python_library.src.model.va.create_va_response import CreateVAResponse
from doku_python_library.src.services.va_service import VaService

class VaController:

    @staticmethod
    def createVa(is_production: bool, client_id: str, access_token: str, create_va_request: CreateVARequest) -> CreateVAResponse:
        return VaService.createVa(create_va_request=create_va_request, is_production=is_production, client_id=client_id, access_token=access_token)

    