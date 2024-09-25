import uuid
from datetime import datetime, timedelta
import pytz
from doku_python_library.src.model.general.request_header import RequestHeader
import time
import random
import string

class SnapUtils:

    @staticmethod
    def generate_external_id() -> str:
        timestamp = int(time.time())
        random_numeric = ''.join(random.choices(string.digits, k=16))
        return random_numeric + str(timestamp)
    
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