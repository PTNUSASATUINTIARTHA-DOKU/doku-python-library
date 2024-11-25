from doku_python_library.src.model.va.origin import Origin
class AccountBindingAdditionalInfoRequest:

    def __init__(self, channel: str, success_registration_url: str, failed_registration_url: str, 
                 cust_id_merchant: str = None, customer_name: str = None, email: str = None, id_card: str = None, 
                 country: str = None, address: str = None, date_of_birth: str = None, device_model: str = None,
                 os_type: str = None, channel_id: str = None) -> None:
        self.channel = channel
        self.cust_id_merchant = cust_id_merchant
        self.customer_name = customer_name
        self.email = email
        self.id_card = id_card
        self.country = country
        self.address = address
        self.date_of_birth = date_of_birth
        self.success_registration_url = success_registration_url
        self.failed_registration_url = failed_registration_url
        self.device_model = device_model
        self.os_type = os_type
        self.channel_id = channel_id
    
    def json(self) -> dict:
        return {
            "channel": self.channel,
            "custIdMerchant": self.cust_id_merchant,
            "email": self.email,
            "idCard": self.id_card,
            "country": self.country,
            "address": self.address,
            "dateOfBirth": self.date_of_birth,
            "successRegistrationUrl": self.success_registration_url,
            "failedRegistrationUrl": self.failed_registration_url,
            "deviceModel": self.device_model,
            "osType": self.os_type,
            "channelId": self.channel_id,
            "origin": Origin.create_request_body()
        }