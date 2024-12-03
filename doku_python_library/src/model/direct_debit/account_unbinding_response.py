
class AccountUnbindingResponse:

    def __init__(self, responseCode: str, responseMessage: str, referenceNo: str = None, additionalInfo = None) -> None:
        self.response_code = responseCode
        self.response_message = responseMessage
        self.reference_no = referenceNo
    
    def json(self) -> dict:
        response = {
            "responseCode": self.response_code,
            "responseMessage": self.response_message,
        }
        if self.reference_no is not None:
            response["referenceNo"] = self.reference_no
        return response