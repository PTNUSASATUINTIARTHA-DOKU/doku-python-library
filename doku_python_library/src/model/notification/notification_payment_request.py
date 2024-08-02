from doku_python_library.src.model.va.total_amount import TotalAmount

class PaymentNotificationRequest:

    def __init__(self, partnerServiceId: str, customerNo: str, virtualAccountNo: str,
                 virtualAccountName: str, trxId: str, paymentRequestId: str,
                 paidAmount: TotalAmount, virtualAccountEmail: str, virtualAccountPhone: str) -> None:
        self.partner_service_id = partnerServiceId
        self.customer_no = customerNo
        self.virtual_acc_no = virtualAccountNo
        self.virtual_acc_name = virtualAccountName
        self.trx_id = trxId
        self.payment_request_id = paymentRequestId
        self.paid_amount = paidAmount
        self.virtual_acc_email = virtualAccountEmail
        self.virtual_acc_phone = virtualAccountPhone