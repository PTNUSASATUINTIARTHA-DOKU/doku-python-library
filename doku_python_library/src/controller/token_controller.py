from doku_python_library.src.model.token.token_b2b_response import TokenB2BResponse
from doku_python_library.src.commons.config import Config
from doku_python_library.src.model.token.token_b2b_request import TokenB2BRequest
from doku_python_library.src.services.token_service import TokenService
from flask import request
from doku_python_library.src.model.notification import NotificationToken
from doku_python_library.src.commons.snap_utils import SnapUtils
from doku_python_library.src.model.general.request_header import RequestHeader
from doku_python_library.src.services.va_service import VaService
from doku_python_library.src.model.token.token_b2b2c_request import TokenB2B2CRequest
from doku_python_library.src.model.token.token_b2b2c_response import TokenB2B2CResponse

class TokenController:

    @staticmethod
    def get_token_b2b(private_key: str, client_id: str, is_production: bool) -> TokenB2BResponse:
        timestamp = TokenService.get_timestamp()
        signature = TokenService.create_signature(private_key=private_key, text="{client_id}|{date}".format(client_id=client_id, date=timestamp))
        headers: dict = {
            "X-SIGNATURE": signature,
            "X-TIMESTAMP": timestamp,
            "X-CLIENT-KEY": client_id,
            "content-type": "application/json"
        }

        token_b2b_request: TokenB2BRequest = TokenService.create_token_b2b_request(
            signature=signature,
            timestamp=timestamp,
            client_id=client_id
        )
        return TokenService.create_token_b2b(token_b2b_request=token_b2b_request, is_production=is_production, headers=headers)
    
    @staticmethod
    def is_token_invalid(token: str, token_expires_in: int, token_generated_timestamp: str) -> bool:
        return TokenService.is_token_empty(token) or TokenService.is_token_expired(token_expires_in, token_generated_timestamp)
        
    @staticmethod
    def generate_token_b2b(expire_in: int, issuer: str, private_key: str, client_id: str) -> None:
       timestamp: str = TokenService.get_timestamp()
       token: str = TokenService.generate_token(
            expired_in= expire_in,
            issuer= issuer,
            private_key= private_key,
            client_id= client_id
        )
       return TokenService.generate_notification_token(
           token= token,
           timestamp= timestamp,
           client_id= client_id,
           expires_in= expire_in
        )
       
    @staticmethod
    def validate_token_b2b(token: str, public_key: str) -> bool:
        return TokenService.validate_token_b2b(token=token, public_key=public_key) is not None
    
    @staticmethod
    def validate_signature(client_id: str, public_key: str) -> bool:
        timestamp: str = request.headers.get("X-TIMESTAMP")
        request_signature: str = request.headers.get("X-SIGNATURE")
        return TokenService.compare_signatures(
            string_to_sign="{client_id}|{timestamp}".format(client_id=client_id, timestamp=timestamp),
            signature=request_signature,
            string_public_key=public_key
        )
    
    @staticmethod
    def generate_invalid_signature_response() -> NotificationToken:
        timestamp: str = TokenService.get_timestamp()
        return TokenService.generate_invalid_signature(timestamp= timestamp)
    
    @staticmethod
    def do_generate_request_header(private_key: str, client_id: str, token_b2b: str) -> RequestHeader:
        external_id: str = SnapUtils.generate_external_id()
        timestamp: str = TokenService.get_timestamp()
        signature: str = TokenService.create_signature(
            private_key= private_key,
            text= "{client_id}|{date}".format(client_id=client_id, date=timestamp)
        )
        return VaService.generate_request_header(
            channel_id="SDK",
            client_id= client_id,
            token_b2b=token_b2b,
            timestamp= timestamp,
            external_id=external_id,
            signature=signature
        )
    
    @staticmethod
    def get_token_b2b2c(auth_code: str, private_key: str, 
                        client_id: str, is_production: bool) -> TokenB2B2CResponse:
        timestamp: str = TokenService.get_timestamp()
        signature: str = TokenService.create_signature(
            private_key=private_key,
            text="{client_id}|{date}".format(client_id=client_id, date=timestamp)
        )
        request: TokenB2B2CRequest = TokenService.create_token_b2b2c_request(
            auth_code=auth_code
        )
        return TokenService.create_token_b2b2c(
            request=request,
            timestamp=timestamp,
            signature=signature,
            client_id=client_id,
            is_production=is_production
        )
