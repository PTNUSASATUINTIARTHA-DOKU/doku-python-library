from doku_python_library.src.model.va.create_va_request import CreateVARequest
from doku_python_library.src.model.va.create_va_response import CreateVAResponse
from doku_python_library.src.services.token_service import TokenService
import requests, uuid
from doku_python_library.src.commons.config import Config
from doku_python_library.src.model.general.request_header_dto import RequestHeaderDto

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
        url: str = Config.get_base_url(is_production=is_production) + Config.CREATE_VA

        headers: RequestHeaderDto = request_header.to_json()

        response = requests.post(url=url, json=create_va_request.create_request_body(), headers=headers)
        response_json = response.json()
        va_response: CreateVAResponse = CreateVAResponse(**response_json) 
        return va_response