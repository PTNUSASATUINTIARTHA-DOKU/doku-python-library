
class PaymentResponse:

    def __init__(self, responseCode: str, responseMessage: str, webRedirectUrl: str = None, partnerReferenceNo: str = None) -> None:
        self.response_code = responseCode
        self.response_message = responseMessage
        self.web_redirect_url = webRedirectUrl
        self.partner_reference_no = partnerReferenceNo