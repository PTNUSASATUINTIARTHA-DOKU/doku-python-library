import uuid
from datetime import datetime, timedelta
import pytz
from doku_python_library.src.model.general.request_header import RequestHeader

class SnapUtils:

    @staticmethod
    def generate_external_id() -> str:
        now = datetime.now()
        utc_timezone = pytz.utc
        utc_time_now = now.astimezone(utc_timezone)
        date_string = utc_time_now.strftime('%Y-%m-%dT%H:%M:%SZ')
        return uuid.uuid4().hex + date_string
    
    @staticmethod
    def generate_request_header(channel_id: str, client_id: str, 
                                 token_b2b: str, timestamp: str, external_id: str, signature: str, device_id: str = None, ip_address: str = None,
                                 token_b2b2c: str = None) -> RequestHeader:
        header: RequestHeader = RequestHeader(
            x_timestamp= timestamp,
            x_signature= signature,
            x_partner_id= client_id,
            authorization= token_b2b,
            x_external_id= external_id,
            channel_id= channel_id,
            device_id=device_id,
            ip_address=ip_address,
            token_b2b2c=token_b2b2c
        )
        return header