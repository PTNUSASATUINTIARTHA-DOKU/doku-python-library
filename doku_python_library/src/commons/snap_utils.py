import uuid
from datetime import datetime, timedelta
import pytz

class SnapUtils:

    @staticmethod
    def generate_external_id() -> str:
        now = datetime.now()
        utc_timezone = pytz.utc
        utc_time_now = now.astimezone(utc_timezone)
        date_string = utc_time_now.strftime('%Y-%m-%dT%H:%M:%SZ')
        return uuid.uuid4().hex + date_string