from datetime import datetime
import pytz
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
import base64
import jwt
from src.model.token.token_b2b_response import TokenB2BResponse

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
        try:
            payload: dict = jwt.decode(token_b2b.access_token, verify=False, algorithms = ['HS256'])
            return False
        except jwt.ExpiredSignatureError:
            return True