
Welcome to the DOKU Python library! This powerful tool simplifies access to the DOKU API for your server-side Python applications.

## Documentation
For detailed information, visit the full [DOKU API Docs](https://developers.doku.com/accept-payment/direct-api/snap).

## Requirements
- Python 3.8 or higher

## Installation
Get started by installing the library:
```sh
pip3 install doku_python_library
```

## Usage
This section will guide you through setting up the DOKU Python library, creating payment requests, and handling notifications. Let’s get started!

### 1. Configuration
To configure the library, you'll need your account's Client ID, Secret Key, and Private Key. Here’s how:

1. **Client ID and Secret Key:** Retrieve these from the Integration menu in your [DOKU Dashboard](https://dashboard.doku.com/bo/login).
2. **Private Key:** Generate your Private Key following DOKU’s guide and insert the corresponding Public Key into the same menu.

> [!info]
> Your private key will not be transmitted or shared with DOKU. It remains on your server and is only used to sign the requests you send to DOKU.

```python
payment: DokuSNAP = DokuSNAP(
    private_key= private_key, 
    client_id="your_client_id", 
    is_production=False,
    public_key= "your_public_key",
    issuer= "your_issuer_data",
    secret_key="your_secret_key"
    )
```

### 2. Payment Flow
This section guides you through the steps to process payments using the DOKU Python library. You'll learn how to create a payment request and call the payment function.
#### a. Virtual Account
DOKU offers three ways to use a virtual account: DOKU-Generated Payment Code (DGPC), Merchant-Generated Payment Code (MGPC), and Direct Inquiry Payment Code (DIPC). You can find the full details [here](https://developers.doku.com/accept-payment/direct-api/snap/integration-guide/virtual-account).

> [!Important!]
>Each transaction can use only one feature at a time, but you can use multiple features across different transactions.

##### DGPC and MGPC
###### CreateVARequest Object
Create the request object to generate a VA number. Specify the acquirer in the request object. This function is applicable for DGPC and MGPC.

```python
request: CreateVARequest = CreateVARequest(
    partner_service_id= "    1899",
    virtual_acc_name= "Toru Yamashitas",
    trx_id= TokenService.get_timestamp(),
    virtual_acc_trx_type= "C",
    total_amount= TotalAmount(value="150000.00", currency="IDR"),
    additional_info= AdditionalInfo(channel="VIRTUAL_ACCOUNT_BANK_CIMB", virtual_account_config= VirtualAccountConfig(
        reusable_status=False,
        )),
    expired_date="2025-07-11T10:55:00+07:00",
    customer_no="20240715001",
    virtual_account_no="    189920240715001"
)
```

###### create_va Function
Call the `create_va` function to request the paycode from DOKU. You’ll receive the paycode and payment instructions to display to your customers. This function is applicable for DGPC and MGPC.

```python
response: CreateVAResponse = payment.create_va(create_va_request= request)
```

##### DIPC
###### #coming-soon inquiryResponse Function
If you use the DIPC feature, you can generate your own paycode and allow your customers to pay without direct communication with DOKU. After customers initiate the payment via the acquirer's channel, DOKU sends an inquiry request to you for validation. This function is applicable for DIPC.
```python
@app.route('/v1.1/transfer-va/inquiry', methods=['POST'])
def inquiry_request() -> dict:
    try:
        header: dict = dict(request.headers)
        request_json: dict = request.get_json()
        is_token_valid: bool = snap.validate_token_b2b(request_token=header["Authorization"])
        if is_token_valid:
            request_body = request.get_json()
            status = insert_direct_inquiry_info(
                request_inquiry_request_id=request_body["inquiryRequestId"],
                request_inquiry_body=json.dumps(request_body),
                request_inquiry_header=json.dumps(dict(request.headers)),
                prog_language="python",
                versi_sdk="1.1.0"
            )
            row = fetch_direct_inquiry(inquiry_id=request_json['inquiryRequestId'])
            response_body = row[2]
            if not isinstance(row, str):
                response: InquiryResponseBody = InquiryResponseBody(
                    responseCode="2002400",
                    responseMessage="successful",
                    virtualAccountData=InquiryRequestVirtualAccountData(
                        partnerServiceId=None if "partnerServiceId" not in response_body.keys() else response_body["partnerServiceId"],
                        customerNo=None if "customerNo" not in response_body.keys() else response_body["customerNo"],
                        virtualAccountNo=None if "virtualAccountNo" not in response_body.keys() else response_body["virtualAccountNo"],
                        virtualAccountName=None if "virtualAccountName" not in response_body.keys() else response_body["virtualAccountName"],
                        virtualAccountEmail=None if "virtualAccountEmail" not in response_body.keys() else response_body["virtualAccountEmail"],
                        virtualAccountPhone=None if "virtualAccountPhone" not in response_body.keys() else response_body["virtualAccountPhone"],
                        totalAmount=TotalAmount(
                            value=None if response_body["totalAmount"]["value"] is None else response_body["totalAmount"]["value"],
                            currency=None if response_body["totalAmount"]["currency"] is None else response_body["totalAmount"]["currency"],
                        ),
                        virtualAccountTrxType=None if "virtualAccountTrxType" not in response_body.keys() else response_body["virtualAccountTrxType"],
                        expiredDate=None if "expiredDate" not in response_body.keys() else response_body["expiredDate"],
                        additionalInfo=InquiryRequestAdditionalInfo(
                            channel=None if response_body["additionalInfo"]["channel"] is None else response_body["additionalInfo"]["channel"],
                            trxId=None if response_body["additionalInfo"]["trxId"] is None else response_body["additionalInfo"]["trxId"],
                            virtualAccountConfig= VirtualAccountConfig(
                                reusable_status=None if response_body["additionalInfo"]["virtualAccountConfig"]["reusableStatus"] is None else response_body["additionalInfo"]["virtualAccountConfig"]["reusableStatus"],
                                min_amount=None if response_body["additionalInfo"]["virtualAccountConfig"]["minAmount"] is None else response_body["additionalInfo"]["virtualAccountConfig"]["minAmount"],
                                max_amount=None if response_body["additionalInfo"]["virtualAccountConfig"]["maxAmount"] is None else response_body["additionalInfo"]["virtualAccountConfig"]["maxAmount"],
                            )
                        ),
                        inquiryReason=InquiryReason(
                            english=None if response_body["inquiryReason"]["english"] is None else response_body["inquiryReason"]["english"],
                            indonesia=None if response_body["inquiryReason"]["indonesia"] is None else response_body["inquiryReason"]["indonesia"],
                        ),
                        inquiryRequestId=None if "inquiryRequestId" not in response_body.keys() else response_body["inquiryRequestId"],
                        inquiryStatus=None if "inquiryStatus" not in response_body.keys() else response_body["inquiryStatus"],
                        trxId=None if "trxId" not in response_body.keys() else response_body["trxId"],
                    )
                )
                response = response.json()
                return json.dumps(response)
            else:
                return {
                    "responseCode": "4012400",
                    "responseMessage": "Virtual Account Not Found",
                    }
        return {
                "responseCode": "4010000",
                "responseMessage": "Invalid Token (B2B)",
            }
    except Exception as e:
        return {"error": str(e)}
```

> [!Important!]
>Before sending the inquiry, DOKU sends a token request. Use the `generateToken` function found in the Handling Payment Notification section.

### 3. Handling Payment Notification
After your customers make a payment, you’ll receive a notification from DOKU to update the payment status on your end. DOKU first sends a token request (as with DIPC), then uses that token to send the payment notification.
##### validate_signature_and_generate_token function
Generate the response to DOKU, including the required token, by calling this function.
```python
notification_token: NotificationToken = payment.validate_signature_and_generate_token()
```

##### validate_token_and_generate_notification_response function
Deserialize the raw notification data into a structured object using a Data Transfer Object (DTO). This allows you to update the order status, notify customers, or perform other necessary actions based on the notification details.
```python
response: PaymentNotificationResponseBody = payment.validate_token_and_generate_notification_response(
        header= RequestHeader(
            x_timestamp=header['X-Timestamp'],
            authorization= header['Authorization'],
            x_external_id=header['X-External-Id'],
            x_partner_id=header['X-Client-Key'],
            x_signature=header['X-Signature'],
        ), 
        request=PaymentNotificationRequest(**request.get_json())
    )
```

##### generate_notification_response function
DOKU requires a response to the notification. Use this function to serialize the response data to match DOKU’s format.
```python
response: PaymentNotificationResponseBody = payment.generate_notification_response(
        is_token_valid=is_token_valid
        request=PaymentNotificationRequest(**request.get_json())
    )
```

### 4. Additional Features
Need to use our functions independently? No problem! Here’s how:
#### - v1 to SNAP converter
If you're one of our earliest users, you might still use our v1 APIs. In order to simplify your re-integration process to DOKU's SNAP API specification, DOKU provides you with a helper tools to directly convert v1 APIs to SNAP APIs specification
##### a. convertRequestV1
Convert DOKU's inquiry and notification from SNAP format (JSON) to v1 format (XML). Feed the inquiry and notification directly to your app without manually mapping parameters or converting file formats.
```python
form_data: dict = payment.direct_inquiry_request_mapping(header=dict(request.headers()), snap_format=request.get_json())
```
##### b. convertResponseV1
Convert your inquiry response to DOKU from v1 format (XML) to SNAP format (JSON). Our library handles response code mapping, allowing you to directly use the converted response and send it to DOKU.
```python
json_format: dict = payment.direct_inquiry_response_mapping(v1_data=xml)
# xml string format
```