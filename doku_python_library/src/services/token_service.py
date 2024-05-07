from datetime import datetime, timedelta
import pytz
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
import base64
from doku_python_library.src.model.token.token_b2b_response import TokenB2BResponse
from datetime import datetime

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