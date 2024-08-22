from doku_python_library.src.commons.config import *
from doku_python_library.src.controller.token_controller import TokenController
from doku_python_library.src.model.token.token_b2b_response import TokenB2BResponse
from doku_python_library.src.controller.va_controller import VaController
from doku_python_library.src.model.va.create_va_request import CreateVARequest
from doku_python_library.src.model.va.create_va_response import CreateVAResponse
from doku_python_library.src.model.va.update_va_request import UpdateVaRequest
from doku_python_library.src.model.va.update_va_response import UpdateVAResponse
from doku_python_library.src.model.va.check_status_va_request import CheckStatusRequest
from doku_python_library.src.model.va.check_status_va_response import CheckStatusVAResponse
from doku_python_library.src.model.notification.notification_token import NotificationToken
from doku_python_library.src.model.va.delete_va_request import DeleteVARequest
from doku_python_library.src.model.va.delete_va_response import DeleteVAResponse
from doku_python_library.src.model.notification.notification_payment_request import PaymentNotificationRequest
from doku_python_library.src.model.notification.notification_payment_body_response import PaymentNotificationResponseBody
from doku_python_library.src.model.general.request_header import RequestHeader
from doku_python_library.src.controller.notification_controler import NotificationController

class DokuSNAP :

    def __init__(self, private_key: str, client_id: str, is_production: bool, public_key: str, issuer: str, secret_key: str) -> None:
        self.private_key = private_key
        self.client_id = client_id
        self.is_production = is_production
        self.public_key = public_key
        self.issuer = issuer
        self.get_token()
        self.token_b2b: TokenB2BResponse
        self.token: str
        self.token_expires_in: int
        self.token_generate_timestamp: str
        self.secret_key = secret_key

        
    def get_token(self) -> TokenB2BResponse:
        try:
            token_b2b_response: TokenB2BResponse = TokenController.get_token_b2b(
            private_key=self.private_key, 
            client_id=self.client_id, 
            is_production=self.is_production
            )
            if token_b2b_response is not None:
                self._set_token_b2b(token_b2b_response)
            return token_b2b_response
        except Exception as e:
            print("Error occured when get token "+str(e))
    
    def _set_token_b2b(self, token_b2b_response: TokenB2BResponse) -> None:
        self.token_b2b = token_b2b_response
        self.token = token_b2b_response.access_token
        self.token_expires_in = token_b2b_response.expires_in
        self.token_generate_timestamp = token_b2b_response.generated_timestamp

    def create_va(self, create_va_request: CreateVARequest) -> CreateVAResponse:
        try:
            create_va_request.validate_va_request()
            is_token_invalid: bool = TokenController.is_token_invalid(self.token_b2b, self.token_expires_in, self.token_generate_timestamp)
            if is_token_invalid:
                self.get_token()
            return VaController.create_va(
                is_production= self.is_production,
                client_id= self.client_id,
                token_b2b= self.token,
                create_va_request= create_va_request,
                secret_key= self.secret_key
            )
        except Exception as e:
            print("• Exception --> "+str(e))
    
    def update_va(self, update_request: UpdateVaRequest) -> UpdateVAResponse:
        try:
            update_request.validate_update_va_request()
            is_token_invalid: bool = TokenController.is_token_invalid(self.token_b2b, self.token_expires_in, self.token_generate_timestamp)
            if is_token_invalid:
                self.get_token()
            return VaController.do_update_va(
                update_va_request= update_request,
                secret_key= self.secret_key,
                client_id= self.client_id,
                token_b2b= self.token,
                is_production= self.is_production
            )
        except Exception as e:
            print("• Exception --> "+str(e)) 
            
    
    def check_status_va(self, check_status_request: CheckStatusRequest) -> CheckStatusVAResponse:
        try:
            check_status_request.validate_check_status_request()
            is_token_invalid: bool = TokenController.is_token_invalid(self.token_b2b, self.token_expires_in, self.token_generate_timestamp)
            if is_token_invalid:
                self.get_token()
            return VaController.do_check_status_va(
                check_status_request= check_status_request,
                secret_key= self.secret_key,
                client_id= self.client_id,
                token_b2b= self.token,
                is_production= self.is_production
            )
        except Exception as e:
            print("• Exception --> "+str(e))
    
    def delete_payment_code(self, delete_va_request: DeleteVARequest) -> DeleteVAResponse:
        try:
            delete_va_request.validate_delete_request()
            is_token_invalid: bool = TokenController.is_token_invalid(self.token_b2b, self.token_expires_in, self.token_generate_timestamp)
            if is_token_invalid:
                self.get_token()
            return VaController.do_delete_payment_code(
                delete_va_request= delete_va_request,
                secret_key= self.secret_key,
                client_id= self.client_id,
                token_b2b= self.token,
                is_production= self.is_production
            )
        except Exception as e:
            print("• Exception --> "+str(e))
        
    def validate_signature(self) -> bool:
        return TokenController.validate_signature(
            private_key= self.private_key,
            client_id= self.client_id
        )
    
    def generate_token_b2b(self, is_signature_valid: bool) -> NotificationToken:
        if is_signature_valid:
            return TokenController.generate_token_b2b(
                expire_in= self.token_expires_in,
                issuer= self.issuer,
                private_key= self.private_key,
                client_id=  self.client_id
            )
        return TokenController.generate_invalid_signature_response()
    
    def validate_token_b2b(self, request_token: str) -> bool:
        return TokenController.validate_token_b2b(token= request_token, public_key= self.public_key)
    
    def validate_signature_and_generate_token(self) -> NotificationToken:
        is_signature_valid: bool = self.validate_signature()
        return self.generate_token_b2b(is_signature_valid= is_signature_valid)
    
    def generate_notification_response(self, is_token_valid: bool, request: PaymentNotificationRequest) -> PaymentNotificationResponseBody:
        try:
            if is_token_valid:
                if request is not None:
                    return NotificationController.generate_notification_response(request=request)
            
            return NotificationController.generate_invalid_token_response(request=request)
        except Exception as e:
            print("• Exception --> "+str(e))
    
    def validate_token_and_generate_notification_response(self, header: RequestHeader, request: PaymentNotificationRequest) -> PaymentNotificationResponseBody:
        is_token_valid: bool = self.validate_token_b2b(request_token= header.authorization)
        return self.generate_notification_response(is_token_valid=is_token_valid, request=request)

    def generate_request_header(self) -> RequestHeader:
        is_token_invalid: bool = TokenController.is_token_invalid(
            token_b2b=self.token,
            token_expires_in=self.token_expires_in,
            token_generated_timestamp=self.token_generate_timestamp
        )

        if is_token_invalid:
            token_b2b_response = TokenController.get_token_b2b(
                private_key=self.private_key,
                client_id=self.client_id,
                is_production=self.is_production
            )
            if token_b2b_response is not None:
                    self._set_token_b2b(token_b2b_response)
            
        request_header: RequestHeader = TokenController.do_generate_request_header(
            private_key=self.private_key,
            client_id=self.client_id,
            token_b2b=self.token
        )
        return request_header
    
    def direct_inquiry_request_mapping(self, header: dict, snap_format: dict) -> dict:
        return VaController.direct_inquiry_request_mapping(
            header=header, 
            snap_format=snap_format
        )
    
    def direct_inquiry_response_mapping(self, v1_data: str) -> dict:
        return VaController.direct_inquiry_response_mapping(v1_data=v1_data)