from doku_python_library.src.commons.config import Config
from doku_python_library.src.services.token_service import TokenService
from doku_python_library.src.model.va.create_va_request import CreateVARequest
from doku_python_library.src.model.va.create_va_response import CreateVAResponse
import requests

class VaController:

    @staticmethod
    def createVa(is_production: bool, client_id: str, access_token: str, create_va_request: CreateVARequest) -> CreateVAResponse:
        url: str = Config.get_base_url(is_production=is_production) + "/virtual-accounts/bi-snap-va/v1/transfer-va/create-va"
        date_now = TokenService.get_timestamp()

        headers: dict = {
            "X-TIMESTAMP": date_now,
            "X-SIGNATURE": "",
            "X-PARTNER-ID": client_id,
            "X-EXTERNAL-ID": create_va_request.external_id,
            "CHANNEL-ID": create_va_request.channel_id,
            "Authorization": access_token
        }

        response = requests.post(url=url, json=create_va_request.create_request_body(), headers=headers)
        response_json = response.json()
        print(response_json)

    