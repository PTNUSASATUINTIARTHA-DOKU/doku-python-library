class UpdateVAConfig:

    def __init__(self, status: str = None, min_amount: str = None, max_amount: str = None):
        self.status = status
        self.min_amount = min_amount
        self.max_amount = max_amount
    
    def create_request_body(self) -> dict:
        param: dict = {}
        if self.status is not None:
            param["status"] = self.status
        if self.min_amount is not None:
            param["minAmount"] = self.min_amount
        if self.max_amount is not None:
            param["maxAmount"] = self.max_amount
        return param