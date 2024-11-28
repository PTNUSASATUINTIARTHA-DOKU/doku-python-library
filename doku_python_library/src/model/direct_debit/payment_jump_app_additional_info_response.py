class PaymentJumpAppAdditionalInfoResponse:
    
    def __init__(self, webRedirectUrl: str = None):
        self.web_redirect_url = webRedirectUrl
    
    def json(self) -> dict:
        return {
            "webRedirectUrl": self.web_redirect_url
        }