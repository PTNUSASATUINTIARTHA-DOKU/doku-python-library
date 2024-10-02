from doku_python_library.src.model.direct_debit.balance_inquiry_additional_info import BalanceInquiryAdditionalInfo
from doku_python_library.src.commons.direct_debit_enum import DirectDebitEnum

class BalanceInquiryRequest:

    def __init__(self, additional_info: BalanceInquiryAdditionalInfo) -> None:
        self.additional_info = additional_info
    
    def create_request_body(self) -> dict:
        return {
            "additionalInfo": self.additional_info.json()
        }

    def validate_request(self):
        dd_enum = [e.value for e in DirectDebitEnum]
        if self.additional_info.channel not in dd_enum:
            raise Exception("additionalInfo.channel is not valid. Ensure that additionalInfo.channel is one of the valid channels. Example: 'DIRECT_DEBIT_ALLO_SNAP'.") 