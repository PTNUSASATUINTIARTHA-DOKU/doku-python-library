from datetime import datetime, timedelta
import pytz
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
import base64
from doku_python_library.src.model.token.token_b2b_response import TokenB2BResponse
from doku_python_library.src.model.token.token_b2b_request import TokenB2BRequest
from doku_python_library.src.commons.config import Config
from datetime import datetime
import hmac, requests
import hashlib

class TokenService:

    @staticmethod
    def get_timestamp() -> str:
        now = datetime.now()
        utc_timezone = pytz.utc
        utc_time_now = now.astimezone(utc_timezone)
        date_string = utc_time_now.strftime('%Y-%m-%dT%H:%M:%SZ')
        return date_string
    
    @staticmethod
    def create_signature(private_key: str, text: str) -> str:
        with open(private_key, "rb") as key_file:
            priv_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
            )
        signature = priv_key.sign(
            text.encode('utf-8'),
            padding=padding.PKCS1v15(),
            algorithm=hashes.SHA256()
        )
        decode_signature = base64.encodebytes(signature).decode()
        return decode_signature.replace('\n', '')

    @staticmethod
    def check_token_expired(token_b2b: TokenB2BResponse) -> bool:
        generated_time = datetime.strptime(token_b2b.generated_timestamp, "%Y-%m-%dT%H:%M:%SZ")
        expired_date = generated_time + timedelta(seconds=token_b2b.expires_in)
        date_now = datetime.strptime(TokenService.get_timestamp(), "%Y-%m-%dT%H:%M:%SZ")
        return expired_date > date_now
    
    @staticmethod
    def create_signature_hmac512(secret_key: str, text: str):
        return base64.b64encode(hmac.new(secret_key.encode("utf-8"), msg=text.encode("utf-8"), digestmod=hashlib.sha512).digest()).decode()      
    
    @staticmethod
    def create_token_b2b_request(signature: str, timestamp: str, client_id: str) -> TokenB2BRequest:
        token_b2b_request: TokenB2BRequest = TokenB2BRequest(
            signature=signature,
            timestamp=timestamp,
            client_id=client_id
        )
        return token_b2b_request

    @staticmethod
    def create_token_b2b(token_b2b_request: TokenB2BRequest, is_production: bool, headers: dict) -> TokenB2BResponse:
        url: str = Config.get_base_url(is_production=is_production) + "/authorization/v1/access-token/b2b"
        response = requests.post(url=url, json=token_b2b_request.create_request_body(), headers=headers)
        response_json = response.json()
        token_response: TokenB2BResponse = TokenB2BResponse(**response_json)
        if(token_response.response_code == "2007300"):
            token_response.generated_timestamp = token_b2b_request.timestamp
            token_response.expires_in = token_response.expires_in - 10
        return token_response