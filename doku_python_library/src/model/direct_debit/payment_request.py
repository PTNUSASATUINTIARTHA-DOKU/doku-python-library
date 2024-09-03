from doku_python_library.src.model.direct_debit.pay_option_detail import PayOptionDetail
from doku_python_library.src.model.direct_debit.payment_additional_info_request import PaymentAdditionalInfoRequest
from doku_python_library.src.model.va.total_amount import TotalAmount
from doku_python_library.src.commons.direct_debit_enum import DirectDebitEnum

class PaymentRequest:

    def __init__(self, partner_reference_no: str, amount: TotalAmount, 
                 pay_option_detail: list[PayOptionDetail], additional_info: PaymentAdditionalInfoRequest, fee_type: str = None) -> None:
        self.partner_reference_no = partner_reference_no
        self.amount = amount
        self.pay_option_detail = pay_option_detail
        self.additional_info = additional_info
        self.fee_type = fee_type

    def create_request_body(self) -> dict:
        options = []
        for option in self.pay_option_detail:
            options.append(option.json())
        return {
            "partnerReferenceNo": self.partner_reference_no,
            "amount": self.amount.json(),
            "payOptionDetails": options,
            "additionalInfo": self.additional_info,
            "feeType": self.fee_type
        }
    
    def validate_request(self):
        self._validate_allo_bank()
        self._validate_bri_bank()
        self._validate_cimb_bank()
        self._validate_ovo()

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
        if self.fee_type.upper() not in ["OUR", "BEN", "SHA"]:
            raise Exception("Value can only be OUR/BEN/SHA for EMONEY_OVO_SNAP")
    
    def _validate_pay_option_detail(self):
        if len(self.pay_option_detail) == 0:
            raise Exception("Pay Option Details cannot be empty for EMONEY_OVO_SNAP")
    
    def _validate_payment_type(self):
        if self.additional_info.payment_type.upper() not in ["SALE", "RECURRING"]:
            raise Exception("additionalInfo.paymentType cannot be empty")
    
    def _validate_allo_bank(self):
        if self.additional_info.channel == DirectDebitEnum.DIRECT_DEBIT_ALLO_SNAP.value:
            self._validate_line_items()
            self._validate_remarks()
    
    def _validate_line_items(self):
        if len(self.additional_info.line_items) == 0:
            raise Exception("additionalInfo.lineItems cannot be empty for DIRECT_DEBIT_ALLO_SNAP")
    
    def _validate_remarks(self):
        if self.additional_info.remarks == "" or self.additional_info.remarks is None:
            raise Exception("additionalInfo.remarks cannot be empty")
    
    def _validate_cimb_bank(self):
        if self.additional_info.channel == DirectDebitEnum.DIRECT_DEBIT_CIMB_SNAP.value:
            self._validate_remarks()
    
    def _validate_bri_bank(self):
        if self.additional_info.channel == DirectDebitEnum.DIRECT_DEBIT_BRI_SNAP.value:
            self._validate_payment_type()