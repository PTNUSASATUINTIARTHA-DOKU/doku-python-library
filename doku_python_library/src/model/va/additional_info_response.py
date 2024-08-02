class AdditionalInfoResponse:

    def __init__(self, channel: str, howToPayPage: str, howToPayApi: str) -> None:
        self.channel = channel
        self.how_to_pay_page = howToPayPage
        self.how_to_pay_api = howToPayApi