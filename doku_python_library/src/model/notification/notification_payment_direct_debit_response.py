
class NotificationPaymentDirectDebitResponse:

    def __init__(self, responseCode: str, responseMessage: str, approvalCode: str = None) -> None:
        self.response_code = responseCode
        self.response_message = responseMessage
        self.approval_code = approvalCode
    
    def json(self) -> dict:
        return {
            "responseCode": self.response_code,
            "responseMessage": self.response_message,
            "approvalCode": self.approval_code if self.approval_code is not None else None
        }