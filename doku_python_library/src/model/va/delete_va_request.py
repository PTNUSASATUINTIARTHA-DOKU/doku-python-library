from doku_python_library.src.model.va.delete_va_additional_info import DeleteVAAdditionalInfo
from doku_python_library.src.commons.va_channel_enum import VaChannelEnum
import re

class DeleteVARequest:

    def __init__(self, partner_service_id: str, customer_no: str, virtual_acc_no: str, trx_id: str, additional_info: DeleteVAAdditionalInfo) -> None:
        self.partner_service_id = partner_service_id
        self.customer_no = customer_no
        self.virtual_acc_no = virtual_acc_no
        self.trx_id = trx_id
        self.additional_info = additional_info

    def validate_delete_request(self) -> None:
        self._validate_partner_service_id()
        self._validate_customer_no()
        self._validate_virtual_acc_no()
        self._validate_trx_id()
        self._validate_channel()

    def _validate_partner_service_id(self) -> None:
        pattern = r'^\s{0,7}\d{1,8}$' 
        value: str = self.partner_service_id
        if value is None:
            raise Exception("partnerServiceId cannot be null. Please provide a partnerServiceId. Example: ' 888994'.")
        elif len(value) != 8:
            raise Exception("partnerServiceId must be exactly 8 characters long and equiped with left-padded spaces. Example: ' 888994'.")
        elif not value.isascii():
            raise Exception("partnerServiceId must be a string. Ensure that partnerServiceId is enclosed in quotes. Example: ' 888994'.")
        elif not re.match(pattern, value):
            raise Exception("partnerServiceId must consist of up to 8 digits of character. Remaining space in case of partner serivce id is less than 8 must be filled with spaces. Example: ' 888994' (2 spaces and 6 digits).")
    
    def _validate_customer_no(self) -> None:
        pattern = r'^\d+$'
        value: str = self.customer_no
        if value is None:
            raise Exception("customerNo must be a string. Ensure that customerNo is enclosed in quotes. Example: '00000000000000000001'.")
        elif len(value) > 20:
            raise Exception("customerNo must be 20 characters or fewer. Ensure that customerNo is no longer than 20 characters. Example: '00000000000000000001'.")
        elif not re.match(pattern, value):
            raise Exception("customerNo must consist of only digits. Ensure that customerNo contains only numbers. Example: '00000000000000000001'.")
        self._validate_virtual_acc_no()
    
    def _validate_virtual_acc_no(self) -> None:
        va_no: str = self.virtual_acc_no
        if va_no is None:
            raise Exception("virtualAccountNo cannot be null. Please provide a virtualAccountNo. Example: ' 88899400000000000000000001'.")
        elif not va_no.isascii():
            raise Exception("virtualAccountNo must be a string. Ensure that virtualAccountNo is enclosed in quotes. Example: ' 88899400000000000000000001'.")
    
    def _validate_trx_id(self) -> None:
        value: str = self.trx_id
        if value is None:
            raise Exception("trxId cannot be null. Please provide a trxId. Example: '23219829713'.")
        elif not value.isascii():
            raise Exception("trxId must be a string. Ensure that trxId is enclosed in quotes. Example: '23219829713'.")
        elif len(value) < 1:
            raise Exception("trxId must be at least 1 character long. Ensure that trxId is not empty. Example: '23219829713'.")
        elif len(value) > 64:
            raise Exception("trxId must be 64 characters or fewer. Ensure that trxId is no longer than 64 characters. Example: '23219829713'.")
    
    def _validate_channel(self) -> None:
        value: str = self.additional_info.channel  
        va_enum = [e.value for e in VaChannelEnum]
        if not value.isascii():
            raise Exception("additionalInfo.channel must be a string. Ensure that additionalInfo.channel is enclosed in quotes. Example: 'VIRTUAL_ACCOUNT_MANDIRI'.")
        elif len(value) < 1:
            raise Exception("additionalInfo.channel must be at least 1 character long. Ensure that additionalInfo.channel is not empty. Example: 'VIRTUAL_ACCOUNT_MANDIRI'.")
        elif len(value) > 30:
            raise Exception("additionalInfo.channel must be 30 characters or fewer. Ensure that additionalInfo.channel is no longer than 30 characters. Example: 'VIRTUAL_ACCOUNT_MANDIRI'.")
        elif value not in va_enum:
            raise Exception("additionalInfo.channel is not valid. Ensure that additionalInfo.channel is one of the valid channels. Example: 'VIRTUAL_ACCOUNT_MANDIRI'.")
        
    def create_request_body(self) -> dict:
        request = {
            "partnerServiceId" : self.partner_service_id,
            "customerNo": self.customer_no,
            "virtualAccountNo": self.virtual_acc_no,
            "trxId": self.trx_id,
            "additionalInfo": self.additional_info.json()
        }
        return request