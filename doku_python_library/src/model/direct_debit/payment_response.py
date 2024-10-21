
class PaymentResponse:

    def __init__(self, responseCode: str, responseMessage: str, webRedirectUrl: str = None, partnerReferenceNo: str = None, referenceNo: str = None) -> None:
        self.response_code = responseCode
        self.response_message = responseMessage
        self.web_redirect_url = webRedirectUrl
        self.partner_reference_no = partnerReferenceNo
        self.reference_no = referenceNo
    
    def json(self) -> dict:
        return {
            "responseCode": self.response_code,
            "responseMessage": self.response_message,
            "webRedirectUrl": self.web_redirect_url,
            "partnerReferenceNo": self.partner_reference_no,
            "referenceNo": self.reference_no
        }