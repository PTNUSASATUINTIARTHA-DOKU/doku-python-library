
class PaymentResponse:

    def __init__(self, responseCode: str, responseMessage: str, webRedirectUrl: str = None, partnerReferenceNo: str = None, referenceNo: str = None) -> None:
        self.response_code = responseCode
        self.response_message = responseMessage
        self.web_redirect_url = webRedirectUrl
        self.partner_reference_no = partnerReferenceNo
        self.reference_no = referenceNo
    
    def json(self) -> dict:
        response = {
            "responseCode": self.response_code,
            "responseMessage": self.response_message,
        }
        if self.web_redirect_url is not None:
            response["webRedirectUrl"] = self.web_redirect_url
        if self.partner_reference_no is not None:
            response["partnerReferenceNo"] = self.partner_reference_no
        if self.reference_no is not None:
            response["referenceNo"] = self.reference_no
        return response