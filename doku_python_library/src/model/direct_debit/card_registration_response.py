from doku_python_library.src.model.direct_debit.account_binding_additional_info_response import AccountBindingAdditionalInfoResponse


class CardRegistrationResponse:

    def __init__(self, responseCode: str, responseMessage: str, additionalInfo: AccountBindingAdditionalInfoResponse = None, 
                 referenceNo: str = None, redirectUrl: str = None) -> None:
        self.response_code = responseCode
        self.response_message = responseMessage
        self.additional_info = additionalInfo
        self.reference_no = referenceNo
        self.redirect_url = redirectUrl