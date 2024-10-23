from doku_python_library.src.commons.config import *
from doku_python_library.src.controller.token_controller import TokenController
from doku_python_library.src.model.token.token_b2b_response import TokenB2BResponse
from doku_python_library.src.controller.va_controller import VaController
from doku_python_library.src.model.va.create_va_request import CreateVARequest
from doku_python_library.src.model.va.create_va_response import CreateVAResponse
from doku_python_library.src.model.va.update_va_request import UpdateVaRequest
from doku_python_library.src.model.va.update_va_response import UpdateVAResponse
from doku_python_library.src.model.va.check_status_va_request import CheckStatusRequest as va_status
from doku_python_library.src.model.va.check_status_va_response import CheckStatusVAResponse
from doku_python_library.src.model.notification.notification_token import NotificationToken
from doku_python_library.src.model.va.delete_va_request import DeleteVARequest
from doku_python_library.src.model.va.delete_va_response import DeleteVAResponse
from doku_python_library.src.model.notification.notification_payment_request import PaymentNotificationRequest
from doku_python_library.src.model.notification.notification_payment_body_response import PaymentNotificationResponseBody
from doku_python_library.src.model.general.request_header import RequestHeader
from doku_python_library.src.controller.notification_controler import NotificationController
from doku_python_library.src.model.direct_debit.account_binding_request import AccountBindingRequest
from doku_python_library.src.model.direct_debit.account_binding_response import AccountBindingResponse
from doku_python_library.src.controller.direct_debit_controller import DirectDebitController
from doku_python_library.src.model.token.token_b2b2c_response import TokenB2B2CResponse
from doku_python_library.src.model.direct_debit.payment_request import PaymentRequest
from doku_python_library.src.model.direct_debit.payment_response import PaymentResponse
from doku_python_library.src.model.direct_debit.balance_inquiry_request import BalanceInquiryRequest
from doku_python_library.src.model.direct_debit.balance_inquiry_response import BalanceInquiryResponse
from doku_python_library.src.model.direct_debit.account_unbinding_request import AccountUnbindingRequest
from doku_python_library.src.model.direct_debit.account_unbinding_response import AccountUnbindingResponse
from doku_python_library.src.model.direct_debit.payment_jump_app_request import PaymentJumpAppRequest
from doku_python_library.src.model.direct_debit.paymet_jump_app_response import PaymentJumpAppResponse
from doku_python_library.src.model.direct_debit.card_registration_request import CardRegistrationRequest
from doku_python_library.src.model.direct_debit.card_registration_response import CardRegistrationResponse
from doku_python_library.src.model.direct_debit.refund_request import RefundRequest
from doku_python_library.src.model.direct_debit.refund_response import RefundResponse
from doku_python_library.src.model.direct_debit.check_status_request import CheckStatusRequest
from doku_python_library.src.model.direct_debit.check_status_response import CheckStatusResponse
from doku_python_library.src.model.direct_debit.card_unbinding_request import CardUnbindingRequest
from doku_python_library.src.model.direct_debit.card_unbinding_response import CardUnbindingResponse
from doku_python_library.src.model.notification.notification_payment_direct_debit_response import *

class DokuSNAP :

    def __init__(self, private_key: str, client_id: str, is_production: bool, public_key: str, issuer: str, secret_key: str, 
                 merchant_public_key: str) -> None:
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
        self.token_b2b2c: str
        self.token_b2b2c_generate_timestamp: str
        self.token_b2b2c_expires_in: int
        self.merchant_public_key = merchant_public_key

        
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
            return TokenB2BResponse(
                responseCode="5007300",
                responseMessage=str(e)
            )
    
    def _set_token_b2b(self, token_b2b_response: TokenB2BResponse) -> None:
        self.token_b2b = token_b2b_response
        self.token = token_b2b_response.access_token
        self.token_expires_in = token_b2b_response.expires_in
        self.token_generate_timestamp = token_b2b_response.generated_timestamp

    def create_va(self, create_va_request: CreateVARequest) -> CreateVAResponse:
        try:
            resp = create_va_request.check_simulator(is_production=self.is_production)
            if resp is not None:
                return resp
            create_va_request.validate_va_request()
            is_token_invalid: bool = TokenController.is_token_invalid(self.token, self.token_expires_in, self.token_generate_timestamp)
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
            return CreateVAResponse(
                responseCode="5002700",
                responseMessage=str(e)
            )
    
    def update_va(self, update_request: UpdateVaRequest) -> UpdateVAResponse:
        try:
            resp = update_request.check_simulator(is_production=self.is_production)
            if resp is not None:
                return resp
            update_request.validate_update_va_request()
            is_token_invalid: bool = TokenController.is_token_invalid(self.token, self.token_expires_in, self.token_generate_timestamp)
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
            return UpdateVAResponse(
                responseCode="5002800",
                responseMessage=str(e)
            )
            
    
    def check_status_va(self, check_status_request: va_status) -> CheckStatusVAResponse:
        try:
            resp = check_status_request.check_simulator(is_production=self.is_production)
            if resp is not None:
                return resp
            check_status_request.validate_check_status_request()
            is_token_invalid: bool = TokenController.is_token_invalid(self.token, self.token_expires_in, self.token_generate_timestamp)
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
            return CheckStatusVAResponse(
                responseCode="5002600",
                responseMessage=str(e)
            )
    
    def delete_payment_code(self, delete_va_request: DeleteVARequest) -> DeleteVAResponse:
        try:
            resp = delete_va_request.check_simulator(is_production=self.is_production)
            if resp is not None:
                return resp
            delete_va_request.validate_delete_request()
            is_token_invalid: bool = TokenController.is_token_invalid(self.token, self.token_expires_in, self.token_generate_timestamp)
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
            return DeleteVAResponse(
                responseCode="5003100",
                responseMessage=str(e)
            )
        
    def validate_signature(self) -> bool:
        return TokenController.validate_signature(
            client_id= self.client_id,
            public_key=self.public_key
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
        return TokenController.validate_token_b2b(token= request_token, public_key= self.merchant_public_key)
    
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
            token=self.token,
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
    
    def do_account_binding(self, request: AccountBindingRequest, device_id: str = None, ip_address: str = None) -> AccountBindingResponse:
        try:
            request.validate_request()

            is_token_invalid: bool = TokenController.is_token_invalid(
                token=self.token,
                token_expires_in=self.token_expires_in,
                token_generated_timestamp=self.token_generate_timestamp
            )

            if is_token_invalid:
                self.get_token()
            
            return DirectDebitController.do_account_binding(
                request=request,
                secret_key=self.secret_key,
                client_id=self.client_id,
                device_id=device_id,
                ip_address=ip_address,
                token_b2b=self.token,
                is_production=self.is_production
            )
        except Exception as e:
            return AccountBindingResponse(
                responseCode="500700",
                responseMessage=str(e)
            )
    
    def get_token_b2b2c(self, auth_code: str) -> TokenB2B2CResponse:
        try:
            token_b2b2c_response: TokenB2B2CResponse = TokenController.get_token_b2b2c(
                auth_code=auth_code,
                private_key=self.private_key,
                client_id=self.client_id,
                is_production=self.is_production
            )
            if token_b2b2c_response.response_code == "2007400":
                self._set_token_b2b2c(token_b2b2c_response=token_b2b2c_response)
            return token_b2b2c_response
        except Exception as e:
            return TokenB2B2CResponse(
                responseCode="5007400",
                responseMessage=str(e)
            )
    
    def _set_token_b2b2c(self, token_b2b2c_response: TokenB2B2CResponse) -> None:
        self.token_b2b2c = token_b2b2c_response.access_token
        self.token_b2b2c_expires_in = token_b2b2c_response.access_token_expiry_time
        self.token_b2b2c_generate_timestamp = token_b2b2c_response.generated_timestamp
    
    def do_payment(self, request: PaymentRequest, ip_address: str, auth_code: str) -> PaymentResponse:
        try:
            request.validate_request()
            is_token_invalid: bool = TokenController.is_token_invalid(self.token, self.token_expires_in, self.token_generate_timestamp)
            if is_token_invalid:
                self.get_token()
            is_token_b2b2c_invalid: bool = TokenController.is_token_invalid(self.token_b2b2c, self.token_b2b2c_expires_in, self.token_b2b2c_generate_timestamp)
            if is_token_b2b2c_invalid:
                self.get_token_b2b2c(auth_code=auth_code)
            return DirectDebitController.do_payment_process(
                request=request,
                secret_key=self.secret_key,
                client_id=self.client_id,
                ip_address=ip_address,
                token_b2b=self.token,
                token_b2b2c=self.token_b2b2c,
                is_production=self.is_production
            )
        except Exception as e:
            return PaymentResponse(
                responseCode="5005400",
                responseMessage=str(e)
            )
    
    def do_balance_inquiry(self, request: BalanceInquiryRequest, ip_address: str, auth_code: str) -> BalanceInquiryResponse:
        try:
            request.validate_request()
            is_token_invalid: bool = TokenController.is_token_invalid(self.token, self.token_expires_in, self.token_generate_timestamp)
            if is_token_invalid:
                self.get_token()
            is_token_b2b2c_invalid: bool = TokenController.is_token_invalid(self.token_b2b2c, self.token_b2b2c_expires_in, self.token_b2b2c_generate_timestamp)
            if is_token_b2b2c_invalid:
                self.get_token_b2b2c(auth_code=auth_code)
            return DirectDebitController.do_balance_inquiry(
                request=request,
                ip_address=ip_address,
                token=self.token,
                token_b2b2c=self.token_b2b2c,
                secret_key=self.secret_key,
                client_id=self.client_id,
                is_production=self.is_production
            )
        except Exception as e:
            return BalanceInquiryResponse(
                responseCode="5001100",
                responseMessage=str(e)
            )
    
    def do_account_unbinding(self, request: AccountUnbindingRequest, ip_address: str) -> AccountUnbindingResponse:
        try:
            request.validate_request()
            is_token_invalid: bool = TokenController.is_token_invalid(
                token=self.token,
                token_expires_in=self.token_expires_in,
                token_generated_timestamp=self.token_generate_timestamp
            )

            if is_token_invalid:
                self.get_token()
            return DirectDebitController.do_account_unbinding(
                request=request,
                secret_key=self.secret_key,
                client_id=self.client_id,
                ip_address=ip_address,
                token=self.token,
                is_production=self.is_production
            )
        except Exception as e:
            return AccountUnbindingResponse(
                responseCode="500500",
                responseMessage=str(e)
            )
    
    def do_payment_jump_app(self, request: PaymentJumpAppRequest, device_id: str, ip_address: str) -> PaymentJumpAppResponse:
        try:
            request.validate_request()
            is_token_invalid: bool = TokenController.is_token_invalid(
                token=self.token,
                token_expires_in=self.token_expires_in,
                token_generated_timestamp=self.token_generate_timestamp
            )

            if is_token_invalid:
                self.get_token()
            return DirectDebitController.do_payment_jump_app(
                request=request,
                client_id=self.client_id,
                token_b2b=self.token,
                secret_key=self.secret_key,
                device_id=device_id,
                ip_address=ip_address,
                is_production=self.is_production
            )
        except Exception as e:
            return PaymentJumpAppResponse(
                responseCode="500500",
                responseMessage=str(e)
            )
        
    def do_card_registration(self, request: CardRegistrationRequest, channel_id: str) -> CardRegistrationResponse:
        try:
            request.validate_request()
            is_token_invalid: bool = TokenController.is_token_invalid(
                token=self.token,
                token_expires_in=self.token_expires_in,
                token_generated_timestamp=self.token_generate_timestamp
            )

            if is_token_invalid:
                self.get_token()
            return DirectDebitController.do_card_registration(
                request=request,
                secret_key=self.secret_key,
                client_id=self.client_id,
                channel_id=channel_id,
                token_b2b=self.token,
                is_production=self.is_production
            )
        except Exception as e:
            return CardRegistrationResponse(
                responseCode="500700",
                responseMessage=str(e)
            )
    
    def do_card_unbinding(self, request: CardUnbindingRequest, ip_address: str) -> CardUnbindingResponse:
        try:
            request.validate_request()
            is_token_invalid: bool = TokenController.is_token_invalid(
                token=self.token,
                token_expires_in=self.token_expires_in,
                token_generated_timestamp=self.token_generate_timestamp
            )

            if is_token_invalid:
                self.get_token()
            return DirectDebitController.do_card_unbinding(
                request=request,
                secret_key=self.secret_key,
                client_id=self.client_id,
                ip_address=ip_address,
                token=self.token,
                is_production=self.is_production
            )
        except Exception as e:
            return CardUnbindingResponse(
                responseCode="500500",
                responseMessage=str(e)
            )
    
    def do_refund(self, request: RefundRequest, ip_address: str, auth_code: str, device_id: str) -> RefundResponse:
        try:
            request.validate_request()
            is_token_invalid: bool = TokenController.is_token_invalid(self.token, self.token_expires_in, self.token_generate_timestamp)
            if is_token_invalid:
                self.get_token()
            is_token_b2b2c_invalid: bool = TokenController.is_token_invalid(self.token_b2b2c, self.token_b2b2c_expires_in, self.token_b2b2c_generate_timestamp)
            if is_token_b2b2c_invalid:
                self.get_token_b2b2c(auth_code=auth_code)
            return DirectDebitController.do_refund(
                request=request,
                secret_key=self.secret_key,
                client_id=self.client_id,
                ip_address=ip_address,
                token_b2b=self.token,
                token_b2b2c=self.token_b2b2c,
                is_production=self.is_production,
                device_id=device_id
            )
        except Exception as e:
            return RefundResponse(
                responseCode="500700",
                responseMessage=str(e)
            )
        
    def do_check_status(self, request: CheckStatusRequest) -> CheckStatusResponse:
        try:
            request.validate_request()
            is_token_invalid: bool = TokenController.is_token_invalid(
                token=self.token,
                token_expires_in=self.token_expires_in,
                token_generated_timestamp=self.token_generate_timestamp
            )

            if is_token_invalid:
                self.get_token()
            return DirectDebitController.do_check_status(
                request=request,
                secret_key=self.secret_key,
                client_id=self.client_id,
                token_b2b=self.token,
                is_production=self.is_production
            )
        except Exception as e:
            return CheckStatusResponse(
                responseCode="5005500",
                responseMessage=str(e)
            )
    
    def direct_debit_payment_notification(self, request_token_b2b2c: str) -> NotificationPaymentDirectDebitResponse:
        is_token_b2b2c_valid: bool = self.validate_token_b2b(request_token=request_token_b2b2c)
        return self.generate_direct_debit_notification(is_token_b2b2c_valid=is_token_b2b2c_valid)

    def generate_direct_debit_notification(self, is_token_b2b2c_valid: bool) -> NotificationPaymentDirectDebitResponse:
        if is_token_b2b2c_valid:
            return NotificationController.generate_direct_debit_notification_response()
        return NotificationController.generate_direct_debit_invalid_token_response()
    
    @staticmethod
    def encrypt_card(input_str: str, secret_key: str) -> str:
        return DirectDebitController.encrypt_card(input_str, secret_key)