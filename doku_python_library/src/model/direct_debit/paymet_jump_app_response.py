from doku_python_library.src.model.direct_debit.payment_jump_app_additional_info_response import PaymentJumpAppAdditionalInfoResponse

class PaymentJumpAppResponse:

    def __init__(self, responseCode: str, responseMessage: str, webRedirectUrl: str = None, 
                 partnerReferenceNo: str = None, referenceNo: str = None, additionalInfo: PaymentJumpAppAdditionalInfoResponse = None) -> None:
        self.response_code = responseCode
        self.response_message = responseMessage
        self.web_redirect_url = webRedirectUrl
        self.partner_reference_no = partnerReferenceNo
        self.reference_no = referenceNo
        self.additional_info = additionalInfo
    
    def json(self) -> dict:
        response = {
            "responseCode": self.response_code,
            "responseMessage": self.response_message,
            "webRedirectUrl": self.web_redirect_url,
            "partnerReferenceNo": self.partner_reference_no,
            "referenceNo": self.reference_no,
            "additionalInfo": self.additional_info if self.additional_info is not None else None
        }
        if self.web_redirect_url is not None:
            response["webRedirectUrl"] = self.web_redirect_url
        if self.partner_reference_no is not None:
            response["partnerReferenceNo"] = self.partner_reference_no
        if self.reference_no is not None:
            response["referenceNo"] = self.reference_no
        if self.additional_info is not None:
            response["additionalInfo"] = self.additional_info
        return response