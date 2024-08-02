from doku_python_library.src.model.notification.notification_payment_request import PaymentNotificationRequest
from doku_python_library.src.model.notification.notification_payment_body_response import PaymentNotificationResponseBody
from doku_python_library.src.services.notification_service import NotificationService

class NotificationController:

    @staticmethod
    def generate_notification_response(request: PaymentNotificationRequest) -> PaymentNotificationResponseBody:
        return NotificationService.generate_notification_response(request=request)

    @staticmethod
    def generate_invalid_token_response(request: PaymentNotificationRequest) -> PaymentNotificationResponseBody:
        return NotificationService.generate_invalid_token_response(request=request)