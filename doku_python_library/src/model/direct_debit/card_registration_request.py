from doku_python_library.src.model.direct_debit.card_registration_additional_info import CardRegistrationAdditionalInfo
from doku_python_library.src.commons.direct_debit_enum import DirectDebitEnum

class CardRegistrationRequest:

    def __init__(self, card_data: str, cust_id_merchant: str,
                additionalInfo: CardRegistrationAdditionalInfo, phone_no: str = None) -> None:
        self.card_data = card_data
        self.cust_id_merchant = cust_id_merchant
        self.additional_info = additionalInfo
        self.phone_no = phone_no
    
    def create_request_body(self) -> dict:
        return {
            "cardData": self.card_data,
            "custIdMerchant": self.cust_id_merchant,
            "phoneNoe": self.phone_no,
            "additionalInfo": self.additional_info.json()
        }
    
    def validate_request(self):
        dd_enum = [e.value for e in DirectDebitEnum]
        if self.additional_info.channel not in dd_enum:
            raise Exception("additionalInfo.channel is not valid. Ensure that additionalInfo.channel is one of the valid channels. Example: 'DIRECT_DEBIT_ALLO_SNAP'.")