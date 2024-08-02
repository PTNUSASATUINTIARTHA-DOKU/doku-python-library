from doku_python_library.src.model.notification.notification_virtual_account_data import NotificationVirtualAccountData

class PaymentNotificationResponseBody:

    def __init__(self, responseCode: str, responseMessage: str, virtualAccountData: NotificationVirtualAccountData) -> None:
        self.response_code = responseCode
        self.response_message = responseMessage
        self.virtual_account_data = virtualAccountData