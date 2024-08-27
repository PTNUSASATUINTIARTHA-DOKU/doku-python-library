class RequestHeader:

    def __init__(self, x_timestamp: str, x_signature: str, x_partner_id: str, x_external_id: str, authorization: str, channel_id: str="SDK"):
        self.x_timestamp = x_timestamp
        self.x_signature = x_signature
        self.x_partner_id = x_partner_id
        self.x_external_id = x_external_id
        self.channel_id = channel_id
        self.authorization = authorization
    
    def to_json(self) -> dict:
        headers: dict = {
            "X-TIMESTAMP": self.x_timestamp,
            "X-SIGNATURE": self.x_signature,
            "X-PARTNER-ID": self.x_partner_id,
            "X-EXTERNAL-ID": self.x_external_id,
            "CHANNEL-ID": self.channel_id,
            "Authorization": self.authorization
        }
        return headers