from doku_python_library.src.model.direct_debit.account_binding_request import AccountBindingRequest, AccountBindingAdditionalInfoRequest
from doku_python_library.src.model.direct_debit.account_binding_response import AccountBindingResponse


class Util:

    @staticmethod
    def generate_account_binding_request() -> AccountBindingRequest:
        return AccountBindingRequest(
        phone_no="62813941306101",
        additional_info=AccountBindingAdditionalInfoRequest(
            channel="DIRECT_DEBIT_CIMB_SNAP",
            cust_id_merchant="sdjkava4",
            success_registration_url="https://sandbox.doku.com/bo/login/",
            failed_registration_url="https://www.seleniumeasy.com/test",
        )
    )

    @staticmethod
    def generate_account_binding_response(response_code: str) -> AccountBindingResponse:
        return AccountBindingResponse(
            responseCode= response_code,
            responseMessage="Successful"
        )