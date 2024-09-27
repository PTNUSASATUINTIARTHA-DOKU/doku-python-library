from datetime import datetime, timedelta
import pytz
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import base64
from doku_python_library.src.model.token.token_b2b_response import TokenB2BResponse
from doku_python_library.src.model.token.token_b2b_request import TokenB2BRequest
from doku_python_library.src.commons.config import Config
from datetime import datetime
import hmac, requests
import hashlib
import jwt
from jwt.exceptions import InvalidTokenError
import time
from doku_python_library.src.model.notification.notification_token import NotificationToken
from doku_python_library.src.model.notification.notification_token_header import NotificationTokenHeader
from doku_python_library.src.model.notification.notification_token_body import NotificationTokenBody
from doku_python_library.src.model.token.token_b2b2c_request import TokenB2B2CRequest
from doku_python_library.src.model.token.token_b2b2c_response import TokenB2B2CResponse
import json

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
        priv_key = serialization.load_pem_private_key(
            private_key.encode('utf-8'),
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
    def generate_symmetric_signature(http_method: str, endpoint: str, token_b2b: str, 
                                     request: dict, timestamp: str, secret_key: str):
        request_body_minify = json.dumps(request, separators=(',', ':'))
        hash_object = hashlib.sha256()
        hash_object.update(request_body_minify.encode('utf-8'))
        data_hex = hash_object.hexdigest()
        data_hex_lower = data_hex.lower()
        
        string_to_sign = "{method}:{url}:{token}:{request_body}:{timestamp}".format(method=http_method, url=endpoint, token=token_b2b, request_body=data_hex_lower, timestamp=timestamp)
        return base64.b64encode(hmac.new(secret_key.encode("utf-8"), msg=string_to_sign.encode("utf-8"), digestmod=hashlib.sha512).digest()).decode()      
    
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
        url: str = Config.get_base_url(is_production=is_production) + Config.ACCESS_TOKEN
        response = requests.post(url=url, json=token_b2b_request.create_request_body(), headers=headers)
        response_json = response.json()
        token_response: TokenB2BResponse = TokenB2BResponse(**response_json)
        if(token_response.response_code == "2007300"):
            token_response.generated_timestamp = token_b2b_request.timestamp
            token_response.expires_in = token_response.expires_in - 10
        return token_response
    
    @staticmethod
    def is_token_expired(token_expires_in: int, token_generated_timestamp: str) -> bool:
        generated_time = datetime.strptime(token_generated_timestamp, "%Y-%m-%dT%H:%M:%SZ")
        expired_date = generated_time + timedelta(seconds= token_expires_in if not isinstance(token_expires_in, str) else 890)
        date_now = datetime.strptime(TokenService.get_timestamp(), "%Y-%m-%dT%H:%M:%SZ")
        return expired_date > date_now
    
    @staticmethod
    def is_token_empty(token: str) -> bool:
        return token is None
    
    @staticmethod
    def validate_token_b2b(token: str, public_key: str) -> dict:
        try:
            decoded_token = jwt.decode(token, public_key, algorithms=["RS256"])
            return decoded_token
        except InvalidTokenError as e:
            return None
        
    @staticmethod
    def generate_token(expired_in: int, issuer: str, private_key: str, client_id: str) -> str:
        expires: int = int(time.time()) + expired_in
        payload: dict = {
            "exp": expires,
            "issuer": issuer,
            "clientId": client_id
        }
        token = jwt.encode(payload= payload, key=private_key, algorithm='RS256')
        return token.decode('utf-8') if not isinstance(token, str) else token
    
    @staticmethod
    def generate_notification_token(token: str, timestamp: str, client_id: str, expires_in: int) -> NotificationToken:
        header: NotificationTokenHeader = NotificationTokenHeader(
            client_id= client_id, timestamp= timestamp
        )
        body: NotificationTokenBody = NotificationTokenBody(
            responseCode= "2007300",
            responseMessage= "Successful",
            accessToken= token,
            tokenType= "Bearer",
            expiresIn= expires_in,
            additionalInfo= ""
        )
        response: NotificationToken = NotificationToken(
            header= header,
            body= body
        )
        return response
    
    @staticmethod
    def compare_signatures(string_to_sign, signature, string_public_key):
        try:
            string_public_key = string_public_key.replace("-----BEGIN PUBLIC KEY-----", "")
            string_public_key = string_public_key.replace("-----END PUBLIC KEY-----", "")
            string_public_key = string_public_key.replace("\n", "")
            
            missing_padding = len(string_public_key) % 4
            if missing_padding:
                string_public_key += '=' * (4 - missing_padding)
            
            decoded_public_key = base64.b64decode(string_public_key)
            public_key = serialization.load_der_public_key(
                decoded_public_key,
                backend=default_backend()
            )
            decoded_signature = base64.b64decode(signature)
            
            public_key.verify(
                decoded_signature,  
                string_to_sign.encode("utf-8"),  
                padding.PKCS1v15(),  
                hashes.SHA256()  
            )
            
            return True
        except Exception as e:
            print(f"Error verifying signature: {str(e)}")
            return False
    
    @staticmethod
    def generate_invalid_signature(timestamp: str) -> NotificationToken:
        header: NotificationTokenHeader = NotificationTokenHeader(
            client_id= None, timestamp= timestamp
        )
        body: NotificationTokenBody = NotificationTokenBody(
            responseCode= "4017300",
            responseMessage= "Unauthorized.Invalid Signature",
            accessToken= None,
            tokenType= None,
            expiresIn= None,
            additionalInfo= None
        )
        return NotificationToken(header= header, body= body)
    
    @staticmethod
    def create_token_b2b2c_request(auth_code: str) -> TokenB2B2CRequest:
        return TokenB2B2CRequest(
            grant_type="authorization_code",
            auth_code=auth_code,
        )

    @staticmethod
    def create_token_b2b2c(request: TokenB2B2CRequest, timestamp: str, signature: str, client_id: str, is_production: bool) -> TokenB2B2CResponse:
        url: str = Config.get_base_url(is_production=is_production) + Config.ACCESS_TOKEN_B2B2C
        headers: dict = {
            "content-type": "application/json",
            "X-SIGNATURE": signature,
            "X-TIMESTAMP": timestamp,
            "X-CLIENT-KEY": client_id
        }
        response = requests.post(url=url, json=request.create_request_body(), headers=headers)
        response_json = response.json()
        token_response: TokenB2B2CResponse = TokenB2B2CResponse(**response_json)
        if token_response.response_code.startswith("200"):
            token_response.generated_timestamp = timestamp
            token_response.access_token_expiry_time = token_response.access_token_expiry_time
        return token_response