from doku_python_library.src.model.direct_debit.account_binding_request import AccountBindingRequest
from doku_python_library.src.model.direct_debit.account_binding_response import AccountBindingResponse
from doku_python_library.src.services.token_service import TokenService
from doku_python_library.src.commons.config import Config
from doku_python_library.src.commons.snap_utils import SnapUtils
from doku_python_library.src.model.general.request_header import RequestHeader
from doku_python_library.src.services.direct_debit_service import DirectDebitService
from doku_python_library.src.model.direct_debit.payment_request import PaymentRequest
from doku_python_library.src.model.direct_debit.payment_response import PaymentResponse
from doku_python_library.src.model.direct_debit.balance_inquiry_request import BalanceInquiryRequest
from doku_python_library.src.model.direct_debit.balance_inquiry_response import BalanceInquiryResponse
from doku_python_library.src.model.direct_debit.account_unbinding_request import AccountUnbindingRequest
from doku_python_library.src.model.direct_debit.account_unbinding_response import AccountUnbindingResponse


class DirectDebitController:

    @staticmethod
    def do_account_binding(request: AccountBindingRequest, secret_key: str,
                           client_id: str, device_id: str, ip_address: str, token_b2b: str,
                           is_production: bool) -> AccountBindingResponse:
        timestamp: str = TokenService.get_timestamp()
        endpoint: str = Config.DIRECT_DEBIT_ACCOUNT_BINDING_URL
        method: str = "POST"
        signature: str = TokenService.generate_symmetric_signature(
            http_method=method,
            endpoint=endpoint,
            token_b2b=token_b2b,
            request=request.json(),
            timestamp=timestamp,
            secret_key=secret_key
        )
        external_id: str = SnapUtils.generate_external_id()
        request_header: RequestHeader = SnapUtils.generate_request_header(
            channel_id="SDK",
            client_id=client_id,
            token_b2b=token_b2b,
            timestamp=timestamp,
            external_id=external_id,
            signature=signature,
            device_id=device_id,
            ip_address=ip_address
        )

        return DirectDebitService.do_account_binding_process(request_header=request_header, request=request, is_production=is_production)
    
    @staticmethod
    def do_payment_process(request: PaymentRequest, secret_key: str, client_id: str, 
                           ip_address: str, token_b2b: str, token_b2b2c: str, is_production: bool) -> PaymentResponse:
        timestamp: str = TokenService.get_timestamp()
        endpoint: str = Config.DIRECT_DEBIT_PAYMENT_URL
        method: str = "POST"
        signature: str = TokenService.generate_symmetric_signature(
            http_method=method,
            endpoint=endpoint,
            token_b2b=token_b2b,
            request=request.create_request_body(),
            timestamp=timestamp,
            secret_key=secret_key
        )
        external_id: str = SnapUtils.generate_external_id()
        request_header: RequestHeader = SnapUtils.generate_request_header(
            channel_id="SDK",
            client_id=client_id,
            token_b2b=token_b2b,
            timestamp=timestamp,
            external_id=external_id,
            signature=signature,
            ip_address=ip_address,
            token_b2b2c=token_b2b2c
        )
        return DirectDebitService.do_payment_process(request_header=request_header, request=request, is_production=is_production)
    
    @staticmethod
    def do_balance_inquiry(request: BalanceInquiryRequest, ip_address: str, token: str, token_b2b2c: str, secret_key: str, client_id: str, is_production: bool) -> BalanceInquiryResponse:
        timestamp: str = TokenService.get_timestamp()
        endpoint: str = Config.DIRECT_DEBIT_BALANCE_INQUIRY_URL
        method: str = "POST"
        signature: str = TokenService.generate_symmetric_signature(
            http_method=method,
            endpoint=endpoint,
            token_b2b=token,
            request=request.create_body_request(),
            timestamp=timestamp,
            secret_key=secret_key
        )
        external_id: str = SnapUtils.generate_external_id()
        request_header: RequestHeader = SnapUtils.generate_request_header(
            channel_id="SDK",
            client_id=client_id,
            token_b2b=token,
            external_id=external_id,
            timestamp=timestamp,
            signature=signature,
            ip_address=ip_address,
            token_b2b2c=token_b2b2c
        )
        
        return DirectDebitService.do_balance_inquiry(request_header=request_header, request=request, is_production=is_production)
    
    @staticmethod
    def do_account_unbinding(request: AccountUnbindingRequest, secret_key: str, client_id: str,
                             ip_address: str, token: str, is_production: bool) -> AccountUnbindingResponse:
        timestamp: str = TokenService.get_timestamp()
        endpoint: str = Config.DIRECT_DEBIT_ACCOUNT_UNBINDING_URL
        method: str = "POST"
        signature: str = TokenService.generate_symmetric_signature(
            http_method=method,
            endpoint=endpoint,
            token_b2b=token,
            request=request.create_body_request(),
            timestamp=timestamp,
            secret_key=secret_key
        )
        external_id: str = SnapUtils.generate_external_id()
        request_header: RequestHeader = SnapUtils.generate_request_header(
            channel_id="SDK",
            client_id=client_id,
            token_b2b=token,
            timestamp=timestamp,
            external_id=external_id,
            signature=signature,
            ip_address=ip_address
        )
        return DirectDebitService.do_account_unbinding_process(request_header=request_header, request=request, is_production=is_production)