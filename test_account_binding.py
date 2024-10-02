from doku_python_library.src.commons.config import Config
import unittest
from unittest.mock import patch, Mock, MagicMock
from util import Util
import requests

class TestAccountBinding(unittest.TestCase):

    def setUp(self) -> None:
        self.account_binding_url = "/direct-debit/core/v1/registration-account-binding"
    
    @patch('requests.post')
    def test_account_binding_success(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_account_binding_response("2000700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_account_binding_request()
        response = requests.post(Config.get_base_url(is_production=False)+self.account_binding_url, json=request.json())
        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.account_binding_url, json=request.json())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    def test_account_binding_phone_null(self):
        request = Util.generate_account_binding_request()
        request.phone_no = None
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "phoneNo cannot be null. Please provide a phoneNo. Example: '62813941306101'.")
    
    def test_account_binding_phone_min(self):
        request = Util.generate_account_binding_request()
        request.phone_no = "628891"
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "phoneNo must be at least 9 digits. Ensure that phoneNo is not empty. Example: '62813941306101'.")
    
    def test_account_binding_phone_max(self):
        request = Util.generate_account_binding_request()
        request.phone_no = "12345678909876543"
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "phoneNo must be 16 characters or fewer. Ensure that phoneNo is no longer than 16 characters. Example: '62813941306101'.")
    
    def test_account_binding_channel_null(self):
        request = Util.generate_account_binding_request()
        request.additional_info.channel = None
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "additionalInfo.channel cannot be null. Ensure that additionalInfo.channel is one of the valid channels. Example: 'DIRECT_DEBIT_ALLO_SNAP'.")
    
    def test_account_binding_channel_not_in_enum(self):
        request = Util.generate_account_binding_request()
        request.additional_info.channel = "CHANNEL_A"
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "additionalInfo.channel is not valid. Ensure that additionalInfo.channel is one of the valid channels. Example: 'DIRECT_DEBIT_ALLO_SNAP'.")
    
    def test_account_binding_cust_id_merchant_null(self):
        request = Util.generate_account_binding_request()
        request.additional_info.cust_id_merchant = None
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "additionalInfo.custIdMerchant cannot be null. Please provide a additionalInfo.custIdMerchant. Example: 'cust-001'.")
    
    def test_account_binding_cust_id_merchant_max(self):
        request = Util.generate_account_binding_request()
        request.additional_info.cust_id_merchant = "12345678901234567890123456789012345678901234567890123456789011234567890123456789012345678901234567890123456789012345678901"
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "additionalInfo.custIdMerchant must be 64 characters or fewer. Ensure that additionalInfo.custIdMerchant is no longer than 16 characters. Example: 'cust-001'.")
    
    def test_account_binding_cust_id_merchant_max(self):
        request = Util.generate_account_binding_request()
        request.additional_info.cust_id_merchant = "12345678901234567890123456789012345678901234567890123456789011234567890123456789012345678901234567890123456789012345678901"
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "additionalInfo.custIdMerchant must be 64 characters or fewer. Ensure that additionalInfo.custIdMerchant is no longer than 16 characters. Example: 'cust-001'.")
    
    def test_account_binding_success_url_null(self):
        request = Util.generate_account_binding_request()
        request.additional_info.success_registration_url = None
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "additionalInfo.successRegistrationUrl cannot be null. Please provide a additionalInfo.successRegistrationUrl. Example: 'https://www.doku.com'.")
    
    def test_account_binding_failed_url_null(self):
        request = Util.generate_account_binding_request()
        request.additional_info.failed_registration_url = None
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "additionalInfo.failedRegistrationUrl cannot be null. Please provide a additionalInfo.failedRegistrationUrl. Example: 'https://www.doku.com'.")