from doku_python_library.src.model.notification.notification_payment_header_response import PaymentNotificationResponseHeader
from doku_python_library.src.model.notification.notification_payment_body_response import PaymentNotificationResponseBody


class PaymentNotificationResponse:

    def __init__(self, header: PaymentNotificationResponseHeader, body: PaymentNotificationResponseBody) -> None:
        self.header = header
        self.body = body