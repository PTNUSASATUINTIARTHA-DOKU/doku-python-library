from doku_python_library.src.model.va.update_va_config import UpdateVAConfig

class UpdateVAAdditionalInfo:

    def __init__(self, channel: str, virtualAccountConfig: UpdateVAConfig):
        self.channel = channel
        self.virtual_account_config = virtualAccountConfig