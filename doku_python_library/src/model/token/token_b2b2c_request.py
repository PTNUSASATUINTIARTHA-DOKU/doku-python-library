
class TokenB2B2CRequest:

    def __init__(self, grant_type: str, auth_code: str, refresh_token: str, additional_info: any = None) -> None:
        self. grant_type = grant_type
        self.auth_code = auth_code
        self.refresh_token = refresh_token
        self.additional_info = additional_info

    def create_request_body(self) -> dict:
        return {
            "grantType": self.grant_type,
            "authCode": self.auth_code,
            "refreshToken": self.refresh_token,
            "additionalInfo": self.additional_info
        }