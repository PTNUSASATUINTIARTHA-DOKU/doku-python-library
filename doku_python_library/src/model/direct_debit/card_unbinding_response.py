
class CardUnbindingResponse:

    def __init__(self, responseCode: str, responseMessage: str, referenceNo: str = None, redirectUrl: str = None) -> None:
        self.response_code = responseCode
        self.response_message = responseMessage
        self.reference_no = referenceNo
        self.redirect_url = redirectUrl
    
    def json(self) -> dict:
        response = {
            "responseCode": self.response_code,
            "responseMessage": self.response_message,
        }
        if self.reference_no is not None:
            response["referenceNo"] = self.reference_no
        if self.redirect_url is not None:
            response["redirectUrl"] = self.redirect_url
        return response