from doku_python_library.src.model.notification.notification_token_header import NotificationTokenHeader
from doku_python_library.src.model.notification.notification_token_body import NotificationTokenBody

class NotificationToken:

    def __init__(self, header: NotificationTokenHeader, body: NotificationTokenBody) -> None:
        self.header = header
        self.body = body