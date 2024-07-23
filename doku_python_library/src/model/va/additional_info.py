from doku_python_library.src.model.va.virtual_account_config import VirtualAccountConfig

class AdditionalInfo:

    def __init__(self, channel: str, virtual_account_config: VirtualAccountConfig = None) -> None:
        self.channel = channel
        self.virtual_account_config = virtual_account_config
    
    def json(self) -> dict:
        param: dict = {
            "channel": self.channel,
        }
        if self.virtual_account_config is not None:
            param["virtualAccountConfig"] = self.virtual_account_config.json()
        return param