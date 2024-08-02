from doku_python_library.src.model.va.delete_va_additional_info_response import DeleteVaResponseAdditionalInfo
class DeleteVAResponseVirtualAccountData:

    def __init__(self, partnerServiceId: str, customerNo: str, virtualAccountNo: str, trxId: str, additionalInfo: DeleteVaResponseAdditionalInfo) -> None:
        self.partner_service_id = partnerServiceId
        self.customer_no: customerNo
        self.virtual_acc_no: virtualAccountNo
        self.trx_id: trxId
        self.additional_info = additionalInfo