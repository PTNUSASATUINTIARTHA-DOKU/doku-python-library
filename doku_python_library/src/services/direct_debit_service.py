from doku_python_library.src.model.general.request_header import RequestHeader
from doku_python_library.src.model.direct_debit.account_binding_request import AccountBindingRequest
from doku_python_library.src.model.direct_debit.account_binding_response import AccountBindingResponse
from doku_python_library.src.model.direct_debit.payment_request import PaymentRequest
from doku_python_library.src.model.direct_debit.payment_response import PaymentResponse
from doku_python_library.src.model.direct_debit.balance_inquiry_request import BalanceInquiryRequest
from doku_python_library.src.model.direct_debit.balance_inquiry_response import BalanceInquiryResponse
from doku_python_library.src.model.direct_debit.account_unbinding_request import AccountUnbindingRequest
from doku_python_library.src.model.direct_debit.account_unbinding_response import AccountUnbindingResponse
from doku_python_library.src.commons.config import Config
import requests

class DirectDebitService:

    @staticmethod
    def do_account_binding_process(request_header: RequestHeader, request: AccountBindingRequest, is_production: bool) -> AccountBindingResponse:
        try:
            url: str = Config.get_base_url(is_production=is_production) + Config.DIRECT_DEBIT_ACCOUNT_BINDING_URL
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
            headers: dict = request_header.to_json()
            response = requests.post(url=url, json=request.create_body_request(), headers=headers)
            response_json = response.json()
            balance_response: BalanceInquiryResponse = BalanceInquiryResponse(**response_json)
            return balance_response
        except Exception as e:
            print("Failed Parse Response "+ str(e))
    
    @staticmethod
    def do_account_unbinding_process(request_header: RequestHeader, request: AccountUnbindingRequest, is_production: bool) -> AccountUnbindingResponse:
        try:
            url: str = Config.get_base_url(is_production=is_production) + Config.DIRECT_DEBIT_ACCOUNT_UNBINDING_URL
            headers: dict = request_header.to_json()
            response = requests.post(url=url, json=request.create_request_body(), headers=headers)
            response_json = response.json()
            unbinding_response: AccountUnbindingResponse = AccountUnbindingResponse(**response_json)
            return unbinding_response
        except Exception as e:
            print("Failed Parse Response "+ str(e))