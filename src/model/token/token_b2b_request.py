class TokenB2BRequest:

    def __init__(self, signature: str, 
                 timestamp: str, 
                 client_id: str, 
                 grant_type="client_credentials", 
                 additional_info="") -> None:
        self.signature = signature
        self.timestamp = timestamp
        self.client_id = client_id
        self.grant_type = grant_type
        self.additional_info = additional_info
    
    def create_request_body(self) -> dict:
        return {
            "grantType": self.grant_type,
            "additionalInfo": self.additional_info 
        }