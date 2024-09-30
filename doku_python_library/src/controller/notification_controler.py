from doku_python_library.src.model.notification.notification_payment_request import PaymentNotificationRequest
from doku_python_library.src.model.notification.notification_payment_body_response import PaymentNotificationResponseBody
from doku_python_library.src.services.notification_service import NotificationService
from doku_python_library.src.model.notification.notification_payment_direct_debit_request import NotificationPaymentDirectDebitRequest
from doku_python_library.src.model.notification.notification_payment_direct_debit_response import NotificationPaymentDirectDebitResponse

class NotificationController:

    @staticmethod
    def generate_notification_response(request: PaymentNotificationRequest) -> PaymentNotificationResponseBody:
        return NotificationService.generate_notification_response(request=request)

    @staticmethod
    def generate_invalid_token_response(request: PaymentNotificationRequest) -> PaymentNotificationResponseBody:
        return NotificationService.generate_invalid_token_response(request=request)

    @staticmethod
    def generate_direct_debit_notification_response() -> NotificationPaymentDirectDebitResponse:
        return NotificationService.generate_direct_debit_notification_response()
    
    @staticmethod
    def generate_direct_debit_invalid_token_response() -> NotificationPaymentDirectDebitResponse:
        return NotificationService.generate_direct_debit_invalid_token_response()