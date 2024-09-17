
class TokenB2B2CResponse:

    def __init__(self, responseCode: str, responseMessage: str, accessToken: str = None, tokenType: str = None,
                 accessTokenExpiryTime: str = None, refreshToken: str = None, refreshTokenExpiryTime: str = None,
                 additionalInfo: any = None) -> None:
        self.response_code = responseCode
        self.response_message = responseMessage
        self.access_token = accessToken
        self.token_type = tokenType
        self.access_token_expiry_time = accessTokenExpiryTime
        self.refresh_token = refreshToken
        self.refresh_token_expiry_time = refreshTokenExpiryTime
        self.additional_info = additionalInfo
        self.generated_timestamp = ''

    def json(self) -> dict:
        return {
            "responseCode": self.response_code,
            "responseMessage": self.response_message,
            "accessToken": self.access_token,
            "tokenType": self.token_type,
            "accessTokenExpiryTime": self.access_token_expiry_time,
            "refreshToken": self.refresh_token,
            "refreshTokenExpiryTime": self.refresh_token_expiry_time,
            "additionalInfo": self.additional_info
        }