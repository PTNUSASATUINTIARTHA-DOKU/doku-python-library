from doku_python_library.src.commons.config import Config
import unittest
from unittest.mock import patch, Mock, MagicMock
from util import Util
import requests

class TestDeleteVa(unittest.TestCase):

    def setUp(self) -> None:
        self.delete_va_url = "/virtual-accounts/bi-snap-va/v1.1/transfer-va/delete-va"
    
    @patch('requests.delete')
    def test_delete_va_success_bca(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_delete_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_delete_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BCA"
        response = requests.delete(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.delete')
    def test_delete_va_success_mandiri(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_delete_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_delete_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BANK_MANDIRI"
        response = requests.delete(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.delete')
    def test_delete_va_success_bri(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_delete_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_delete_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BRI"
        response = requests.delete(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.delete')
    def test_delete_va_success_bni(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_delete_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_delete_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BNI"
        response = requests.delete(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.delete')
    def test_delete_va_success_danamon(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_delete_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_delete_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BANK_DANAMON"
        response = requests.delete(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.delete')
    def test_delete_va_success_permata(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_delete_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_delete_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BANK_PERMATA"
        response = requests.delete(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.delete')
    def test_delete_va_success_maybank(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_delete_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_delete_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_MAYBANK"
        response = requests.delete(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.delete')
    def test_delete_va_success_bnc(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_delete_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_delete_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BNC"
        response = requests.delete(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
        
    @patch('requests.delete')
    def test_delete_va_success_btn(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_delete_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_delete_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BTN"
        response = requests.delete(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.delete')
    def test_delete_va_success_bsi(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_delete_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_delete_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BSI"
        response = requests.delete(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.delete')
    def test_delete_va_success_cimb(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_delete_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_delete_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BANK_CIMB"
        response = requests.delete(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.delete')
    def test_delete_va_success_sinarmas(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_delete_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_delete_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_SINARMAS"
        response = requests.delete(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)

    @patch('requests.delete')
    def test_delete_va_success_doku(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_delete_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_delete_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_DOKU"
        response = requests.delete(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.delete')
    def test_delete_va_success_bss(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_delete_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_delete_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BSS"
        response = requests.delete(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.delete_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)

    def test_delete_va_partner_service_id_null(self):
        request = Util.generate_delete_va_request()
        request.partner_service_id = None
        with self.assertRaises(Exception) as context:
            request.validate_delete_request()
        self.assertEqual(str(context.exception.args[0]), "partnerServiceId cannot be null. Please provide a partnerServiceId. Example: ' 888994'.")
    
    def test_delete_va_partner_service_id_not_valid_length(self):
        request = Util.generate_delete_va_request()
        request.partner_service_id = "1234"
        with self.assertRaises(Exception) as context:
            request.validate_delete_request()
        self.assertEqual(str(context.exception.args[0]), "partnerServiceId must be exactly 8 characters long and equiped with left-padded spaces. Example: ' 888994'.")

    def test_delete_va_partner_service_id_not_valid_format(self):
        request = Util.generate_delete_va_request()
        request.partner_service_id = "    890E"
        with self.assertRaises(Exception) as context:
            request.validate_delete_request()
        self.assertEqual(str(context.exception.args[0]), "partnerServiceId must consist of up to 8 digits of character. Remaining space in case of partner serivce id is less than 8 must be filled with spaces. Example: ' 888994' (2 spaces and 6 digits).")

    def test_delete_va_customer_no_null(self):
        request = Util.generate_delete_va_request()
        request.customer_no = None
        with self.assertRaises(Exception) as context:
            request.validate_delete_request()
        self.assertEqual(str(context.exception.args[0]), "customerNo must be a string. Ensure that customerNo is enclosed in quotes. Example: '00000000000000000001'.")

    def test_delete_va_customer_no_not_valid_length(self):
        request = Util.generate_delete_va_request()
        request.customer_no = "1234567890123456789011"
        with self.assertRaises(Exception) as context:
            request.validate_delete_request()
        self.assertEqual(str(context.exception.args[0]), "customerNo must be 20 characters or fewer. Ensure that customerNo is no longer than 20 characters. Example: '00000000000000000001'.")
    
    def test_delete_va_customer_no_not_valid_format(self):
        request = Util.generate_delete_va_request()
        request.customer_no = "1234567890123456789E"
        with self.assertRaises(Exception) as context:
            request.validate_delete_request()
        self.assertEqual(str(context.exception.args[0]), "customerNo must consist of only digits. Ensure that customerNo contains only numbers. Example: '00000000000000000001'.")

    def test_delete_va_virtual_acc_no_not_valid_format(self):
        request = Util.generate_delete_va_request()
        request.virtual_account_no = "TEST123"
        self.assertTrue(request.virtual_account_no != request.partner_service_id+request.customer_no, "virtualAccountNo is not partnerServiceId + customerNo")

    def test_delete_va_trx_id_null(self):
        request = Util.generate_delete_va_request()
        request.trx_id = None
        with self.assertRaises(Exception) as context:
            request.validate_delete_request()
        self.assertEqual(str(context.exception.args[0]), "trxId cannot be null. Please provide a trxId. Example: '23219829713'.")

    def test_delete_va_trx_id_not_valid_length_min(self):
        request = Util.generate_delete_va_request()
        request.trx_id = ""
        with self.assertRaises(Exception) as context:
            request.validate_delete_request()
        self.assertEqual(str(context.exception.args[0]), "trxId must be at least 1 character long. Ensure that trxId is not empty. Example: '23219829713'.")
    
    def test_delete_va_trx_id_not_valid_length_max(self):
        request = Util.generate_delete_va_request()
        request.trx_id = "ImCyDjTlTqJu9Rrq1uSuKxNNqcNdcD8EuXigmUMZsge3fvkSOyZ8FwMfyDGeOXxaDENzXzHrnXTfHIqXaKLz5Uq7zaGkjNL0DiTRn7vnBEigFFkJlhftfqiT2ml82pYI1ZUmuuR3N1zaAQNYZvg3asANmoDVGmJYnMdGTyWtD3PPb2t8Nwm57Qd1BfSZIiC7A4cGFSyzYZNp2ObxP4zUeMoa0TPV2WbnLKJ761qP594vMXt9Om4pzdcwK3aAWHQd"
        with self.assertRaises(Exception) as context:
            request.validate_delete_request()
        self.assertEqual(str(context.exception.args[0]), "trxId must be 64 characters or fewer. Ensure that trxId is no longer than 64 characters. Example: '23219829713'.")

    def test_delete_va_channel_length_min(self):
        request = Util.generate_delete_va_request()
        request.additional_info.channel = ""
        with self.assertRaises(Exception) as context:
            request.validate_delete_request()
        self.assertEqual(str(context.exception.args[0]), "additionalInfo.channel must be at least 1 character long. Ensure that additionalInfo.channel is not empty. Example: 'VIRTUAL_ACCOUNT_MANDIRI'.")
    
    def test_delete_va_channel_length_max(self):
        request = Util.generate_delete_va_request()
        request.additional_info.channel = "ImCyDjTlTqJu9Rrq1uSuKxNNqcNdcD8EuXigmUMZsge3fvkSOyZ8FwMfyDGeOXxaDENzXzHrnXTfHIqXaKLz5Uq7zaGkjNL0DiTRn7vnBEigFFkJlhftfqiT2ml82pYI1ZUmuuR3N1zaAQNYZvg3asANmoDVGmJYnMdGTyWtD3PPb2t8Nwm57Qd1BfSZIiC7A4cGFSyzYZNp2ObxP4zUeMoa0TPV2WbnLKJ761qP594vMXt9Om4pzdcwK3aAWHQd"
        with self.assertRaises(Exception) as context:
            request.validate_delete_request()
        self.assertEqual(str(context.exception.args[0]), "additionalInfo.channel must be 30 characters or fewer. Ensure that additionalInfo.channel is no longer than 30 characters. Example: 'VIRTUAL_ACCOUNT_MANDIRI'.")
    
    def test_delete_va_channel_length_enum(self):
        request = Util.generate_delete_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_CUSTOM"
        with self.assertRaises(Exception) as context:
            request.validate_delete_request()
        self.assertEqual(str(context.exception.args[0]), "additionalInfo.channel is not valid. Ensure that additionalInfo.channel is one of the valid channels. Example: 'VIRTUAL_ACCOUNT_MANDIRI'.")


if __name__ == "__main__":
    unittest.main()