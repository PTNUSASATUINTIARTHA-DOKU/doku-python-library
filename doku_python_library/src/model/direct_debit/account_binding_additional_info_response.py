
class AccountBindingAdditionalInfoResponse:

    def __init__(self, custIdMerchant: str = None, status: str = None, authCode: str = None) -> None:
        self.cust_id_merchant = custIdMerchant
        self.status = status
        self.auth_code = authCode

    def json(self) -> dict:
        return {
            "custIdMerchant": self.cust_id_merchant if self.cust_id_merchant is not None else None,
            "status": self.status if self.status is not None else None,
            "authCode": self.auth_code if self.auth_code is not None else None
        }