from doku_python_library.src.model.direct_debit.card_registration_additional_info import CardRegistrationAdditionalInfo
from doku_python_library.src.model.direct_debit.bank_card_data import BankCardData
from doku_python_library.src.commons.direct_debit_enum import DirectDebitEnum
from typing import Union

class CardRegistrationRequest:

    def __init__(self, card_data: Union[str, BankCardData], cust_id_merchant: str,
                additionalInfo: CardRegistrationAdditionalInfo, phone_no: str) -> None:
        self.card_data = card_data
        self.cust_id_merchant = cust_id_merchant
        self.additional_info = additionalInfo
        self.phone_no = phone_no
    
    def create_request_body(self) -> dict:
        return {
            "cardData": self.card_data.json() if isinstance(self.card_data, BankCardData) else self.card_data,
            "custIdMerchant": self.cust_id_merchant,
            "phoneNo": self.phone_no,
            "additionalInfo": self.additional_info.json()
        }
    
    def validate_request(self):
        self._validate_card_data()
        self._validate_cust_id_merchant()
        self._validate_channel()
        self._validate_success_registration_url()
        self._validate_failed_registration_url()
    
    def _validate_card_data(self):
        value: str = self.card_data
        if value is None:
            raise Exception("cardData cannot be null. Please provide cardData. Example: '5cg2G2719+jxU1RfcGmeCyQrLagUaAWJWWhLpmmb'.")

    def _validate_cust_id_merchant(self):
        value: str = self.cust_id_merchant
        if value is None:
            raise Exception("custIdMerchant cannot be null. Please provide custIdMerchant. Example: 'cust-001'.")
        elif len(value) > 64:
            raise Exception("custIdMerchant must be 64 characters or fewer. Ensure that custIdMerchant is no longer than 64 characters. Example: 'cust-001'.")

    def _validate_channel(self):
        dd_enum = [e.value for e in DirectDebitEnum]
        if self.additional_info.channel not in dd_enum:
            raise Exception("additionalInfo.channel is not valid. Ensure that additionalInfo.channel is one of the valid channels. Example: 'DIRECT_DEBIT_ALLO_SNAP'.")
    
    def _validate_success_registration_url(self):
        value: str = self.additional_info.success_registration_url
        if value is None:
            raise Exception("additionalInfo.successRegistrationUrl cannot be null. Please provide a additionalInfo.successRegistrationUrl. Example: 'https://www.doku.com'.")
    
    def _validate_failed_registration_url(self):
        value: str = self.additional_info.failed_registration_url
        if value is None:
            raise Exception("additionalInfo.failedRegistrationUrl cannot be null. Please provide a additionalInfo.failedRegistrationUrl. Example: 'https://www.doku.com'.")