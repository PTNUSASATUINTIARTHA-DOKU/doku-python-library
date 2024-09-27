from doku_python_library.src.model.direct_debit.account_unbinding_additional_info_request import AccountUnbindingAdditionalInfoRequest
from doku_python_library.src.commons.direct_debit_enum import DirectDebitEnum

class CardUnbindingRequest:

    def __init__(self, token: str, additional_info: AccountUnbindingAdditionalInfoRequest = None) -> None:
        self.token = token
        self.additional_info = additional_info
    
    def create_request_body(self) -> dict:
        return {
            "tokenId": self.token,
            "additionalInfo": self.additional_info.json()
        }

    def validate_request(self):
        dd_enum = [e.value for e in DirectDebitEnum]
        if self.additional_info.channel not in dd_enum:
            raise Exception("additionalInfo.channel is not valid. Ensure that additionalInfo.channel is one of the valid channels. Example: 'DIRECT_DEBIT_ALLO_SNAP'.")