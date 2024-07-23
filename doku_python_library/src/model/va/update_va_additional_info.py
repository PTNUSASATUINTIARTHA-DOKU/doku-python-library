from doku_python_library.src.model.va.update_va_config import UpdateVAConfig

class UpdateVAAdditionalInfo:

    def __init__(self, channel: str, virtualAccountConfig: UpdateVAConfig = None):
        self.channel = channel
        self.virtual_account_config = virtualAccountConfig
    
    def create_request_body(self) -> dict:
        param: dict = {
            "channel": self.channel
        }
        if self.virtual_account_config is not None:
            param["virtualAccountConfig"] = self.virtual_account_config.create_request_body()
        return param