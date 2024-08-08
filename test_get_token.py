from doku_python_library.src.commons.config import Config
import unittest
from unittest.mock import patch, Mock
from util import Util
import requests


class TestGetToken(unittest.TestCase):

    def setUp(self) -> None:
        self.access_token_url = "/authorization/v1/access-token/b2b"

    @patch('requests.post')
    def test_get_token_success(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_tokenb2b_response("2007300")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        response = requests.post(Config.get_base_url(is_production=False)+self.access_token_url)

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.access_token_url)
        self.assertEqual(response.json().response_code, resp_dict.response_code)

    @patch('requests.post')
    def test_get_token_invalid_client_id(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_tokenb2b_response("5007300")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        response = requests.post(Config.get_base_url(is_production=False)+self.access_token_url)

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.access_token_url)
        self.assertEqual(response.json().response_code, resp_dict.response_code)



if __name__ == "__main__":
    unittest.main()