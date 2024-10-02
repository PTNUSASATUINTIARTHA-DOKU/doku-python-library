from doku_python_library.src.model.va.total_amount import TotalAmount
from doku_python_library.src.model.direct_debit.check_status_additional_info_request import CheckStatusAdditionalInfoRequest
from doku_python_library.src.commons.direct_debit_enum import DirectDebitEnum

class CheckStatusRequest:

    def __init__(self, service_code: str, original_partner_reference_no: str = None,
                 original_reference_no: str = None, original_external_id: str = None,
                 transaction_date: str = None, amount: TotalAmount = None, merchant_id: str = None,
                 sub_merchant_id: str = None, external_store_id: str = None, additional_info: CheckStatusAdditionalInfoRequest = None) -> None:
        self.service_code = service_code
        self.original_partner_reference_no = original_partner_reference_no
        self.original_reference_no = original_reference_no
        self.original_external_id = original_external_id
        self.transcation_date = transaction_date
        self.amount = amount
        self.merchant_id = merchant_id
        self.sub_merchant_id = sub_merchant_id
        self.external_store_id = external_store_id
        self.additional_info = additional_info
    
    def create_request_body(self) -> dict:
        return {
            "originalPartnerReferenceNo": self.original_partner_reference_no,
            "originalReferenceNo": self.original_reference_no,
            "originalExternalId": self.original_external_id,
            "serviceCode": self.service_code,
            "transactionDate": self.transcation_date,
            "amount": self.amount.json() if self.amount is not None else None,
            "merchantId": self.merchant_id,
            "subMerchantId": self.sub_merchant_id,
            "externalStoreId": self.external_store_id,
            "additionalInfo": self.additional_info.json() if self.additional_info is not None else None
        }

    def validate_request(self):
        if self.service_code != "55":
            raise Exception("serviceCode must be 55.")
        dd_enum = [e.value for e in DirectDebitEnum]
        if self.additional_info.channel not in dd_enum:
            raise Exception("additionalInfo.channel is not valid. Ensure that additionalInfo.channel is one of the valid channels. Example: 'DIRECT_DEBIT_ALLO_SNAP'.")