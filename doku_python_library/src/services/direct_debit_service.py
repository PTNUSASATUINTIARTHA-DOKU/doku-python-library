from doku_python_library.src.model.general.request_header import RequestHeader
from doku_python_library.src.model.direct_debit.account_binding_request import AccountBindingRequest
from doku_python_library.src.model.direct_debit.account_binding_response import AccountBindingResponse
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
from doku_python_library.src.model.direct_debit.card_unbinding_request import CardUnbindingRequest
from doku_python_library.src.model.direct_debit.card_unbinding_response import CardUnbindingResponse
from doku_python_library.src.model.direct_debit.refund_request import RefundRequest
from doku_python_library.src.model.direct_debit.refund_response import RefundResponse
from doku_python_library.src.model.direct_debit.check_status_request import CheckStatusRequest
from doku_python_library.src.model.direct_debit.check_status_response import CheckStatusResponse
from doku_python_library.src.commons.config import Config
import requests

class DirectDebitService:

    @staticmethod
    def do_account_binding_process(request_header: RequestHeader, request: AccountBindingRequest, is_production: bool) -> AccountBindingResponse:
        try:
            url: str = Config.get_base_url(is_production=is_production) + Config.DIRECT_DEBIT_ACCOUNT_BINDING_URL
            request_header.validate_account_binding_header(request.additional_info.channel)
            headers: dict = request_header.to_json()
            response = requests.post(url=url, json=request.json(), headers=headers)
            response_json = response.json()
            account_binding_response: AccountBindingResponse = AccountBindingResponse(**response_json)
            return account_binding_response
        except Exception as e:
            print("Failed Parse Response "+str(e))
    
    @staticmethod
    def do_payment_process(request_header: RequestHeader, request: PaymentRequest, is_production: bool) -> PaymentResponse:
        try:
            url: str = Config.get_base_url(is_production=is_production) + Config.DIRECT_DEBIT_PAYMENT_URL
            request_header.validate_payment_header(request.additional_info.channel)
            headers: dict = request_header.to_json()
            response = requests.post(url=url, json=request.create_request_body(), headers=headers)
            response_json = response.json()
            payment_response: PaymentResponse = PaymentResponse(**response_json)
            return payment_response
        except Exception as e:
            print("Failed Parse Response "+ str(e))
    
    @staticmethod
    def do_balance_inquiry(request_header: RequestHeader, request: BalanceInquiryRequest, is_production: bool) -> BalanceInquiryRequest:
        try:
            url: str = Config.get_base_url(is_production=is_production) + Config.DIRECT_DEBIT_BALANCE_INQUIRY_URL
            request_header.validate_balance_inquiry_header(channel=request.additional_info.channel)
            headers: dict = request_header.to_json()
            response = requests.post(url=url, json=request.create_request_body(), headers=headers)
            response_json = response.json()
            balance_response: BalanceInquiryResponse = BalanceInquiryResponse(**response_json)
            return balance_response
        except Exception as e:
            print("Failed Parse Response "+ str(e))
    
    @staticmethod
    def do_account_unbinding_process(request_header: RequestHeader, request: AccountUnbindingRequest, is_production: bool) -> AccountUnbindingResponse:
        try:
            url: str = Config.get_base_url(is_production=is_production) + Config.DIRECT_DEBIT_ACCOUNT_UNBINDING_URL
            request_header.validate_account_unbinding_header(channel=request.additional_info.channel)
            headers: dict = request_header.to_json()
            response = requests.post(url=url, json=request.create_request_body(), headers=headers)
            response_json = response.json()
            unbinding_response: AccountUnbindingResponse = AccountUnbindingResponse(**response_json)
            return unbinding_response
        except Exception as e:
            print("Failed Parse Response "+ str(e))

    
    @staticmethod
    def do_payment_jump_app_process(request_header: RequestHeader, request: PaymentJumpAppRequest, is_production: bool) -> PaymentJumpAppResponse:
        try:
            url: str = Config.get_base_url(is_production=is_production) + Config.DIRECT_DEBIT_PAYMENT_URL
            headers: dict = request_header.to_json()
            response = requests.post(url=url, json=request.create_request_body(), headers=headers)
            response_json = response.json()
            payment_response: PaymentJumpAppResponse = PaymentJumpAppResponse(**response_json)
            return payment_response
        except Exception as e:
            print("Failed Parse Response "+ str(e))
    
    @staticmethod
    def do_card_registration_process(request_header: RequestHeader, request: CardRegistrationRequest, is_production: bool) -> CardRegistrationResponse:
        try:
            url: str = Config.get_base_url(is_production=is_production) + Config.DIRECT_DEBIT_CARD_REGISTRATION
            headers: dict = request_header.to_json()
            response = requests.post(url=url, json=request.create_request_body(), headers=headers)
            response_json = response.json()
            card_registration_response: CardRegistrationResponse = CardRegistrationResponse(**response_json)
            return card_registration_response
        except Exception as e:
            print("Failed Parse Response "+ str(e))
    
    @staticmethod
    def do_refund_process(request_header: RequestHeader, request: RefundRequest, is_production: bool) -> RefundResponse:
        try:
            url: str = Config.get_base_url(is_production=is_production) + Config.DIRECT_DEBIT_REFUND
            request_header.validate_refund_header(channel=request.additional_info.channel)
            headers: dict = request_header.to_json()
            response = requests.post(url=url, json=request.create_request_body(), headers=headers)
            response_json = response.json()
            refund_response: RefundResponse = RefundResponse(**response_json)
            return refund_response
        except Exception as e:
            print("Failed Parse Response "+ str(e))
    
    @staticmethod
    def do_check_status(request_header: RequestHeader, request: CheckStatusRequest, is_production: bool) -> CheckStatusResponse:
        try:
            url: str = Config.get_base_url(is_production=is_production) + Config.DIRECT_DEBIT_CHECK_STATUS
            headers: dict = request_header.to_json()
            response = requests.post(url=url, json=request.create_request_body(), headers=headers)
            response_json = response.json()
            status_response: CheckStatusResponse = CheckStatusResponse(**response_json)
            return status_response
        except Exception as e:
            print("Failed Parse Response "+ str(e))
    
    @staticmethod
    def do_card_unbinding_process(request_header: RequestHeader, request: CardUnbindingRequest, is_production: bool) -> CardUnbindingResponse:
        try:
            url: str = Config.get_base_url(is_production=is_production) + Config.DIRECT_DEBIT_ACCOUNT_UNBINDING_URL
            headers: dict = request_header.to_json()
            response = requests.post(url=url, json=request.create_request_body(), headers=headers)
            response_json = response.json()
            unbinding_response: CardUnbindingResponse = CardUnbindingResponse(**response_json)
            return unbinding_response
        except Exception as e:
            print("Failed Parse Response "+ str(e))