from doku_python_library.src.model.va.total_amount import TotalAmount
from doku_python_library.src.model.va.additional_info_response import AdditionalInfoResponse


class VirtualAccountData:

    def __init__(self, 
                 partnerServiceId: str, 
                 virtualAccountName: str,
                 trxId: str,
                 totalAmount: TotalAmount,
                 additionalInfo: AdditionalInfoResponse,
                 customerNo: str = None, 
                 virtualAccountNo: str = None,
                 virtualAccountEmail: str = None,
                 ) -> None:
        self.partner_service_id = partnerServiceId
        self.customer_no = customerNo
        self.virtual_acc_no = virtualAccountNo
        self.virtual_acc_name = virtualAccountName
        self.virtual_acc_email = virtualAccountEmail
        self.trx_id = trxId
        self.total_amount = totalAmount
        self.additional_info = additionalInfo