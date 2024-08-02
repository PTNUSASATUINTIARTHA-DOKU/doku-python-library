from doku_python_library.src.model.notification.notification_payment_request import PaymentNotificationRequest
from doku_python_library.src.model.notification.notification_payment_body_response import PaymentNotificationResponseBody
from doku_python_library.src.model.notification.notification_virtual_account_data import NotificationVirtualAccountData

class NotificationService:

    @staticmethod
    def generate_notification_response(request: PaymentNotificationRequest) -> PaymentNotificationResponseBody:
        return PaymentNotificationResponseBody(
            responseCode="2002500",
            responseMessage="success",
            virtualAccountData= NotificationVirtualAccountData(
                partnerServiceId= request.partner_service_id,
                customerNo=request.customer_no,
                virtualAccountNo= request.virtual_acc_no,
                virtualAccountName=request.virtual_acc_name,
                paymentRequestId=request.payment_request_id
            )
        )
    
    @staticmethod
    def generate_invalid_token_response(request: PaymentNotificationRequest) -> PaymentNotificationResponseBody:
        return PaymentNotificationResponseBody(
            responseCode= "4012701",
            responseMessage= "Invalid Token (B2B)",
            virtualAccountData=NotificationVirtualAccountData(
                partnerServiceId=request.partner_service_id,
                customerNo=request.customer_no,
                virtualAccountNo=request.virtual_acc_no,
                virtualAccountName=request.virtual_acc_name,
                paymentRequestId=request.payment_request_id
            )
        )