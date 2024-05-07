class AdditionalInfoResponse:

    def __init__(self, channel: str, how_to_pay_page: str, how_to_pay_api: str) -> None:
        self.channel = channel
        self.how_to_pay_page = how_to_pay_page
        self.how_to_pay_api = how_to_pay_api