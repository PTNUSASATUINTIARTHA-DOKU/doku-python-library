# DOKU Python SDK Documentation

## Introduction
Welcome to the DOKU Python SDK! This SDK simplifies access to the DOKU API for your Python applications, enabling seamless integration with payment and virtual account services.

If your looking for another language  [Node.js](https://github.com/PTNUSASATUINTIARTHA-DOKU/doku-nodejs-library), [PHP](https://github.com/PTNUSASATUINTIARTHA-DOKU/doku-php-library), [Go](https://github.com/PTNUSASATUINTIARTHA-DOKU/doku-golang-library), [Java](https://github.com/PTNUSASATUINTIARTHA-DOKU/doku-java-library)

## Table of Contents
- [DOKU Python SDK Documentation](#doku-python-sdk-documentation)
  - [1. Getting Started](#1-getting-started)
  - [2. Usage](#2-usage)
    - [Virtual Account](#virtual-account)
      - [I. Virtual Account (DGPC \& MGPC)](#i-virtual-account-dgpc--mgpc)
      - [II. Virtual Account (DIPC)](#ii-virtual-account-dipc)
      - [III. Check Virtual Account Status](#iii-check-virtual-account-status)
    - [B. Binding / Registration Operations](#b-binding--registration-operations)
      - [I. Account Binding](#i-account-binding)
      - [II. Card Registration](#ii-card-registration)
    - [C. Direct Debit and E-Wallet](#c-direct-debit-and-e-wallet)
      - [I. Request Payment](#i-request-payment)
      - [II. Request Payment Jump App](#ii-request-payment-jump-app)
  - [3. Other Operation](#3-other-operation)
    - [Check Transaction Status](#a-check-transaction-status)
    - [Refund](#b-refund)
    - [Balance Inquiry](#c-balance-inquiry)
  - [4. Error Handling and Troubleshooting](#4-error-handling-and-troubleshooting)




## 1. Getting Started

### Requirements
- Python 3.8 or higher

### Installation
To install the DOKU Snap SDK, use Python:
```bash
pip3 install doku_python_library
```

### Configuration
Before using the Doku Snap SDK, you need to initialize it with your credentials:
1. **Client ID**, **Secret Key** and **DOKU Public Key**: Retrieve these from the Integration menu in your Doku Dashboard
2. **Private Key** and **Public Key** : Generate your Private Key and Public Key

Merchant privateKey and publiKey
How to generate :
1. generate private key RSA : openssl genrsa -out private.key 2048
2. set passphrase your private key RSA : openssl pkcs8 -topk8 -inform PEM -outform PEM -in private.key -out pkcs8.key -v1 PBE-SHA1-3DES
3. generate public key RSA : openssl rsa -in private.key -outform PEM -pubout -out public.pem

The encryption model applied to messages involves both asymmetric and symmetric encryption, utilizing a combination of Private Key and Public Key, adhering to the following standards:

  1. Standard Asymmetric Encryption Signature: SHA256withRSA dengan Private Key ( Kpriv ) dan Public Key ( Kpub ) (256 bits)
  2. Standard Symmetric Encryption Signature HMAC_SHA512 (512 bits)
  3. Standard Symmetric Encryption AES-256 dengan client secret sebagai encryption key.

| **Parameter**       | **Description**                                    | **Required** |
|-----------------|----------------------------------------------------|--------------|
| `privateKey`    | The private key for the partner service.           | ✅          |
| `publicKey`     | The public key for the partner service.            | ✅           |
| `clientId`      | The client ID associated with the service.         | ✅           |
| `secretKey`     | The secret key for the partner service.            | ✅           |
| `isProduction`  | Set to true for production environment             | ✅           |
| `dokuPublicKey` | Key that merchants use to verify DOKU request      | ✅           |
| `issuer`        | Optional issuer for advanced configurations.       | ❌           |
| `authCode`      | Optional authorization code for advanced use.      | ❌           |


```python
from doku_python_library.src.snap import DokuSNAP

snap: DokuSNAP = DokuSNAP(
    private_key= private_key, 
    client_id="your_client_id", 
    is_production=False,
    public_key= "doku_public_key",
    issuer= "your_issuer_data",
    secret_key="your_secret_key",
    merchant_public_key= "your_public_key"
)
```

## 2. Usage

**Initialization**
Always start by initializing the Snap object.

```python
snap: DokuSNAP = DokuSNAP(
    private_key= private_key, 
    client_id="your_client_id", 
    is_production=False,
    public_key= "doku_public_key",
    issuer= "your_issuer_data",
    secret_key="your_secret_key",
    merchant_public_key= "your_public_key"
)
```
### Virtual Account
#### I. Virtual Account (DGPC & MGPC)
##### DGPC
- **Description:** A pre-generated virtual account provided by DOKU.
- **Use Case:** Recommended for one-time transactions.
##### MGPC
- **Description:** Merchant generated virtual account.
- **Use Case:** Recommended for top up business model.

Parameters for **createVA** and **updateVA**
<table>
  <thead>
    <tr>
      <th><strong>Parameter</strong></th>
      <th colspan="2"><strong>Description</strong></th>
      <th><strong>Data Type</strong></th>
      <th><strong>Required</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>partnerServiceId</code></td>
      <td colspan="2">The unique identifier for the partner service.</td>
      <td>String(20)</td>
      <td>✅</td>
    </tr>
    <tr>
      <td><code>customerNo</code></td>
      <td colspan="2">The customer's identification number.</td>
      <td>String(20)</td>
      <td>✅</td>
    </tr>
    <tr>
      <td><code>virtualAccountNo</code></td>
      <td colspan="2">The virtual account number associated with the customer.</td>
      <td>String(20)</td>
      <td>✅</td>
    </tr>
    <tr>
      <td><code>virtualAccountName</code></td>
      <td colspan="2">The name of the virtual account associated with the customer.</td>
      <td>String(255)</td>
      <td>✅</td>
    </tr>
    <tr>
      <td><code>virtualAccountEmail</code></td>
      <td colspan="2">The email address associated with the virtual account.</td>
      <td>String(255)</td>
      <td>❌</td>
    </tr>
    <tr>
      <td><code>virtualAccountPhone</code></td>
      <td colspan="2">The phone number associated with the virtual account.</td>
      <td>String(9-30)</td>
      <td>❌</td>
    </tr>
    <tr>
      <td><code>trxId</code></td>
      <td colspan="2">Invoice number in Merchants system.</td>
      <td>String(64)</td>
      <td>✅</td>
    </tr>
    <tr>
      <td rowspan="2"><code>totalAmount</code></td>
      <td colspan="2"><code>value</code>: Transaction Amount (ISO 4217) <br> <small>Example: "11500.00"</small></td>
      <td>String(16.2)</td>
      <td>✅</td>
    </tr>
    <tr>
      <td colspan="2"><code>Currency</code>: Currency <br> <small>Example: "IDR"</small></td>
      <td>String(3)</td>
      <td>✅</td>
    </tr>
    <tr>
      <td rowspan="4"><code>additionalInfo</code></td>
      <td colspan="2"><code>channel</code>: Channel that will be applied for this VA <br> <small>Example: VIRTUAL_ACCOUNT_BANK_CIMB</small></td>
      <td>String(20)</td>
      <td>✅</td>
    </tr>
    <tr>
      <td rowspan="3"><code>virtualAccountConfig</code></td>
      <td><code>reusableStatus</code>: Reusable Status For Virtual Account Transaction <br><small>value TRUE or FALSE</small></td>
      <td>Boolean</td>
      <td>❌</td>
    </tr>
    <tr>
      <td><code>minAmount</code>: Minimum Amount can be used only if <code>virtualAccountTrxType</code> is Open Amount (O). <br><small>Example: "10000.00"</small></td>
      <td>String(16.2)</td>
      <td>❌</td>
    </tr>
    <tr>
      <td><code>maxAmount</code>: Maximum Amount can be used only if <code>virtualAccountTrxType</code> is Open Amount (O). <br><small>Example: "5000000.00"</small></td>
      <td>String(16.2)</td>
      <td>❌</td>
    </tr>
    <tr>
      <td><code>virtualAccountTrxType</code></td>
      <td colspan="2">Transaction type for this transaction. C (Closed Amount), O (Open Amount)</td>
      <td>String(1)</td>
      <td>✅</td>
    </tr>
    <tr>
      <td><code>expiredDate</code></td>
      <td colspan="2">Expiration date for Virtual Account. ISO-8601 <br><small>Example: "2023-01-01T10:55:00+07:00"</small></td>
      <td>String</td>
      <td>❌</td>
    </tr>
  </tbody>
</table>


1. **Create Virtual Account**
    - **Function:** `createVa`
    ```python
    from doku_python_library.src.model.va.create_va_request import CreateVARequest
    from doku_python_library.src.model.va.create_va_response import CreateVAResponse
    
    request: CreateVARequest = CreateVARequest(
      partner_service_id="8129014",
      virtual_acc_name="Test Example",
      trx_id="INV_CIMB_TEST_1",
      virtual_acc_trx_type="C",
      total_amount=TotalAmount(value="12500.00", currency="IDR"),
      additional_info=AdditionalInfo(
          channel="VIRTUAL_ACCOUNT_BANK_CIMB",
          virtual_account_config=VirtualAccountConfig(
              reusable_status=True,
          )
      ),
      expired_date="2025-08-31T09:54:04+07:00",
      customer_no="17223992157",
      virtual_account_no="812901417223992157"
    )

    response: CreateVAResponse = snap.create_va(create_va_request= request)
    ```

2. **Update Virtual Account**
    - **Function:** `updateVa`

    ```python
    from doku_python_library.src.model.va.update_va_request import UpdateVaRequest

    update_va_request: UpdateVaRequest = UpdateVaRequest(
      partnerServiceId="8129014",
      customerNo="17223992157",
      virtualAccountName="Test Example",
      trxId="INV_CIMB_TEST_1",
      virtualAccountNo="812901417223992157",
      additionalInfo=UpdateVAAdditionalInfo(
          channel="VIRTUAL_ACCOUNT_BANK_CIMB",
          virtualAccountConfig=UpdateVAConfig(status="ACTIVE")
      ),
      totalAmount=TotalAmount(value="12500.00", currency="IDR"),
      virtualAccountTrxType="C",
      expiredDate="2025-08-31T09:54:04+07:00"
    )

    response: UpdateVAResponse = snap.update_va(update_request= update_va_request)
    ```

3. **Delete Virtual Account**

    | **Parameter**        | **Description**                                                             | **Data Type**       | **Required** |
    |-----------------------|----------------------------------------------------------------------------|---------------------|--------------|
    | `partnerServiceId`    | The unique identifier for the partner service.                             | String(8)        | ✅           |
    | `customerNo`          | The customer's identification number.                                      | String(20)       | ✅           |
    | `virtualAccountNo`    | The virtual account number associated with the customer.                   | String(20)       | ✅           |
    | `trxId`               | Invoice number in Merchant's system.                                       | String(64)       | ✅           |
    | `additionalInfo`      | `channel`: Channel applied for this VA.<br><small>Example: VIRTUAL_ACCOUNT_BANK_CIMB</small> | String(30)       | ✅    |

    
  - **Function:** `deletePaymentCode`

    ```python
    from doku_python_library.src.model.va.delete_va_request import DeleteVARequest
    from doku_python_library.src.model.va.delete_va_response import DeleteVAResponse

    delete_va: DeleteVARequest = DeleteVARequest(
      partner_service_id="8129014",
      customer_no="17223992157",
      trx_id="INV_CIMB_TEST_1",
      virtual_acc_no="812901417223992157",
      additional_info=DeleteVAAdditionalInfo(
          channel="VIRTUAL_ACCOUNT_BANK_CIMB"
      )
    )

    response: DeleteVAResponse = snap.delete_payment_code(delete_va_request= delete_va)
    ```


#### II. Virtual Account (DIPC)
- **Description:** The VA number is registered on merchant side and DOKU will forward Acquirer inquiry request to merchant side when the customer make payment at the acquirer channel

- **Function:** `directInquiryVa`

    ```python
    @app.route('/v1.1/transfer-va/inquiry', methods=['POST'])
    def directInquiryVa() -> dict:
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
                row_va = fetch_direct_inquiry_va(virtual_account_no=request_json['virtualAccountNo'])
                if row_va is not None and not isinstance(row_va, str):
                    db_status = update_status_inquiry(status_va="inquiry", settlement_time=request_json["trxDateInit"], va_number=request_json['virtualAccountNo'])
                    if db_status == 200:
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
                            response["db_status"] = db_status
                            return json.dumps(response)
                        else:
                            return {
                                "responseCode": "4012400",
                                "responseMessage": "Virtual Account Not Found",
                                "db_status": db_status
                                }
                    else:
                        return {
                                "responseCode": "4012400",
                                "responseMessage": "Virtual Account Not Found",
                                "db_status": db_status
                                }
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

#### III. Check Virtual Account Status
 | **Parameter**        | **Description**                                                             | **Data Type**       | **Required** |
|-----------------------|----------------------------------------------------------------------------|---------------------|--------------|
| `partnerServiceId`    | The unique identifier for the partner service.                             | String(8)        | ✅           |
| `customerNo`          | The customer's identification number.                                      | String(20)       | ✅           |
| `virtualAccountNo`    | The virtual account number associated with the customer.                   | String(20)       | ✅           |
| `inquiryRequestId`    | The customer's identification number.                                      | String(128)       | ❌           |
| `paymentRequestId`    | The virtual account number associated with the customer.                   | String(128)       | ❌           |
| `additionalInfo`      | The virtual account number associated with the customer.                   | String      | ❌           |

  - **Function:** `checkStatusVa`
    ```python
    from doku_python_library.src.model.va.check_status_va_request import CheckStatusRequest
    from doku_python_library.src.model.va.check_status_va_response import CheckStatusResponse

    check_status_request: CheckStatusRequest = CheckStatusRequest(
      partner_service_id="8129014",
      customer_no="17223992157",
      virtual_acc_no="812901417223992157"
    )

    check_status_response: CheckStatusResponse = snap.check_status_va(check_status_request= check_status_request)
    ```

### B. Binding / Registration Operations
The card registration/account binding process must be completed before payment can be processed. The merchant will send the card registration request from the customer to DOKU.

Each card/account can only registered/bind to one customer on one merchant. Customer needs to verify OTP and input PIN.

| **Services**     | **Binding Type**      | **Details**                        |
|-------------------|-----------------------|-----------------------------------|
| Direct Debit      | Account Binding       | Supports **Allo Bank** and **CIMB** |
| Direct Debit      | Card Registration     | Supports **BRI**                    |
| E-Wallet          | Account Binding       | Supports **OVO**                    |

#### I. Account Binding 
1. **Binding**

<table>
  <thead>
    <tr>
      <th><strong>Parameter</strong></th>
      <th colspan="2"><strong>Description</strong></th>
      <th><strong>Data Type</strong></th>
      <th><strong>Required</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>phoneNo</code></td>
      <td colspan="2">Phone Number Customer. <br> <small>Format: 628238748728423</small> </td>
      <td>String(9-16)</td>
      <td>✅</td>
    </tr>
    <tr>
      <td rowspan="13"><code>additionalInfo</code></td>
      <td colspan="2"><code>channel</code>: Payment Channel<br></td>
      <td>String</td>
      <td>✅</td>
    </tr>
    <tr>
      <td colspan="2"><code>custIdMerchant</code>: Customer id from merchant</td>
      <td>String(64)</td>
      <td>✅</td>
    </tr>
    <tr>
      <td colspan="2"><code>customerName</code>: Customer name from merchant</td>
      <td>String(70)</td>
      <td>❌</td>
    </tr>
    <tr>
      <td colspan="2"><code>email</code>: Customer email from merchant </td>
      <td>String(64)</td>
      <td>❌</td>
    </tr>
    <tr>
      <td colspan="2"><code>idCard</code>: Customer id card from merchant</td>
      <td>String(20)</td>
      <td>❌</td>
    </tr>
    <tr>
      <td colspan="2"><code>country</code>: Customer country </td>
      <td>String</td>
      <td>❌</td>
    </tr>
    <tr>
      <td colspan="2"><code>address</code>: Customer Address</td>
      <td>String(255)</td>
      <td>❌</td>
    </tr>
        <tr>
      <td colspan="2"><code>dateOfBirth</code> </td>
      <td>String(YYYYMMDD)</td>
      <td>❌</td>
    </tr>
    <tr>
      <td colspan="2"><code>successRegistrationUrl</code>: Redirect URL when binding is success </td>
      <td>String</td>
      <td>✅</td>
    </tr>
    <tr>
      <td colspan="2"><code>failedRegistrationUrl</code>: Redirect URL when binding is success fail</td>
      <td>String</td>
      <td>✅</td>
    </tr>
    <tr>
      <td colspan="2"><code>deviceModel</code>: Device Model customer </td>
      <td>String</td>
      <td>✅</td>
    </tr>
    <tr>
      <td colspan="2"><code>osType</code>: Format: ios/android </td>
      <td>String</td>
      <td>✅</td>
    </tr>
    <tr>
      <td colspan="2"><code>channelId</code>: Format: app/web </td>
      <td>String</td>
      <td>✅</td>
    </tr>
    </tbody>
  </table> 

  - **Function:** `doAccountBinding`

    ```python
    from doku_python_library.src.model.direct_debit.account_binding_request import AccountBindingRequest, AccountBindingAdditionalInfoRequest
    from doku_python_library.src.model.direct_debit.account_binding_response import AccountBindingResponse

    accountBindingRequest = AccountBindingRequest(
      phone_no="6288912121237",
      additional_info=AccountBindingAdditionalInfoRequest(
          channel="DIRECT_DEBIT_CIMB_SNAP",
          cust_id_merchant="CUST123",
          customer_name="John Doe",
          email="john.doe@example.com",
          id_card="99999",
          country="Indonesia",
          address="Jakarta",
          date_of_birth="19990101",
          success_registration_url="https://success.example.com",
          failed_registration_url="https://fail.example.com",
          device_model="iPhone 12",
          os_type="ios",
          channel_id="CH001"
      )
    )

    response: AccountBindingResponse = snap.do_account_binding(request= accountBindingRequest, device_id="YOUR_DEVICE_ID", ip_address="YOUR_IP_ADDRESS")
    ```

1. **Unbinding**

    - **Function:** `getTokenB2B2C`
    ```python
    from doku_python_library.src.model.token.token_b2b2c_response import TokenB2B2CResponse

    authCode := "YOUR_AUTH_CODE_FROM_ACCOUNT_BINDING"
    responseB2B2C: TokenB2B2CResponse = snap.get_token_b2b2c(auth_code=authCode)
   ```
    - **Function:** `doAccountUnbinding`
    ```python
    from doku_python_library.src.model.direct_debit.account_unbinding_request import AccountUnbindingRequest, AccountUnbindingAdditionalInfoRequest
    from doku_python_library.src.model.direct_debit.account_unbinding_response import AccountUnbindingResponse

    accountUnbindingRequest = AccountUnbindingRequest(
      token=responseB2B2C.access_token,
      additional_info=AccountUnbindingAdditionalInfoRequest(
          channel="DIRECT_DEBIT_CIMB_SNAP"
      )
    )

    response: AccountUnbindingResponse = snap.do_account_unbinding(request= accountUnbindingRequest, ip_address="YOUR_IP_ADDRESS")
    ```

#### II. Card Registration
1. **Registration**
    - **Function:** `doCardRegistration`

    ```python
    from doku_python_library.src.model.direct_debit.card_registration_request import CardRegistrationRequest, CardRegistrationAdditionalInfo
    from doku_python_library.src.model.direct_debit.card_registration_response import CardRegistrationResponse

    cardRegistRequest = CardRegistrationRequest(
      card_data=BankCardData(
          bank_card_no="7801",
          bank_card_type="D",
          expiry_date="0525",
          email="email@email.com"
      ),
      cust_id_merchant="Jhon Doe",
      phone_no="6282124918109",
      additionalInfo=CardRegistrationAdditionalInfo(
          channel="DIRECT_DEBIT_BRI_SNAP",
          date_of_birth="19990101",
          success_registration_url="https://success.example.com",
          failed_registration_url="https://fail.example.com"
      )
    )

    cardRegistrationResponse: CardRegistrationResponse = snap.do_card_registration(request= cardRegistRequest, channel_id="DH")
    ```

2. **UnRegistration**
    - **Function:** `getTokenB2B2C`
    ```python
    from doku_python_library.src.model.token.token_b2b2c_response import TokenB2B2CResponse

    authCode := "YOUR_AUTH_CODE_FROM_ACCOUNT_BINDING"
    responseB2B2C: TokenB2B2CResponse = snap.get_token_b2b2c(auth_code=authCode)
    ```
    - **Function:** `doCardUnbinding`

    ```python
    from doku_python_library.src.model.direct_debit.card_unbinding_request import CardUnbindingRequest
    from doku_python_library.src.model.direct_debit.card_unbinding_response import CardUnbindingResponse

    cardUnbindingRequest = CardUnbindingRequest(
      token=responseB2B2C.access_token,
      additional_info=AccountUnbindingAdditionalInfoRequest(
          channel="DIRECT_DEBIT_BRI_SNAP"
      )
    )
    
    cardUnbindingResponse: CardUnbindingResponse = snap.do_card_unbinding(request= cardUnbindingRequest, ip_address= 'YOUR_IP_ADDRESS')
    ```

### C. Direct Debit and E-Wallet 

#### I. Request Payment
  Once a customer’s account or card is successfully register/bind, the merchant can send a payment request. This section describes how to send a unified request that works for both Direct Debit and E-Wallet channels.

| **Acquirer**       | **Channel Name**         | 
|-------------------|--------------------------|
| Allo Bank         | DIRECT_DEBIT_ALLO_SNAP   | 
| BRI               | DIRECT_DEBIT_BRI_SNAP    | 
| CIMB              | DIRECT_DEBIT_CIMB_SNAP   |
| OVO               | EMONEY_OVO_SNAP   | 

##### Common parameter
<table>
  <thead>
    <tr>
      <th><strong>Parameter</strong></th>
      <th colspan="2"><strong>Description</strong></th>
      <th><strong>Data Type</strong></th>
      <th><strong>Required</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>partnerReferenceNo</code></td>
      <td colspan="2"> Reference No From Partner <br> <small>Format: 628238748728423</small> </td>
      <td>String(9-16)</td>
      <td>✅</td>
    </tr>
    <tr>
      <td rowspan="2"><code>amount</code></td>
      <td colspan="2"><code>value</code>: Transaction Amount (ISO 4217) <br> <small>Example: "11500.00"</small></td>
      <td>String(16.2)</td>
      <td>✅</td>
    </tr>
    <tr>
      <td colspan="2"><code>Currency</code>: Currency <br> <small>Example: "IDR"</small></td>
      <td>String(3)</td>
      <td>✅</td>
    </tr>
    <tr>
      <td rowspan="4"><code>additionalInfo</code> </td>
      <td colspan = "2" ><code>channel</code>: payment channel</td>
      <td>String</td>
      <td>✅</td>
    </tr>
    <tr>
      <td colspan="2"><code>remarks</code>:Remarks from Partner</td>
      <td>String(40)</td>
      <td>✅</td>
    </tr>
    <tr>
      <td colspan="2"><code>successPaymentUrl</code>: Redirect Url if payment success</td>
      <td>String</td>
      <td>✅</td>
    </tr>
        <tr>
      <td colspan="2"><code>failedPaymentUrl</code>: Redirect Url if payment fail
      </td>
      <td>String</td>
      <td>✅</td>
    </tr>
    </tbody>
  </table> 

 ##### Allo Bank Specific Parameters

| **Parameter**                        | **Description**                                               | **Required** |
|--------------------------------------|---------------------------------------------------------------|--------------|
| `additionalInfo.remarks`             | Remarks from the partner                                      | ✅           |
| `additionalInfo.lineItems.name`      | Item name (String)                                            | ✅           |
| `additionalInfo.lineItems.price`     | Item price (ISO 4217)                                         | ✅           |
| `additionalInfo.lineItems.quantity`  | Item quantity (Integer)                                      | ✅           |
| `payOptionDetails.payMethod`         | Balance type (options: BALANCE/POINT/PAYLATER)                | ✅           |
| `payOptionDetails.transAmount.value` | Transaction amount                                            | ✅           |
| `payOptionDetails.transAmount.currency` | Currency (ISO 4217, e.g., "IDR")                             | ✅           |


#####  CIMB Specific Parameters

| **Parameter**                        | **Description**                                               | **Required** |
|--------------------------------------|---------------------------------------------------------------|--------------|
| `additionalInfo.remarks`             | Remarks from the partner                                      | ✅           |


#####  DANA Specific Parameters

| **Parameter**                           | **Description**                                                | **Required** |
| ------------------------------------|---------------------------------------------------------------|--------------|
| `additionalInfo.orderTitle`              | Order title from merchant (optional)                          | ❌           |
| `additionalInfo.supportDeepLinkCheckoutUrl` | Value ('true' for Jumpapp behavior, 'false' for webview, default: 'false') | ❌           |


#####  OVO Specific Parameters

| **Parameter**                           | **Description**                                                | **Required** |
|------------------------------------------|---------------------------------------------------------------|--------------|
| `feeType`                                | Fee type from partner (values: OUR, BEN, SHA)                  | ❌           |
| `payOptionDetails.payMethod`             | Payment method format: CASH, POINTS                            | ✅           |
| `payOptionDetails.transAmount.value`    | Transaction amount (ISO 4217)                                  | ✅           |
| `payOptionDetails.transAmount.currency` | Currency (ISO 4217, e.g., "IDR")                               | ✅           |
| `payOptionDetails.feeAmount.value`      | Fee amount (if applicable)                                     | ✅           |
| `payOptionDetails.feeAmount.currency`   | Currency for the fee                                          | ✅           |
| `additionalInfo.paymentType`            | Transaction type (values: SALE, RECURRING)                     | ✅           |

  
Here’s how you can use the `doPayment` function for both payment types:
  - **Function:** `doPayment`
    
    ```python
    from doku_python_library.src.model.direct_debit.payment_request import PaymentRequest
    from doku_python_library.src.model.direct_debit.payment_response import PaymentResponse
    from doku_python_library.src.model.direct_debit.pay_option_detail import PayOptionDetail
    from doku_python_library.src.model.direct_debit.payment_additional_info_request import PaymentAdditionalInfoRequest
    from doku_python_library.src.model.va.total_amount import TotalAmount

    payment_request = PaymentRequest(
      partner_reference_no="INV-101", 
      fee_type="OUR",  # Only for OVO (Optional) - OUR/BEN/SHA
      amount=TotalAmount(
          value="10000.00",         
          currency="IDR"                
      ),
      pay_option_detail=[  # Only for OVO or ALLO_BANK (Required)
          PayOptionDetail(
              pay_method="CASH",  # CASH / POINTS (OVO) or BALANCE/POINT/PAYLATER (ALLO_BANK)
              trans_amount=TotalAmount(
                  value="10000.00",
                  currency="IDR" 
              ),
              fee_amount=TotalAmount(
                  value="1100.00",
                  currency="IDR"    
              )
          )
      ],
      additional_info=PaymentAdditionalInfoRequest(
          channel="EMONEY_OVO_SNAP",  # "DIRECT_DEBIT_CIMB / DIRECT_DEBIT_BRI_SNAP / DIRECT_DEBIT_ALLO_SNAP / EMONEY_OVO_SNAP"
          remarks="Payment Order",  
          success_payment_url="https://success.example.com",
          failed_payment_url="https://fail.example.com", 
          line_items=[   # Only for ALLO_BANK
              LineItems(
                  name="Bag",           
                  price="10000.00",     
                  quantity="1"         
              )
          ],
          payment_type="SALE"  # Only For OVO and BRI: SALE, RECURRING (Optional)
      ),
      charge_token=""
    )

    paymentResponse: PaymentResponse = snap.do_payment(request= payment_request, ip_address="YOUR_IP_ADDRESS", auth_code="YOUR_AUTH_CODE_FROM_BINDING")
    ```
#### II. Request Payment Jump App
| **Acquirer**      | **Channel Name**        | 
|-------------------|-------------------------|
| DANA              | EMONEY_DANA_SNAP        | 
| ShopeePay         | EMONEY_SHOPEE_PAY_SNAP  |

The following fields are common across **DANA and ShopeePay** requests:
<table>
  <thead>
    <tr>
      <th><strong>Parameter</strong></th>
      <th colspan="2"><strong>Description</strong></th>
      <th><strong>Data Type</strong></th>
      <th><strong>Required</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>partnerReferenceNo</code></td>
      <td colspan="2"> Reference No From Partner <br> <small>Examplae : INV-0001</small> </td>
      <td>String(9-16)</td>
      <td>✅</td>
    </tr>
    <tr>
      <td><code>validUpto</code></td>
      <td colspan = "2" >Expired time payment url </td>
      <td>String</td>
      <td>❌</td>
    </tr>
    <tr>
      <td><code>pointOfInitiation</code></td>
      <td colspan = "2" >Point of initiation from partner,<br> value: app/pc/mweb </td>
      <td>String</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan = "3" > <code>urlParam</code></td>
      <td colspan = "2"><code>url</code>: URL after payment sucess </td>
      <td>String</td>
      <td>✅</td>
    </tr>
    <tr>
      <td colspan="2"><code>type</code>: Pay Return<br> <small>always PAY_RETURN </small></td>
      <td>String</td>
      <td>✅</td>
    </tr>
    <tr>
      <td colspan="2"><code>isDeepLink</code>: Is Merchant use deep link or not<br> <small>Example: "Y/N"</small></td>
      <td>String(1)</td>
      <td>✅</td>
    </tr>
    <tr>
      <td rowspan="2"><code>amount</code></td>
      <td colspan="2"><code>value</code>: Transaction Amount (ISO 4217) <br> <small>Example: "11500.00"</small></td>
      <td>String(16.2)</td>
      <td>✅</td>
    </tr>
    <tr>
      <td colspan="2"><code>Currency</code>: Currency <br> <small>Example: "IDR"</small></td>
      <td>String(3)</td>
      <td>✅</td>
    </tr>
    <tr>
      <td><code>additionalInfo</code> </td>
      <td colspan = "2" ><code>channel</code>: payment channel</td>
      <td>String</td>
      <td>✅</td>
    </tr>
    </tbody>
  </table> 

##### DANA

DANA spesific parameters
<table>
    <thead>
    <tr>
      <th><strong>Parameter</strong></th>
      <th colspan="2"><strong>Description</strong></th>
      <th><strong>Data Type</strong></th>
      <th><strong>Required</strong></th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <td rowspan = "2" ><code>additionalInfo</code></td>
      <td colspan = "2" ><code>orderTitle</code>: Order title from merchant</td>
      <td>String</td>
      <td>❌</td>
    </tr>
    <tr>
      <td colspan = "2" ><code>supportDeepLinkCheckoutUrl</code> : Value 'true' for Jumpapp behaviour, 'false' for webview, false by default</td>
      <td>String</td>
      <td>❌</td>
    </tr>
    </tbody>
  </table> 
For Shopeepay and Dana you can use the `doPaymentJumpApp` function for for Jumpapp behaviour

- **Function:** `doPaymentJumpApp`

```python
from doku_python_library.src.model.direct_debit.payment_jump_app_request import PaymentJumpAppRequest, PaymentJumpAppAdditionalInfo, UrlParam
from doku_python_library.src.model.direct_debit.paymet_jump_app_response import PaymentJumpAppResponse

payment_jump_app_request = PaymentJumpAppRequest(
    partner_reference_no="INV-101",      
    valid_up_to="2025-12-31T23:59:59Z",  
    point_of_initiation="app", # app/pc/mweb
    url_param=[  
        UrlParam(
            url="https://your.url/endpoint",  
            type="PAY_RETURN",                 
            is_deep_link="Y"                  
        )
    ],
    amount=TotalAmount(                    
        value="10000.00",                 
        currency="IDR"                     
    ),
    additional_info=PaymentJumpAppAdditionalInfo(  
        channel="EMONEY_DANA_SNAP", # EMONEY_DANA_SNAP or EMONEY_SHOPEE_PAY_SNAP
        order_title="Payment Order",          
        metadata="Your Metadata",              # Only for ShopeePay (Optional)
        support_deeplink_checkout_url=True     # Only for DANA (Optional)
    )
)


paymentJumpAppResponse: PaymentJumpAppResponse = snap.do_payment_jump_app(request= payment_jump_app_request, device_id="YOUR_DEVICE_ID", ip_address="YOUR_IP_ADDRESS")
```

## 3. Other Operation

### A. Check Transaction Status

  ```python	
  from doku_python_library.src.model.direct_debit.check_status_request import CheckStatusRequest
  from doku_python_library.src.model.direct_debit.check_status_response import CheckStatusResponse 

  def check_status(self, request: CheckStatusRequest) -> CheckStatusResponse:
        return snap.do_check_status(request=request)
  ```

### B. Refund

  ```python
  from doku_python_library.src.model.direct_debit.refund_request import RefundRequest, RefundAdditionalInfo
  from doku_python_library.src.model.direct_debit.refund_response import RefundResponse

  def refund(self, request: RefundRequest, ip_address: str, auth_code: str, device_id: str) -> RefundResponse:
        return snap.do_refund(
            request=request,
            ip_address=ip_address,
            auth_code=auth_code,
            device_id=device_id
        )
  ```

### C. Balance Inquiry

  ```python
  from doku_python_library.src.model.direct_debit.balance_inquiry_request import BalanceInquiryRequest
  from doku_python_library.src.model.direct_debit.balance_inquiry_response import BalanceInquiryResponse

  def balance_inquiry(self, request: BalanceInquiryRequest, ip_address: str, auth_code: str) -> BalanceInquiryResponse:
        return snap.do_balance_inquiry(
            request=request,
            ip_address=ip_address,
            auth_code=auth_code
        )
  ```

## 4. Error Handling and Troubleshooting

The SDK returns errors for various conditions. Always check for errors when making API calls:
 ```python
import logging

try:
    create_va_response = snap.create_va(create_va_request_dto)
except Exception as err:
    # Handle the error appropriately
    logging.error("Error: %s", str(err))
    # You can also return or take other actions based on the error
    return

# Process successful result
logging.info("VA created successfully: %s", create_va_response)

```

This section provides common errors and solutions:

| Error Code | Description                           | Solution                                     |
|------------|---------------------------------------|----------------------------------------------|
| `4010000`  | Unauthorized                          | Check if Client ID and Secret Key are valid. |
| `4012400`  | Virtual Account Not Found             | Verify the virtual account number provided.  |
| `2002400`  | Successful                            | Transaction completed successfully.          |
