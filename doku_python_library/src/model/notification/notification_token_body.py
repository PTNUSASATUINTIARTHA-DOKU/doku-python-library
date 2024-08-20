class NotificationTokenBody:

    def __init__(self, responseCode: str, responseMessage: str, accessToken: str, 
                 tokenType: str, expiresIn: int, additionalInfo: str) -> None:
        self.response_code = responseCode
        self.response_message = responseMessage
        self.access_token = accessToken
        self.token_type = tokenType
        self.expires_in = expiresIn
        self.additionalInfo= additionalInfo
    
    def json(self) -> dict:
        return {
            "responseCode": self.response_code,
            "responseMessage": self.response_message,
            "accessToken": self.access_token,
            "tokenType": self.token_type,
            "expiresIn": self.expires_in,
            "additionalInfo": self.additionalInfo
        }