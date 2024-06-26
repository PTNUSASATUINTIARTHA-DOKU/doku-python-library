from doku_python_library.src.commons.config import *
from doku_python_library.src.controller.token_controller import TokenController
from doku_python_library.src.model.token.token_b2b_response import TokenB2BResponse
from doku_python_library.src.services.token_service import TokenService
from doku_python_library.src.controller.va_controller import VaController
from doku_python_library.src.model.va.create_va_request import CreateVARequest
from doku_python_library.src.model.va.create_va_response import CreateVAResponse

class DokuSNAP :

    def __init__(self, private_key: str, client_id: str, is_production: bool, public_key: str) -> None:
        self.private_key = private_key
        self.client_id = client_id
        self.is_production = is_production
        self.public_key = public_key
        self.token_b2b = self._get_token()
        self.token: str = None
        self.token_expires_in: int = None
        self.token_generate_timestamp: str = None

        
    def _get_token(self) -> TokenB2BResponse:
        try:
            token_b2b_response: TokenB2BResponse = TokenController.getTokenB2B(
            private_key=self.private_key, 
            client_id=self.client_id, 
            is_production=self.is_production
            )
            self._set_token_b2b(token_b2b_response)
            return token_b2b_response
        except Exception as e:
            print("Error occured when get token "+str(e))
    
    def _set_token_b2b(self, token_b2b_response: TokenB2BResponse) -> None:
        self.token = token_b2b_response.access_token
        self.token_expires_in = token_b2b_response.expires_in
        self.token_generate_timestamp = token_b2b_response.generated_timestamp

    def createVA(self, create_va_request: CreateVARequest) -> CreateVAResponse:
        is_token_invalid: bool = TokenController.is_token_invalid(self.token_b2b, self.token_expires_in, self.token_generate_timestamp)
        if is_token_invalid:
            self._get_token()
        return VaController.createVa(
            is_production=self.is_production, 
            client_id=self.client_id, 
            access_token=self.token.access_token, 
            create_va_request=create_va_request,
            )
            

    