from doku_python_library.src.model.token.token_b2b_response import TokenB2BResponse
from doku_python_library.src.commons.config import Config
from doku_python_library.src.model.token.token_b2b_request import TokenB2BRequest

from doku_python_library.src.services.token_service import TokenService


class TokenController:

    @staticmethod
    def getTokenB2B(private_key: str, client_id: str, is_production: bool) -> TokenB2BResponse:
        timestamp = TokenService.get_timestamp()
        signature = TokenService.create_signature(private_key=private_key, text="{client_id}|{date}".format(client_id=client_id, date=timestamp))
        headers: dict = {
            "X-Signature": signature,
            "X-Timestamp": timestamp,
            "X-Client-Key": client_id,
            "content-type": "application/json"
        }

        token_b2b_request: TokenB2BRequest = TokenService.create_token_b2b_request(
            signature=signature,
            timestamp=timestamp,
            client_id=client_id
        )
        return TokenService.create_token_b2b(token_b2b_request=token_b2b_request, is_production=is_production, headers=headers)
    