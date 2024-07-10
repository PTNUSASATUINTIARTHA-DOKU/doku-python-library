class Origin:

    @staticmethod
    def create_request_body() -> dict:
        return {
            "product": "SDK",
            "source": "python",
            "sourceVersion": "1.0.0",
            "system": "doku-python-library",
            "apiFormat": "SNAP"
        }