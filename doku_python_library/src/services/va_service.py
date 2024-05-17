from doku_python_library.src.model.va.create_va_request import CreateVARequest
from doku_python_library.src.model.va.create_va_response import CreateVAResponse
from doku_python_library.src.services.token_service import TokenService
import hashlib, requests
from doku_python_library.src.commons.config import Config

class VaService:

    @staticmethod
    def createVa(create_va_request: CreateVARequest, is_production: bool, client_id: str, access_token: str) -> CreateVAResponse:
        url: str = Config.get_base_url(is_production=is_production) + "/virtual-accounts/bi-snap-va/v1/transfer-va/create-va"
        timestamp = TokenService.get_timestamp()

        request_body_minify = str(create_va_request.create_request_body())
        hash_object = hashlib.sha256()
        hash_object.update(request_body_minify.encode('utf-8'))
        data_hex = hash_object.hexdigest()
        data_hex_lower = data_hex.lower()
        
        string_to_sign = "POST:{url}:{token}:{request_body}:{timestamp}".format(url="/bi-snap-va/v1/transfer-va/create-va", token=access_token, request_body=data_hex_lower, timestamp=timestamp)
        signature = TokenService.create_signature_hmac512("SK-BxcAg84e6gIbuYw3Vf8s", string_to_sign)
        headers: dict = {
            "X-TIMESTAMP": timestamp,
            "X-SIGNATURE": signature,
            "X-PARTNER-ID": client_id,
            "X-EXTERNAL-ID": timestamp,
            "CHANNEL-ID": create_va_request.additional_info.channel,
            "Authorization": access_token
        }

        response = requests.post(url=url, json=create_va_request.create_request_body(), headers=headers)
        response_json = response.json()
        va_response: CreateVAResponse = CreateVAResponse(**response_json) 
        return va_response