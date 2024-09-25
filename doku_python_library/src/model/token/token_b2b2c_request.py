
class TokenB2B2CRequest:

    def __init__(self, grant_type: str, auth_code: str) -> None:
        self. grant_type = grant_type
        self.auth_code = auth_code

    def create_request_body(self) -> dict:
        return {
            "grantType": self.grant_type,
            "authCode": self.auth_code,
        }