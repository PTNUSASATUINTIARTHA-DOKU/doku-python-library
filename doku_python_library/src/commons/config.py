class _Production:
    BASE_URL = "https://api.doku.com"

class _Development:
    BASE_URL = "https://api-uat.doku.com"

class Config:

    @staticmethod
    def get_base_url(is_production: bool) -> str:
        return _config_by_name["prod" if is_production else "dev"].BASE_URL

_config_by_name = dict(
    dev = _Development,
    prod = _Production
)