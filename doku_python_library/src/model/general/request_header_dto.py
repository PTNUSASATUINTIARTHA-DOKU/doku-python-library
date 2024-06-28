class RequestHeaderDto:

    def __init__(self, x_timestamp: str, x_signature: str, x_partner_id: str, x_external_id: str, channel_id: str, authorization: str):
        self.x_timestamp = x_timestamp
        self.x_signature = x_signature
        self.x_partner_id = x_partner_id
        self.x_external_id = x_external_id
        self.channel_id = channel_id
        self.authorization = authorization