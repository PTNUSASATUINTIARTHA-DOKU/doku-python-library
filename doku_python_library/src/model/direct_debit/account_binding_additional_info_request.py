class AccountBindingAdditionalInfoRequest:

    def __init__(self, channel: str, cust_id_merchant: str, customer_name: str,
                 email: str, id_card: str, country: str, address: str, date_of_birth: str,
                 success_registration_url: str, failed_registration_url: str, device_model: str,
                 os_type: str, channel_id: str) -> None:
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
            "channelId": self.channel_id
        }