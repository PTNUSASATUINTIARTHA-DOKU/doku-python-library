from doku_python_library.src.model.va.total_amount import TotalAmount
from doku_python_library.src.model.va.update_va_additional_info import UpdateVAAdditionalInfo
import re, datetime
from doku_python_library.src.commons.va_channel_enum import VaChannelEnum

class UpdateVaRequest:

    def __init__(self, partnerServiceId: str, customerNo: str, virtualAccountNo: str, 
                 trxId: str, additionalInfo: UpdateVAAdditionalInfo, virtualAccountName: str = None, 
                 virtualAccountEmail: str = None, virtualAccountPhone: str = None,
                 totalAmount: TotalAmount = None, virtualAccountTrxType: str = None,
                 expiredDate: str = None):
        self.partner_service_id = partnerServiceId
        self.customer_no = customerNo
        self.virtual_acc_no = virtualAccountNo
        self.virtual_acc_name = virtualAccountName
        self.virtual_acc_email = virtualAccountEmail
        self.virtual_acc_phone = virtualAccountPhone
        self.trx_id = trxId
        self.total_amount = totalAmount
        self.additional_info = additionalInfo
        self.virtual_acc_trx_type = virtualAccountTrxType
        self.expired_date = expiredDate

    def validate_update_va_request(self):
        self._validate_partner_service_id()
        self._validate_customer_no()
        if(self.virtual_acc_name is not None):
            self._validate_virtual_acc_name()
        if(self.virtual_acc_email is not None):
            self._validate_virtual_acc_email()
        if(self.virtual_acc_phone is not None):
            self._validate_virtual_acc_phone()
        self._validate_trx_id()
        if self.total_amount is not None:
            if(self.total_amount.value is not None):
                self._validate_amount_value()
            if(self.total_amount.currency is not None):
                self._validate_amount_currency()
        self._validate_info_channel()
        self._validate_config_status()
        if self.additional_info.virtual_account_config.max_amount is not None and self.additional_info.virtual_account_config.min_amount is not None:
            self._validate_config_amount()
        if self.virtual_acc_trx_type is not None:
            self._validate_va_trx_type()
        if(self.expired_date is not None):
            self._validate_expired_date()


    def _validate_partner_service_id(self) -> None:
        pattern = r'^\s{0,7}\d{1,8}$' 
        value: str = self.partner_service_id
        if value is None:
            raise Exception("partnerServiceId cannot be null. Please provide a partnerServiceId. Example: ' 888994'.")
        elif len(value) != 8:
            raise Exception("partnerServiceId must be exactly 8 characters long and equiped with left-padded spaces. Example: ' 888994'.")
        elif not isinstance(value, str):
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
    
    def _validate_virtual_acc_no(self):
        va_no: str = self.virtual_acc_no
        value: str = self.customer_no
        if va_no is None:
            raise Exception("virtualAccountNo cannot be null. Please provide a virtualAccountNo. Example: ' 88899400000000000000000001'.")
        elif not va_no.isascii():
            raise Exception("virtualAccountNo must be a string. Ensure that virtualAccountNo is enclosed in quotes. Example: ' 88899400000000000000000001'.")
        elif va_no != (self.partner_service_id + value):
            raise Exception("virtualAccountNo must be the concatenation of partnerServiceId and customerNo. Example: ' 88899400000000000000000001' (where partnerServiceId is ' 888994' and customerNo is '00000000000000000001').")
        
    def _validate_virtual_acc_name(self) -> None:
        value: str = self.virtual_acc_name
        pattern = r'^[a-zA-Z0-9.\-/+,=_:\'@% ]*$'
        if value is None:
            raise Exception("virtualAccountName cannot be null. Please provide a virtualAccountName. Example: 'Toru Yamashita'.")
        elif len(value) < 1:
            raise Exception("virtualAccountName must be at least 1 character long. Ensure that virtualAccountName is not empty. Example: 'Toru Yamashita'.")
        elif len(value) > 255:
            raise Exception("virtualAccountName must be 255 characters or fewer. Ensure that virtualAccountName is no longer than 255 characters. Example: 'Toru Yamashita'.")
        elif not isinstance(value, str):
            raise Exception("virtualAccountName must be a string. Ensure that virtualAccountName is enclosed in quotes. Example: 'Toru Yamashita'.")
        elif not re.match(pattern, value):
            raise Exception("virtualAccountName can only contain letters, numbers, spaces, and the following characters: .\-/+,=_:'@%. Ensure that virtualAccountName does not contain invalid characters. Example: 'Toru.Yamashita-123'.")
        
    def _validate_virtual_acc_email(self) -> None:
        value: str = self.virtual_acc_email
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not isinstance(value, str):
            raise Exception("virtualAccountEmail must be a string. Ensure that virtualAccountEmail is enclosed in quotes. Example: 'toru@example.com'.")
        elif len(value) < 1:
            raise Exception("virtualAccountEmail must be at least 1 character long. Ensure that virtualAccountEmail is not empty. Example: 'toru@example.com'.")
        elif len(value) > 255:
            raise Exception("virtualAccountEmail must be 255 characters or fewer. Ensure that virtualAccountEmail is no longer than 255 characters. Example: 'toru@example.com'.")
        elif not re.match(pattern, value):
            raise Exception("virtualAccountEmail is not in a valid email format. Ensure it contains an '@' symbol followed by a domain name. Example: 'toru@example.com'.")
    
    def _validate_virtual_acc_phone(self) -> None:
        value: str = self.virtual_acc_phone
        if not isinstance(value, str):
            raise Exception("virtualAccountPhone must be a string. Ensure that virtualAccountPhone is enclosed in quotes. Example: '628123456789'.")
        elif len(value) < 9:
            raise Exception("virtualAccountPhone must be at least 9 characters long. Ensure that virtualAccountPhone is at least 9 characters long. Example: '628123456789'.")
        elif len(value) > 30:
            raise Exception("virtualAccountPhone must be 30 characters or fewer. Ensure that virtualAccountPhone is no longer than 30 characters. Example: '628123456789012345678901234567'.")
    
    def _validate_trx_id(self) -> None:
        value: str = self.trx_id
        if value is None:
            raise Exception("trxId cannot be null. Please provide a trxId. Example: '23219829713'.")
        elif not isinstance(value, str):
            raise Exception("trxId must be a string. Ensure that trxId is enclosed in quotes. Example: '23219829713'.")
        elif len(value) < 1:
            raise Exception("trxId must be at least 1 character long. Ensure that trxId is not empty. Example: '23219829713'.")
        elif len(value) > 64:
            raise Exception("trxId must be 64 characters or fewer. Ensure that trxId is no longer than 64 characters. Example: '23219829713'.")
        
    def _validate_amount_value(self) -> None:
        value: str = self.total_amount.value
        pattern = r'^\d{1,16}\.\d{2}$'
        if not isinstance(value, str):
            raise Exception("totalAmount.value must be a string. Ensure that totalAmount.value is enclosed in quotes. Example: '11500.00'.")
        elif len(value) < 4:
            raise Exception("totalAmount.value must be at least 4 characters long and formatted as 0.00. Ensure that totalAmount.value is at least 4 characters long and in the correct format. Example: '100.00'.")
        elif len(value) > 19:
            raise Exception("totalAmount.value must be 19 characters or fewer and formatted as 9999999999999999.99. Ensure that totalAmount.value is no longer than 19 characters and in the correct format. Example: '9999999999999999.99'.")
        elif not re.match(pattern, value):
            raise Exception("totalAmount.value is an invalid format")
    
    def _validate_amount_currency(self) -> None:
        value: str = self.total_amount.currency
        if not isinstance(value, str):
            raise Exception("totalAmount.currency must be a string. Ensure that totalAmount.currency is enclosed in quotes. Example: 'IDR'.")
        elif len(value) != 3:
            raise Exception("totalAmount.currency must be exactly 3 characters long. Ensure that totalAmount.currency is exactly 3 characters. Example: 'IDR'.")
        elif value != "IDR":
            raise Exception("totalAmount.currency must be 'IDR'. Ensure that totalAmount.currency is 'IDR'. Example: 'IDR'.")
        
    def _validate_info_channel(self) -> None:
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
        
    def _validate_config_status(self) -> None:
        value: str = self.additional_info.virtual_account_config.status
        if value is None:
            raise Exception("additionalInfo.config.status must be not null")
        elif not isinstance(value, str):
            raise Exception("additionalInfo.config.“status must be a string. Ensure that status is enclosed in quotes. Example: ‘INACTIVE’.”")
        elif len(value) < 1:
            raise Exception("additionalInfo.config.“status must be at least 1 character long. Ensure that status is not empty. Example: ‘INACTIVE’.”")
        elif len(value) > 20:
            raise Exception("additionalInfo.config.“status must be 20 characters or fewer. Ensure that status is no longer than 20 characters. Example: ‘INACTIVE’.”")
        elif value not in ["ACTIVE", "INACTIVE"]:
            raise Exception("additionalInfo.config.“status must be either ‘ACTIVE’ or ‘INACTIVE’. Ensure that status is one of these values. Example: ‘INACTIVE’.”")
    
    def _validate_config_amount(self) -> None:
        max_value: str = self.additional_info.virtual_account_config.max_amount
        min_value: str = self.additional_info.virtual_account_config.min_amount
        trx_type: str = self.virtual_acc_trx_type
        pattern = r'^\d{1,16}\.\d{2}$'
        if max_value is not None and min_value is not None:
            if trx_type == "C":
                raise Exception("minAmount and maxAmount only supported for virtualAccountTrxType O and V")
            elif not re.match(pattern, max_value):
                raise Exception("maxAmount is not valid format. Example: 10000.00")
            elif not re.match(pattern, min_value):
                raise Exception("minAmount is not valid format. Example: 10000.00")
            elif float(max_value) < float(min_value):
                raise Exception("maxAmount cannot be lesser than minAmount")

    def _validate_va_trx_type(self) -> None:
        value: str = self.virtual_acc_trx_type
        if not value.isascii():
            raise Exception("virtualAccountTrxType must be a string. Ensure that virtualAccountTrxType is enclosed in quotes. Example: 'C'.")
        elif len(value) != 1:
            raise Exception("virtualAccountTrxType must be exactly 1 character long. Ensure that virtualAccountTrxType is either 'V' or 'O' and 'C. Example: 'C'.")
        elif value not in ["C", "V", "O"]:
            raise Exception("virtualAccountTrxType must be either 'V' or 'C' and 'O. Ensure that virtualAccountTrxType is one of these values. Example: 'C'.")
        
        # if value == "2":
        #     if self.total_amount.value != "0":
        #         raise Exception("“value must be a string, 1-16 characters, with up to 2 decimal places, in ISO 4217 format, and greater than 0. Example: ‘11500.00’.”")
        #     elif self.total_amount.currency != "IDR":
        #         raise Exception("“currency must be a string, exactly 3 characters long, and a valid ISO 4217 currency code. Ensure that currency is enclosed in quotes, exactly 3 characters, and valid. Example: ‘IDR’.”")
            
    def _validate_expired_date(self) -> None:
        value: str = self.expired_date
        try:
            datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S%z")
        except ValueError:
            raise Exception("expiredDate must be in ISO-8601 format. Ensure that expiredDate follows the correct format. Example: '2023-01-01T10:55:00+07:00'.") 
    
    def create_request_body(self) -> dict:
        request: dict = {
            "partnerServiceId": self.partner_service_id,
            "customerNo": self.customer_no,
            "trxId": self.trx_id,
            "virtualAccountNo": self.virtual_acc_no,
            "additionalInfo": self.additional_info.create_request_body()
        }
        if self.virtual_acc_name is not None:
            request["virtualAccountName"] = self.virtual_acc_name
        if self.virtual_acc_email is not None:
            request["virtualAccountEmail"] = self.virtual_acc_email
        if self.virtual_acc_phone is not None:
            request["virtualAccountPhone"] = self.virtual_acc_phone
        if self.total_amount is not None:
            request["totalAmount"] = self.total_amount.json()
        if self.virtual_acc_trx_type is not None:
            request["virtualAccountTrxType"] = self.virtual_acc_trx_type
        if self.expired_date is not None:
            request["expiredDate"] = self.expired_date
        return request
