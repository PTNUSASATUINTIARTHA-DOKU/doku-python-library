
class _Production:
    BASE_URL = "https://api.doku.com"

class _Development:
    BASE_URL = "https://api-uat.doku.com"

class Config:
    ACCESS_TOKEN: str = "/authorization/v1/access-token/b2b"
    CREATE_VA: str = "/virtual-accounts/bi-snap-va/v1/transfer-va/create-va"
    @staticmethod
    def get_base_url(is_production: bool) -> str:
        return _config_by_name["prod" if is_production else "dev"].BASE_URL

_config_by_name = dict(
    dev = _Development,
    prod = _Production
)