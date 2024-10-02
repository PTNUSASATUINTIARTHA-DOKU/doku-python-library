from doku_python_library.src.commons.config import Config
import unittest
from unittest.mock import patch, Mock
from util import Util
import requests

class TestCardRegistration(unittest.TestCase):

    def setUp(self) -> None:
        self.card_registration_url = "/direct-debit/core/v1/registration-card-bind"
    
    @patch('requests.post')
    def test_card_registration_success(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_card_registration_response("2000700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_card_registration_request()
        response = requests.post(Config.get_base_url(is_production=False)+self.card_registration_url, json=request.create_request_body())
        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.card_registration_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    def test_card_registration_card_data_null(self):
        request = Util.generate_card_registration_request()
        request.card_data = None
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "cardData cannot be null. Please provide cardData. Example: '5cg2G2719+jxU1RfcGmeCyQrLagUaAWJWWhLpmmb'.")
    
    def test_card_registration_cust_id_merchant_null(self):
        request = Util.generate_card_registration_request()
        request.cust_id_merchant = None
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "custIdMerchant cannot be null. Please provide custIdMerchant. Example: 'cust-001'.")
    
    def test_card_registration_cust_id_merchant_max(self):
        request = Util.generate_card_registration_request()
        request.cust_id_merchant = "12345678901234567890123456789012345678901234567890123456789011234567890123456789012345678901234567890123456789012345678901"
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "custIdMerchant must be 64 characters or fewer. Ensure that custIdMerchant is no longer than 64 characters. Example: 'cust-001'.")
    
    def test_card_registration_channel_invalid(self):
        request = Util.generate_card_registration_request()
        request.additional_info.channel = None
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "additionalInfo.channel is not valid. Ensure that additionalInfo.channel is one of the valid channels. Example: 'DIRECT_DEBIT_ALLO_SNAP'.")
    
    def test_card_registration_success_url_null(self):
        request = Util.generate_card_registration_request()
        request.additional_info.success_registration_url = None
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "additionalInfo.successRegistrationUrl cannot be null. Please provide a additionalInfo.successRegistrationUrl. Example: 'https://www.doku.com'.")
    
    def test_card_registration_failed_url_null(self):
        request = Util.generate_account_binding_request()
        request.additional_info.failed_registration_url = None
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "additionalInfo.failedRegistrationUrl cannot be null. Please provide a additionalInfo.failedRegistrationUrl. Example: 'https://www.doku.com'.")