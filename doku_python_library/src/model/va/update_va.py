from doku_python_library.src.model.va.total_amount import TotalAmount
from doku_python_library.src.model.va.update_va_additional_info import UpdateVAAdditionalInfo

class UpdateVADto:

    def __init__(self, partnerServiceId: str, customerNo: str, virtualAccountNo: str, 
                 virtualAccountName: str, virtualAccountEmail: str, virtualAccountPhone: str,
                 trxId: str, totalAmount: TotalAmount, additionalInfo: UpdateVAAdditionalInfo, virtualAccountTrxType: str ,
                 expiredDate: str):
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