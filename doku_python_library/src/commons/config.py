
class _Production:
    BASE_URL = "https://api.doku.com"

class _Development:
    BASE_URL = "https://api-sandbox.doku.com"

class Config:
    ACCESS_TOKEN: str = "/authorization/v1/access-token/b2b"
    CREATE_VA: str = "/virtual-accounts/bi-snap-va/v1.1/transfer-va/create-va"
    UPDATE_VA: str = "/virtual-accounts/bi-snap-va/v1.1/transfer-va/update-va"
    DELETE_VA: str = "/virtual-accounts/bi-snap-va/v1.1/transfer-va/delete-va"
    CHECK_STATUS_VA: str = "/orders/v1.0/transfer-va/status"
    DIRECT_DEBIT_ACCOUNT_BINDING_URL = "/direct-debit/core/v1/registration-account-binding"
    ACCESS_TOKEN_B2B2C = "/authorization/v1/access-token/b2b2c"
    DIRECT_DEBIT_PAYMENT_URL = "/direct-debit/core/v1/debit/payment-host-to-host"
    DIRECT_DEBIT_BALANCE_INQUIRY_URL = "/direct-debit/core/v1/balance-inquiry"
    DIRECT_DEBIT_ACCOUNT_UNBINDING_URL = "/direct-debit/core/v1/registration-account-unbinding"
    DIRECT_DEBIT_CARD_REGISTRATION = "/direct-debit/core/v1/registration-card-bind"
    DIRECT_DEBIT_CARD_UNBINDING_URL= "/direct-debit/core/v1/registration-card-unbind"
    DIRECT_DEBIT_REFUND = "/direct-debit/core/v1/debit/refund"
    DIRECT_DEBIT_CHECK_STATUS = "/orders/v1.0/debit/status"

    @staticmethod
    def get_base_url(is_production: bool) -> str:
        return _config_by_name["prod" if is_production else "dev"].BASE_URL

_config_by_name = dict(
    dev = _Development,
    prod = _Production
)