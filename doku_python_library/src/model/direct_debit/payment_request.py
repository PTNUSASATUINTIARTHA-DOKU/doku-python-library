from doku_python_library.src.model.direct_debit.pay_option_detail import PayOptionDetail
from doku_python_library.src.model.direct_debit.payment_additional_info_request import PaymentAdditionalInfoRequest
from doku_python_library.src.model.va.total_amount import TotalAmount
from doku_python_library.src.commons.direct_debit_enum import DirectDebitEnum
import re

class PaymentRequest:

    def __init__(self, partner_reference_no: str, amount: TotalAmount, 
                additional_info: PaymentAdditionalInfoRequest, charge_token: str = None, fee_type: str = None, pay_option_detail: list[PayOptionDetail]= None) -> None:
        self.partner_reference_no = partner_reference_no
        self.amount = amount
        self.pay_option_detail = pay_option_detail
        self.additional_info = additional_info
        self.charge_token = charge_token
        self.fee_type = fee_type

    def create_request_body(self) -> dict:
        if self.pay_option_detail != None:
            options = []
            for option in self.pay_option_detail:
                options.append(option.json())
        return {
            "partnerReferenceNo": self.partner_reference_no,
            "amount": self.amount.json(),
            "additionalInfo": self.additional_info.json(),
            "chargeToken": self.charge_token,
            "feeType": self.fee_type
        }
    
    def validate_request(self):
        self._validate_allo_bank()
        self._validate_bri_bank()
        self._validate_cimb_bank()
        self._validate_ovo()
        self._validate_channel()
        self._validate_amount_value()
        self._validate_amount_currency()
        self._validate_success_payment_url()
        self._validate_failed_payment_url()

    def _validate_channel(self):
        dd_enum = [e.value for e in DirectDebitEnum]
        if self.additional_info.channel not in dd_enum:
            raise Exception("additionalInfo.channel is not valid. Ensure that additionalInfo.channel is one of the valid channels. Example: 'DIRECT_DEBIT_ALLO_SNAP'.") 
    
    def _validate_ovo(self):
        if self.additional_info.channel == DirectDebitEnum.EMONEY_OVO_SNAP.value:
            self._validate_fee_type()
            self._validate_pay_option_detail()
            self._validate_payment_type()

    def _validate_fee_type(self):
        if self.fee_type is not None:
            if self.fee_type.upper() not in ["OUR", "BEN", "SHA"]:
                raise Exception("Value can only be OUR/BEN/SHA for EMONEY_OVO_SNAP")
    
    def _validate_pay_option_detail(self):
        if self.pay_option_detail is not None:
            if len(self.pay_option_detail) == 0:
                raise Exception("Pay Option Details cannot be empty for EMONEY_OVO_SNAP")
    
    def _validate_payment_type(self):
        if self.additional_info.payment_type is not None:
            if self.additional_info.payment_type.upper() not in ["SALE", "RECURRING"]:
                raise Exception("additionalInfo.paymentType cannot be empty")
    
    def _validate_allo_bank(self):
        if self.additional_info.channel == DirectDebitEnum.DIRECT_DEBIT_ALLO_SNAP.value:
            self._validate_line_items()
            self._validate_remarks()
    
    def _validate_line_items(self):
        if self.additional_info.line_items is not None:
            if len(self.additional_info.line_items) == 0:
                raise Exception("additionalInfo.lineItems cannot be empty for DIRECT_DEBIT_ALLO_SNAP")
    
    def _validate_remarks(self):
        if self.additional_info.remarks == "" or self.additional_info.remarks is None or len(self.additional_info.remarks) > 40:
            raise Exception("additionalInfo.remarks must be 40 characters or fewer. Ensure that additionalInfo.remarks is no longer than 40 characters. Example: 'remarks'.")
    
    def _validate_cimb_bank(self):
        if self.additional_info.channel == DirectDebitEnum.DIRECT_DEBIT_CIMB_SNAP.value:
            self._validate_remarks()
    
    def _validate_bri_bank(self):
        if self.additional_info.channel == DirectDebitEnum.DIRECT_DEBIT_BRI_SNAP.value:
            self._validate_payment_type()

    def _validate_amount_value(self) -> None:
        value: str = self.amount.value
        pattern = r'^\d{1,16}\.\d{2}$'
        if value is None:
            raise Exception("totalAmount.value cant be null")
        elif len(value) < 4:
            raise Exception("totalAmount.value must be at least 4 characters long and formatted as 0.00. Ensure that totalAmount.value is at least 4 characters long and in the correct format. Example: '100.00'.")
        elif len(value) > 19:
            raise Exception("totalAmount.value must be 19 characters or fewer and formatted as 9999999999999999.99. Ensure that totalAmount.value is no longer than 19 characters and in the correct format. Example: '9999999999999999.99'.")
        elif not re.match(pattern, value):
            raise Exception("totalAmount.value is an invalid format")
    
    def _validate_amount_currency(self) -> None:
        value: str = self.amount.currency
        if not value.isascii():
            raise Exception("totalAmount.currency must be a string. Ensure that totalAmount.currency is enclosed in quotes. Example: 'IDR'.")
        elif len(value) != 3:
            raise Exception("totalAmount.currency must be exactly 3 characters long. Ensure that totalAmount.currency is exactly 3 characters. Example: 'IDR'.")
        elif value != "IDR":
            raise Exception("totalAmount.currency must be 'IDR'. Ensure that totalAmount.currency is 'IDR'. Example: 'IDR'.")
    
    def _validate_success_payment_url(self):
        value: str = self.additional_info.success_payment_url
        if value is None:
            raise Exception("additionalInfo.successPaymentUrl cannot be null. Ensure that additionalInfo.successPaymentUrl is one of the valid channels. Example: 'https://www.doku.com'.")
    
    def _validate_failed_payment_url(self):
        value: str = self.additional_info.failed_payment_url
        if value is None:
            raise Exception("additionalInfo.failedPaymentUrl cannot be null. Ensure that additionalInfo.failedPaymentUrl is one of the valid channels. Example: 'https://www.doku.com'.")