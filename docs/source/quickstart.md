# Quickstart

## Dependencies

This module requires API key to function. You may subscribe a free API key at https://www.fraudlabspro.com

## Installation

Install this package using the command as below:

```
pip install fraudlabspro-python
```

## Sample Codes

### Validate Order

You can validate your order as below:

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

You can get the details of a transaction as below:

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

You can approve, reject or ignore a transaction as below:

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

### Send SMS Verification

You can send SMS verification for authentication purpose as below:

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

You can verify the OTP sent by Fraudlabs Pro SMS verification API as below:

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