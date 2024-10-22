from doku_python_library.src.model.direct_debit.refund_additional_info import RefundAdditionalInfo
from doku_python_library.src.model.va.total_amount import TotalAmount
from doku_python_library.src.commons.direct_debit_enum import DirectDebitEnum
import re

class RefundRequest:

    def __init__(self, original_partner_reference_no: str, refund_amount: TotalAmount, partner_refund_no: str,
                 additional_info: RefundAdditionalInfo, original_external_id: str = None, reason: str = None) -> None:
        self.original_partner_reference_no = original_partner_reference_no
        self.refund_amount = refund_amount
        self.partner_refund_no = partner_refund_no
        self.additional_info = additional_info
        self.original_external_id = original_external_id
        self.reason = reason

    def create_request_body(self) -> dict:
        return {
            "originalPartnerReferenceNo": self.original_partner_reference_no,
            "refundAmount": self.refund_amount.json(),
            "partnerRefundNo": self.partner_refund_no,
            "additionalInfo": self.additional_info.json(),
            "originalExternalId": self.original_external_id,
            "reason": self.reason
        }

    def validate_request(self):
        self._validate_channel()
        self._validate_original_partner_reference_no()
        self._validate_amount_value()
        self._validate_amount_currency()
        self._validate_partner_refund_no()
    
    def _validate_channel(self):
        dd_enum = [e.value for e in DirectDebitEnum]
        if self.additional_info.channel not in dd_enum:
            raise Exception("additionalInfo.channel is not valid. Ensure that additionalInfo.channel is one of the valid channels. Example: 'DIRECT_DEBIT_ALLO_SNAP'.")
    
    def _validate_original_partner_reference_no(self):
        value: str = self.original_partner_reference_no
        channel: str = self.additional_info.channel
        if value is None:
            raise Exception("originalPartnerReferenceNo cannot be null. Please provide a originalPartnerReferenceNo. Example: 'INV-0001'.")
        if channel == "EMONEY_OVO_SNAP":
            if len(value) > 32:
                raise Exception("originalPartnerReferenceNo must be 32 characters or fewer. Ensure that originalPartnerReferenceNo is no longer than 32 characters. Example: 'INV-001'.")
        elif channel == "EMONEY_DANA_SNAP" or channel == "EMONEY_SHOPEE_PAY_SNAP" or channel == "DIRECT_DEBIT_ALLO_SNAP":
            if len(value) > 64:
                raise Exception("originalPartnerReferenceNo must be 64 characters or fewer. Ensure that originalPartnerReferenceNo is no longer than 64 characters. Example: 'INV-001'.")
        elif channel == "DIRECT_DEBIT_CIMB_SNAP" or channel == "DIRECT_DEBIT_BRI_SNAP":
            if len(value) > 12:
                raise Exception("originalPartnerReferenceNo must be 12 characters or fewer. Ensure that originalPartnerReferenceNo is no longer than 12 characters. Example: 'INV-001'.")
    
    def _validate_amount_value(self) -> None:
        value: str = self.refund_amount.value
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
        value: str = self.refund_amount.currency
        if not value.isascii():
            raise Exception("totalAmount.currency must be a string. Ensure that totalAmount.currency is enclosed in quotes. Example: 'IDR'.")
        elif len(value) != 3:
            raise Exception("totalAmount.currency must be exactly 3 characters long. Ensure that totalAmount.currency is exactly 3 characters. Example: 'IDR'.")
        elif value != "IDR":
            raise Exception("totalAmount.currency must be 'IDR'. Ensure that totalAmount.currency is 'IDR'. Example: 'IDR'.")
    
    def _validate_partner_refund_no(self):
        value: str = self.partner_refund_no
        channel: str = self.additional_info.channel
        if value is None:
            raise Exception("partnerRefundNo cannot be null. Please provide a partnerRefundNo. Example: 'INV-0001'.")
        if channel == "EMONEY_DANA_SNAP" or channel == "EMONEY_SHOPEE_PAY_SNAP" or channel == "EMONEY_OVO_SNAP":
            if len(value) > 64:
                raise Exception("partnerRefundNo must be 64 characters or fewer. Ensure that partnerRefundNo is no longer than 64 characters. Example: 'INV-REF-001'.")
        elif channel == "DIRECT_DEBIT_CIMB_SNAP" or channel == "DIRECT_DEBIT_BRI_SNAP":
            if len(value) > 12:
                raise Exception("partnerRefundNo must be 12 characters or fewer. Ensure that partnerRefundNo is no longer than 12 characters. Example: 'INV-REF-001'.")
        elif channel == "DIRECT_DEBIT_ALLO_SNAP":
            if len(value) < 32 or len(value) > 64:
                raise Exception("partnerRefundNo must be 64 characters and at least 32 characters. Ensure that partnerRefundNo is no longer than 64 characters and at least 32 characters. Example: 'INV-REF-001'.")
            