
class CardUnbindingResponse:

    def __init__(self, responseCode: str, responseMessage: str, referenceNo: str = None, redirectUrl: str = None) -> None:
        self.response_code = responseCode
        self.response_message = responseMessage
        self.reference_no = referenceNo
        self.redirect_url = redirectUrl
    
    def json(self) -> dict:
        return {
            "responseCode": self.response_code,
            "responseMessage": self.response_message,
            "referenceNo": self.reference_no,
            "redirectUrl": self.redirect_url
        }