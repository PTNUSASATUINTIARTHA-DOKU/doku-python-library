class Origin:

    @staticmethod
    def create_request_body() -> dict:
        return {
            "product": "SDK",
            "source": "python",
            "sourceVersion": "1.1.69",
            "system": "doku-python-library",
            "apiFormat": "SNAP"
        }