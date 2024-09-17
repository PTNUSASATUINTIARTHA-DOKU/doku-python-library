

class CardRegistrationAdditionalInfo:

    def __init__(self, channel: str, success_registration_url: str, failed_registration_url: str, 
                 customer_name: str = None, email: str = None, id_card: str = None, 
                 country: str = None, address: str = None, date_of_birth: str = None) -> None:
        self.channel = channel
        self.customer_name = customer_name
        self.email = email
        self.id_card = id_card
        self.country = country
        self.address = address
        self.date_of_birth = date_of_birth
        self.success_registration_url = success_registration_url
        self.failed_registration_url = failed_registration_url
    
    def json(self) -> dict:
        return {
            "channel": self.channel,
            "customerName": self.customer_name,
            "email": self.email,
            "idCard": self.id_card,
            "country": self.country,
            "address": self.address,
            "dateOfBirth": self.date_of_birth,
            "successRegistrationUrl": self.success_registration_url,
            "failedRegistrationUrl": self.failed_registration_url,
        }