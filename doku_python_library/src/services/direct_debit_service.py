from doku_python_library.src.model.general.request_header import RequestHeader
from doku_python_library.src.model.direct_debit.account_binding_request import AccountBindingRequest
from doku_python_library.src.model.direct_debit.account_binding_response import AccountBindingResponse
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