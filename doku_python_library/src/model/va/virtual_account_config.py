class VirtualAccountConfig:

    def __init__(self, reusable_status: bool = None, min_amount: str = None, max_amount: str = None):
        self.reusable_status = reusable_status
        self.min_amount = min_amount
        self.max_amount = max_amount
    
    def json(self) -> dict:
        param: dict = {}
        if self.reusable_status is not None:
            param["reusableStatus"] = self.reusable_status
        if self.min_amount is not None:
            param["minAmount"] = self.min_amount
        if self.max_amount is not None:
            param["maxAmount"] = self.max_amount
        return param