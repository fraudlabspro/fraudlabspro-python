# FraudLabs Pro Python SDK

This Python module enables user to easily implement fraud detection feature into their solution using the API from https://www.fraudlabspro.com.



Below are the features of this Python module:

* Fraud analysis and scoring
* Credit card issuing bank validation
* SMS verification and validation

This module requires API key to function. You may subscribe a free API key at https://www.fraudlabspro.com





## Usage Example

### Validate Order

#### Object Properties



| Property Name        | Property Type | Description                                                  |
| -------------------- | ------------- | ------------------------------------------------------------ |
| ip                   | string        | IP address of online transaction. It supports both IPv4 and IPv6 address format. |
| billing->firstName   | string        | User's first name.                                           |
| billing->lastName    | string        | User's last name.                                            |
| billing->username    | string        | User's username.                                             |
| billing->password    | string        | User's password.                                             |
| billing->email       | string        | User's email address.                                        |
| billing->phone       | string        | User's phone number.                                         |
| billing->address     | string        | Street address of billing address.                           |
| billing->city        | string        | City of billing address.                                     |
| billing->state       | string        | State of billing address. It supports state codes, e.g. NY (New York), for state or province of United States or Canada. Please refer to [State & Province Codes](https://www.fraudlabspro.com/developer/reference/state-and-province-codes) for complete list. |
| billing->postcode    | string        | Postal or ZIP code of billing address.                       |
| billing->country     | string        | Country of billing address. It requires the input of ISO-3166 alpha-2 country code, e.g. US for United States. Please refer to [Country Codes](https://www.fraudlabspro.com/developer/reference/country-codes) for complete list. |
| order->orderId       | string        | Merchant identifier to uniquely identify a transaction. It supports maximum of 15 characters user order id input. |
| order->note          | string        | Merchant description of an order transaction. It supports maximum of 200 characters. |
| order->amount        | float         | Amount of the transaction.                                   |
| order->quantity      | integer       | Total quantity of the transaction.                           |
| order->currency      | string        | Currency code used in the transaction. It requires the input of ISO-4217 (3 characters) currency code, e.g. USD for US Dollar. Please refer to [Currency Codes](https://www.fraudlabspro.com/developer/reference/currency-codes) for complete list. |
| order->department    | string        | Merchant identifier to uniquely identify a product or service department. |
| order->paymentMethod | string        | Payment mode of transaction. Please see references section.  |
| card->number         | string        | Billing credit card number or BIN number.                    |
| card->avs            | string        | The single character AVS result returned by the credit card processor. Please refer to [AVS & CVV2 Response Codes](https://www.fraudlabspro.com/developer/reference/avs-and-cvv2-response-codes) for details. |
| card->cvv            | string        | The single character CVV2 result returned by the credit card processor. Please refer to [AVS & CVV2 Response Codes](https://www.fraudlabspro.com/developer/reference/avs-and-cvv2-response-codes) for details. |
| shipping->address    | string        | Street address of shipping address.                          |
| shipping->city       | string        | City of shipping address.                                    |
| shipping->state      | string        | State of shipping address. It supports state codes, e.g. NY - New York, for state or province of United States or Canada. Please refer to [State & Province Codes](https://www.fraudlabspro.com/developer/reference/state-and-province-codes) for complete list. |
| shipping->postcode   | string        | Postal or ZIP code of shipping address.                      |
| shipping->country    | string        | Country of shipping address. It requires the input of ISO-3166 alpha-2 country code, e.g. US for United States. Please refer to [Country Codes](https://www.fraudlabspro.com/developer/reference/country-codes) for complete list. |



```python
 # import SDK to use the function
from fraudlabspro.fraudvalidation import FraudValidation

 # Configure your API key
api_key = 'YOUR_API_KEY'
fraud_validation = FraudValidation(api_key)

 # Order Details
dict1 = {
	'ip': '146.112.62.105',
	'order': {
		'order_id': '67398', 
		'currency': 'USD',
		'amount': '42',
		'quantity': 1, 
		'paymentMethod': 'creditcard'
	},
	'card': {
		'number': '4556553172971283'
	},
	'billing': {
		'firstName': 'Hector',
		'lastName': 'Henderson',
		'email': 'hh5566@gmail.com',
		'phone': '561-628-8674',
		'address': '1766 Powder House Road',
		'city': 'West Palm Beach',
		'state': 'FL',
		'postcode': '33401',
		'country': 'US',
	},
	'shipping': {
		'address': '4469 Chestnut Street',
		'city'   : 'Tampa',
		'state'  : 'FL',
		'postcode': '33602',
		'country': 'US',
	}
}

 # Sends the order details to FraudLabs Pro
result = fraud_validation.validate(dict1)
```



### Get Transaction

#### Parameter Properties

| Parameter Name | Parameter Type | Description                                                  |
| -------------- | -------------- | ------------------------------------------------------------ |
| $id            | string         | FraudLabs Pro transaction ID or Order ID.                    |

```python
 # import SDK to use the function
from fraudlabspro.fraudvalidation import FraudValidation

 # Configure your API key
api_key = 'YOUR_API_KEY'
fraud_validation = FraudValidation(api_key)

 # Values to get transaction details
get_transaction_variables = {
	'id': '20180705-WISXW2',
}

 # Send the values to FraudLabs Pro
result = fraud_validation.get_transaction(get_transaction_variables)
```



### Feedback

#### Object Properties

| Property Name | Property Type | Description                                                  |
| ------------- | ------------- | ------------------------------------------------------------ |
| id            | string        | Unique transaction ID generated from **Validate** function.  |
| status        | string        | Perform APPROVE, REJECT, or REJECT_BLACKLIST action to transaction.	Refer to [reference section](#feedback-status) for status code. |
| note          | string        | Notes for the feedback request.                              |

```python
 # import SDK to use the function
from fraudlabspro.fraudvalidation import FraudValidation

 # Configure your API key
api_key = 'YOUR_API_KEY'
fraud_validation = FraudValidation(api_key)

 # Set feedback of the particular order
feedback_variables = {
	'id': '20180705-WISXW2',
	# Three actions available: APPROVE, REJECT, REJECT_BLACKLIST
	'action': 'APPROVE',
	'notes': 'This is for testing purpose.',
}

result = fraud_validation.feedback(feedback_variables)
```



## SMS Verification

### Send SMS Verification

#### Object Properties

| Property Name | Property Type | Description                                                  |
| ------------- | :-----------: | ------------------------------------------------------------ |
| tel           |    string     | The recipient mobile phone number in E164 format which is a plus followed by just numbers with no spaces or parentheses. |
| mesg          |    string     | The message template for the SMS. Add <otp> as placeholder for the actual OTP to be generated. Max length is 140 characters. |
| otp_timeout   |    integer    | Timeout feature for OTP value in seconds. Default is 3600 seconds(1 hour). Max timeout is 86400 seconds(24 hours). |
| country_code  |    string     | ISO 3166 country code for the recipient mobile phone number. If parameter is supplied, then some basic telephone number validation is done. |

```python
 # import SDK to use the function
from fraudlabspro.smsverification import SMSVerification
 
 # Configure your API key
api_key = 'YOUR_API_KEY'
sms_validation = SMSVerification(api_key)

 # Send SMS verification
sms_verification_variables = {
	'tel': '+123456789',
	'country_code': 'US',
	'mesg': 'Your OTP for the transaction is <otp>.',
	'otp_timeout': 3600,
}
result = sms_validation.send_sms(sms_verification_variables)
```



### Get SMS Verification Result

#### Object Properties

| Property Name | Property Type | Description                                                  |
| ------------- | :-----------: | ------------------------------------------------------------ |
| tran_id       |    string     | The unique ID that was returned by the Send SMS Verification that triggered the OTP sms. |
| otp           |    string     | The OTP that was sent to the recipient’s phone.              |

```python
 # import SDK to use the function
from fraudlabspro.smsverification import SMSVerification
 
 # Configure your API key
api_key = 'YOUR_API_KEY'
sms_validation = SMSVerification(api_key)

 # Get SMS verification result
verify_sms_variables = {
	'tran_id': 'UNIQUE_TRANS_ID',
	'otp': 'OTP_RECEIVED',
}
result = sms_validation.verify_sms(verify_sms_variables)
```



# Reference

#### Payment Method

| Payment Method |
| -------------- |
| creditcard     |
| paypal         |
| googlecheckout |
| bitcoin        |
| cod            |
| moneyorder     |
| wired          |
| bankdeposit    |
| others         |



LICENCE
=====================
See the LICENSE file.
