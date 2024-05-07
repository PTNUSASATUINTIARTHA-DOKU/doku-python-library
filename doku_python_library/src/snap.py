from doku_python_library.src.commons.config import *
from doku_python_library.src.controller.token_controller import TokenController
from doku_python_library.src.model.token.token_b2b_response import TokenB2BResponse
from doku_python_library.src.services.token_service import TokenService
from doku_python_library.src.controller.va_controller import VaController
from doku_python_library.src.model.va.create_va_request import CreateVARequest
from doku_python_library.src.model.va.create_va_response import CreateVAResponse

class DokuSNAP :

    def __init__(self, private_key: str, client_id: str, is_production: bool) -> None:
        self.private_key = private_key
        self.client_id = client_id
        self.is_production = is_production
        self.token: TokenB2BResponse = self._get_token()
        
    def _get_token(self) -> TokenB2BResponse:
        try:
            return TokenController.getTokenB2B(
            private_key=self.private_key, 
            client_id=self.client_id, 
            is_production=self.is_production
            )
        except Exception as e:
            print("Error occured when get token "+str(e))
    
    def createVA(self, create_va_request: CreateVARequest) -> CreateVAResponse:
        if(self.token is not None):
            is_token_expired: bool = TokenService.check_token_expired(self.token)
            if is_token_expired:
                self.token = self._get_token()
        else:
            self.token = self._get_token()
        return VaController.createVa(is_production=self.is_production, client_id=self.client_id, access_token=self.token.access_token, create_va_request=create_va_request)
            

    