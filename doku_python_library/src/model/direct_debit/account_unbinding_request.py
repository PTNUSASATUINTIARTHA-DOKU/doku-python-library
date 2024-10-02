from doku_python_library.src.model.direct_debit.account_unbinding_additional_info_request import AccountUnbindingAdditionalInfoRequest
from doku_python_library.src.commons.direct_debit_enum import DirectDebitEnum

class AccountUnbindingRequest:

    def __init__(self, token: str, additional_info: AccountUnbindingAdditionalInfoRequest = None) -> None:
        self.token = token
        self.additional_info = additional_info
    
    def create_request_body(self) -> dict:
        return {
            "tokenId": self.token,
            "additionalInfo": self.additional_info.json()
        }

    def validate_request(self):
        self._validate_token_id()
        self._validate_channel()
        
    def _validate_channel(self):
        dd_enum = [e.value for e in DirectDebitEnum]
        if self.additional_info.channel not in dd_enum:
            raise Exception("additionalInfo.channel is not valid. Ensure that additionalInfo.channel is one of the valid channels. Example: 'DIRECT_DEBIT_ALLO_SNAP'.")
    
    def _validate_token_id(self):
        value: str = self.token
        if len(value) > 2048:
                raise Exception("tokenId must be 2048 characters or fewer. Ensure that tokenId is no longer than 2048 characters. Example: 'eyJhbGciOiJSUzI1NiJ...'.")