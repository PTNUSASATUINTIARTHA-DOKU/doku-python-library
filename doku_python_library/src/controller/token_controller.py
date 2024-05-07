from doku_python_library.src.model.token.token_b2b_response import TokenB2BResponse
from doku_python_library.src.commons.config import Config
from doku_python_library.src.model.token.token_b2b_request import TokenB2BRequest
import requests

from doku_python_library.src.services.token_service import TokenService


class TokenController:

    @staticmethod
    def getTokenB2B(private_key: str, client_id: str, is_production: bool) -> TokenB2BResponse:
        url: str = Config.get_base_url(is_production=is_production) + "/authorization/v1/access-token/b2b"
        date_now = TokenService.get_timestamp()
        signature = TokenService.create_signature(private_key=private_key, text="{client_id}|{date}".format(client_id=client_id, date=date_now))
        headers: dict = {
            "X-Signature": signature,
            "X-Timestamp": date_now,
            "X-Client-Key": client_id,
            "content-type": "application/json"
        }

        token_b2b_request: TokenB2BRequest = TokenB2BRequest(
            signature=signature,
            timestamp=date_now,
            client_id=client_id
        )

        response = requests.post(url=url, json=token_b2b_request.create_request_body(), headers=headers)
        response_json = response.json()
        token_response: TokenB2BResponse = TokenB2BResponse(**response_json)
        if(token_response.response_code == "2007300"):
            token_response.generated_timestamp = date_now
            token_response.expires_in = token_response.expires_in - 10
        return token_response
    