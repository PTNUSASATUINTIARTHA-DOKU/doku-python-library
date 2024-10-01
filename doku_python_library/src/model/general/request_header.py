class RequestHeader:

    def __init__(self, x_timestamp: str, x_signature: str, x_partner_id: str, x_external_id: str,
                  authorization: str, device_id: str = None, ip_address: str = None, channel_id: str="SDK", token_b2b2c: str = None):
        self.x_timestamp = x_timestamp
        self.x_signature = x_signature
        self.x_partner_id = x_partner_id
        self.x_external_id = x_external_id
        self.channel_id = channel_id
        self.authorization = authorization
        self.device_id = device_id
        self.ip_address = ip_address
        self.token_b2b2c = token_b2b2c
    
    def to_json(self) -> dict:
        headers: dict = {
            "X-TIMESTAMP": self.x_timestamp,
            "X-SIGNATURE": self.x_signature,
            "X-PARTNER-ID": self.x_partner_id,
            "X-EXTERNAL-ID": self.x_external_id,
            "CHANNEL-ID": self.channel_id,
            "Authorization": "Bearer "+str(self.authorization)
        }
        if self.device_id is not None:
            headers["X-DEVICE-ID"] = self.device_id
        if self.ip_address is not None:
            headers["X-IP-ADDRESS"] = self.ip_address
        if self.token_b2b2c is not None:
            headers["Authorization-Customer"] = self.token_b2b2c
        return headers
    
    def validate_device_id(self):
        if self.device_id is not None:
            if len(self.device_id) > 64:
                raise Exception("X-DEVICE-ID must be 64 characters or fewer. Ensure that X-DEVICE-ID is no longer than 64 characters.")
        else:
            raise Exception("X-DEVICE-ID must be 64 characters or fewer. Ensure that X-DEVICE-ID is no longer than 64 characters.")

    def validate_ip_address(self):
        if self.ip_address is not None:
            if len(self.ip_address) < 10 or len(self.ip_address) > 15:
                raise Exception("X-IP-ADDRESS must be in 10 to 15 characters.")
        else:
            raise Exception("X-IP-ADDRESS must be in 10 to 15 characters.")
        
    def validate_account_binding_header(self, channel: str):
        if channel == "DIRECT_DEBIT_ALLO_SNAP":
            self.validate_ip_address()
            self.validate_device_id()
    
    def validate_payment_header(self, channel: str):
        if channel == "DIRECT_DEBIT_ALLO_SNAP":
            self.validate_ip_address()
        elif channel == "EMONEY_DANA_SNAP":
            self.validate_device_id()
            self.validate_ip_address()
        elif channel == "EMONEY_SHOPEE_PAY_SNAP":
            self.validate_device_id()
            self.validate_ip_address()
    
    def validate_balance_inquiry_header(self, channel: str):
        if channel == "DIRECT_DEBIT_ALLO_SNAP":
            self.validate_ip_address()
    
    def validate_account_unbinding_header(self, channel: str):
        if channel == "DIRECT_DEBIT_ALLO_SNAP":
            self.validate_ip_address()
    
    def validate_refund_header(self, channel: str):
        if channel == "DIRECT_DEBIT_ALLO_SNAP":
            self.validate_ip_address()
        elif channel == "EMONEY_DANA_SNAP":
            self.validate_device_id()
            self.validate_ip_address()
        elif channel == "EMONEY_SHOPEE_PAY_SNAP":
            self.validate_device_id()
            self.validate_ip_address()