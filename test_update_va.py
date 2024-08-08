from doku_python_library.src.commons.config import Config
import unittest
from unittest.mock import patch, Mock, MagicMock
from util import Util
import requests

class TestUpdateVa(unittest.TestCase):

    def setUp(self) -> None:
        self.update_va_url = "/virtual-accounts/bi-snap-va/v1.1/transfer-va/update-va"
    
    @patch('requests.put')
    def test_update_va_success_bca(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_update_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_update_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BCA"
        response = requests.put(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.put')
    def test_update_va_success_mandiri(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_update_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_update_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BANK_MANDIRI"
        response = requests.put(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.put')
    def test_update_va_success_bri(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_update_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_update_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BRI"
        response = requests.put(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.put')
    def test_update_va_success_bni(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_update_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_update_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BNI"
        response = requests.put(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.put')
    def test_update_va_success_danamon(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_update_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_update_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BANK_DANAMON"
        response = requests.put(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.put')
    def test_update_va_success_permata(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_update_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_update_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BANK_PERMATA"
        response = requests.put(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.put')
    def test_update_va_success_maybank(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_update_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_update_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_MAYBANK"
        response = requests.put(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.put')
    def test_update_va_success_bnc(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_update_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_update_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BNC"
        response = requests.put(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
        
    @patch('requests.put')
    def test_update_va_success_btn(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_update_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_update_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BTN"
        response = requests.put(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.put')
    def test_update_va_success_bsi(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_update_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_update_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BSI"
        response = requests.put(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.put')
    def test_update_va_success_cimb(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_update_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_update_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BANK_CIMB"
        response = requests.put(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.put')
    def test_update_va_success_sinarmas(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_update_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_update_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_SINARMAS"
        response = requests.put(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)

    @patch('requests.put')
    def test_update_va_success_doku(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_update_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_update_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_DOKU"
        response = requests.put(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    @patch('requests.put')
    def test_update_va_success_bss(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_update_va_response(response_code="2002700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_update_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_BSS"
        response = requests.put(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())

        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.update_va_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)

    def test_update_va_partner_service_id_null(self):
        request = Util.generate_update_va_request()
        request.partner_service_id = None
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "partnerServiceId cannot be null. Please provide a partnerServiceId. Example: ' 888994'.")
    
    def test_update_va_partner_service_id_not_valid_length(self):
        request = Util.generate_update_va_request()
        request.partner_service_id = "1234"
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "partnerServiceId must be exactly 8 characters long and equiped with left-padded spaces. Example: ' 888994'.")

    def test_update_va_partner_service_id_not_valid_format(self):
        request = Util.generate_update_va_request()
        request.partner_service_id = "    890E"
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "partnerServiceId must consist of up to 8 digits of character. Remaining space in case of partner serivce id is less than 8 must be filled with spaces. Example: ' 888994' (2 spaces and 6 digits).")
    
    def test_update_va_customer_no_null(self):
        request = Util.generate_update_va_request()
        request.customer_no = None
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "customerNo must be a string. Ensure that customerNo is enclosed in quotes. Example: '00000000000000000001'.")

    def test_update_va_customer_no_not_valid_length(self):
        request = Util.generate_update_va_request()
        request.customer_no = "1234567890123456789011"
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "customerNo must be 20 characters or fewer. Ensure that customerNo is no longer than 20 characters. Example: '00000000000000000001'.")
    
    def test_update_va_customer_no_not_valid_format(self):
        request = Util.generate_update_va_request()
        request.customer_no = "1234567890123456789E"
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "customerNo must consist of only digits. Ensure that customerNo contains only numbers. Example: '00000000000000000001'.")

    def test_update_va_virtual_acc_no_not_valid_format(self):
        request = Util.generate_update_va_request()
        request.virtual_account_no = "TEST123"
        self.assertTrue(request.virtual_account_no != request.partner_service_id+request.customer_no, "virtualAccountNo is not partnerServiceId + customerNo")
    
    def test_update_va_virtual_acc_name_not_valid_length_min(self):
        request = Util.generate_update_va_request()
        request.virtual_acc_name = ""
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "virtualAccountName must be at least 1 character long. Ensure that virtualAccountName is not empty. Example: 'Toru Yamashita'.")
    
    def test_update_va_virtual_acc_name_not_valid_length_max(self):
        request = Util.generate_update_va_request()
        request.virtual_acc_name = "ImCyDjTlTqJu9Rrq1uSuKxNNqcNdcD8EuXigmUMZsge3fvkSOyZ8FwMfyDGeOXxaDENzXzHrnXTfHIqXaKLz5Uq7zaGkjNL0DiTRn7vnBEigFFkJlhftfqiT2ml82pYI1ZUmuuR3N1zaAQNYZvg3asANmoDVGmJYnMdGTyWtD3PPb2t8Nwm57Qd1BfSZIiC7A4cGFSyzYZNp2ObxP4zUeMoa0TPV2WbnLKJ761qP594vMXt9Om4pzdcwK3aAWHQd"
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "virtualAccountName must be 255 characters or fewer. Ensure that virtualAccountName is no longer than 255 characters. Example: 'Toru Yamashita'.")
    
    def test_update_va_virtual_acc_name_not_valid_char(self):
        request = Util.generate_update_va_request()
        request.virtual_acc_name = "$%%^$"
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "virtualAccountName can only contain letters, numbers, spaces, and the following characters: .\-/+,=_:'@%. Ensure that virtualAccountName does not contain invalid characters. Example: 'Toru.Yamashita-123'.")
    
    def test_update_va_virtual_acc_email_not_valid_length_min(self):
        request = Util.generate_update_va_request()
        request.virtual_acc_email = ""
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "virtualAccountEmail must be at least 1 character long. Ensure that virtualAccountEmail is not empty. Example: 'toru@example.com'.")
    
    def test_update_va_virtual_acc_email_not_valid_length_max(self):
        request = Util.generate_update_va_request()
        request.virtual_acc_email = "ImCyDjTlTqJu9Rrq1uSuKxNNqcNdcD8EuXigmUMZsge3fvkSOyZ8FwMfyDGeOXxaDENzXzHrnXTfHIqXaKLz5Uq7zaGkjNL0DiTRn7vnBEigFFkJlhftfqiT2ml82pYI1ZUmuuR3N1zaAQNYZvg3asANmoDVGmJYnMdGTyWtD3PPb2t8Nwm57Qd1BfSZIiC7A4cGFSyzYZNp2ObxP4zUeMoa0TPV2WbnLKJ761qP594vMXt9Om4pzdcwK3aAWHQd"
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "virtualAccountEmail must be 255 characters or fewer. Ensure that virtualAccountEmail is no longer than 255 characters. Example: 'toru@example.com'.")
    
    def test_update_va_virtual_acc_email_not_valid_format(self):
        request = Util.generate_update_va_request()
        request.virtual_acc_email = "user"
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "virtualAccountEmail is not in a valid email format. Ensure it contains an '@' symbol followed by a domain name. Example: 'toru@example.com'.")

    def test_update_va_virtual_acc_phone_not_valid_length_min(self):
        request = Util.generate_update_va_request()
        request.virtual_acc_phone = "0812"
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "virtualAccountPhone must be at least 9 characters long. Ensure that virtualAccountPhone is at least 9 characters long. Example: '628123456789'.")
    
    def test_update_va_virtual_acc_phone_not_valid_length_max(self):
        request = Util.generate_update_va_request()
        request.virtual_acc_phone = "ImCyDjTlTqJu9Rrq1uSuKxNNqcNdcD8EuXigmUMZsge3fvkSOyZ8FwMfyDGeOXxaDENzXzHrnXTfHIqXaKLz5Uq7zaGkjNL0DiTRn7vnBEigFFkJlhftfqiT2ml82pYI1ZUmuuR3N1zaAQNYZvg3asANmoDVGmJYnMdGTyWtD3PPb2t8Nwm57Qd1BfSZIiC7A4cGFSyzYZNp2ObxP4zUeMoa0TPV2WbnLKJ761qP594vMXt9Om4pzdcwK3aAWHQd"
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "virtualAccountPhone must be 30 characters or fewer. Ensure that virtualAccountPhone is no longer than 30 characters. Example: '628123456789012345678901234567'.")

    def test_update_va_trx_id_null(self):
        request = Util.generate_update_va_request()
        request.trx_id = None
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "trxId cannot be null. Please provide a trxId. Example: '23219829713'.")

    def test_update_va_trx_id_not_valid_length_min(self):
        request = Util.generate_update_va_request()
        request.trx_id = ""
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "trxId must be at least 1 character long. Ensure that trxId is not empty. Example: '23219829713'.")
    
    def test_update_va_trx_id_not_valid_length_max(self):
        request = Util.generate_update_va_request()
        request.trx_id = "ImCyDjTlTqJu9Rrq1uSuKxNNqcNdcD8EuXigmUMZsge3fvkSOyZ8FwMfyDGeOXxaDENzXzHrnXTfHIqXaKLz5Uq7zaGkjNL0DiTRn7vnBEigFFkJlhftfqiT2ml82pYI1ZUmuuR3N1zaAQNYZvg3asANmoDVGmJYnMdGTyWtD3PPb2t8Nwm57Qd1BfSZIiC7A4cGFSyzYZNp2ObxP4zUeMoa0TPV2WbnLKJ761qP594vMXt9Om4pzdcwK3aAWHQd"
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "trxId must be 64 characters or fewer. Ensure that trxId is no longer than 64 characters. Example: '23219829713'.")

    def test_update_va_total_amount_value_length_min(self):
        request = Util.generate_update_va_request()
        request.total_amount.value = ""
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "totalAmount.value must be at least 4 characters long and formatted as 0.00. Ensure that totalAmount.value is at least 4 characters long and in the correct format. Example: '100.00'.")
    
    def test_update_va_total_amount_value_length_max(self):
        request = Util.generate_update_va_request()
        request.total_amount.value = "ImCyDjTlTqJu9Rrq1uSuKxNNqcNdcD8EuXigmUMZsge3fvkSOyZ8FwMfyDGeOXxaDENzXzHrnXTfHIqXaKLz5Uq7zaGkjNL0DiTRn7vnBEigFFkJlhftfqiT2ml82pYI1ZUmuuR3N1zaAQNYZvg3asANmoDVGmJYnMdGTyWtD3PPb2t8Nwm57Qd1BfSZIiC7A4cGFSyzYZNp2ObxP4zUeMoa0TPV2WbnLKJ761qP594vMXt9Om4pzdcwK3aAWHQd"
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "totalAmount.value must be 19 characters or fewer and formatted as 9999999999999999.99. Ensure that totalAmount.value is no longer than 19 characters and in the correct format. Example: '9999999999999999.99'.")

    def test_update_va_total_amount_currency_length_min(self):
        request = Util.generate_update_va_request()
        request.total_amount.currency = "ID"
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "totalAmount.currency must be exactly 3 characters long. Ensure that totalAmount.currency is exactly 3 characters. Example: 'IDR'.")
    
    def test_update_va_total_amount_currency_not_idr(self):
        request = Util.generate_update_va_request()
        request.total_amount.currency = "INR"
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "totalAmount.currency must be 'IDR'. Ensure that totalAmount.currency is 'IDR'. Example: 'IDR'.")

    def test_update_va_channel_length_min(self):
        request = Util.generate_update_va_request()
        request.additional_info.channel = ""
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "additionalInfo.channel must be at least 1 character long. Ensure that additionalInfo.channel is not empty. Example: 'VIRTUAL_ACCOUNT_MANDIRI'.")
    
    def test_update_va_channel_length_max(self):
        request = Util.generate_update_va_request()
        request.additional_info.channel = "ImCyDjTlTqJu9Rrq1uSuKxNNqcNdcD8EuXigmUMZsge3fvkSOyZ8FwMfyDGeOXxaDENzXzHrnXTfHIqXaKLz5Uq7zaGkjNL0DiTRn7vnBEigFFkJlhftfqiT2ml82pYI1ZUmuuR3N1zaAQNYZvg3asANmoDVGmJYnMdGTyWtD3PPb2t8Nwm57Qd1BfSZIiC7A4cGFSyzYZNp2ObxP4zUeMoa0TPV2WbnLKJ761qP594vMXt9Om4pzdcwK3aAWHQd"
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "additionalInfo.channel must be 30 characters or fewer. Ensure that additionalInfo.channel is no longer than 30 characters. Example: 'VIRTUAL_ACCOUNT_MANDIRI'.")
    
    def test_update_va_channel_length_max(self):
        request = Util.generate_update_va_request()
        request.additional_info.channel = "VIRTUAL_ACCOUNT_CUSTOM"
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "additionalInfo.channel is not valid. Ensure that additionalInfo.channel is one of the valid channels. Example: 'VIRTUAL_ACCOUNT_MANDIRI'.")
        
    def test_update_va_trx_type_length_min(self):
        request = Util.generate_update_va_request()
        request.virtual_acc_trx_type = ""
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "virtualAccountTrxType must be exactly 1 character long. Ensure that virtualAccountTrxType is either 'V' or 'O' and 'C. Example: 'C'.")
    
    def test_update_va_trx_type_enum(self):
        request = Util.generate_update_va_request()
        request.virtual_acc_trx_type = "I"
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "virtualAccountTrxType must be either 'V' or 'C' and 'O. Ensure that virtualAccountTrxType is one of these values. Example: 'C'.")

    def test_update_va_expired_date_format(self):
        request = Util.generate_update_va_request()
        request.expired_date = ""
        with self.assertRaises(Exception) as context:
            request.validate_update_va_request()
        self.assertEqual(str(context.exception.args[0]), "expiredDate must be in ISO-8601 format. Ensure that expiredDate follows the correct format. Example: '2023-01-01T10:55:00+07:00'.")
    
if __name__ == "__main__":
    unittest.main()