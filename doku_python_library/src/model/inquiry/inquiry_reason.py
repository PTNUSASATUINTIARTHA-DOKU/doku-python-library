class InquiryReason:

    def __init__(self, english: str, indonesia: str) -> None:
        self.english = english
        self.indonesia = indonesia
    
    def json(self) -> dict:
        return {
            "english": self.english,
            "indonesia": self.indonesia
        }