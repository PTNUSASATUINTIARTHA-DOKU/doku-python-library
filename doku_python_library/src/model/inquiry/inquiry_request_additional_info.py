from doku_python_library.src.model.va.virtual_account_config import VirtualAccountConfig

class InquiryRequestAdditionalInfo:

    def __init__(self, channel: str, trxId: str = None, virtualAccountConfig: VirtualAccountConfig = None) -> None:
        self.channel = channel
        self.trx_id = trxId
        self.virtual_acc_config = virtualAccountConfig
    
    def json(self) -> dict:
        return {
            "channel": self.channel,
            "trxId": self.trx_id,
            "virtualAccountConfig": self.virtual_acc_config.json()
        }