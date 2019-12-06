"""
 # FraudLabsPro Python Library
 # Implements fraud checking solution using FraudLabs Pro service.
 # API key is required, and if you do not have an API key, you may sign up free
 # at at http://www.fraudlabspro.com
 #
 # @copyright 2018 FraudLabs Pro
 # http://www.fraudlabspro.com

"""

import urllib.parse
import urllib.request
import json

"""
 # FraudLabsPro SMS Verification module.
 #
 #Send SMS Verification for authentication and get Verification result.
"""
class SMSVerification:
	"""
	 # Send SMS Verification for authentication.
	 #
	 # Result will be return in json format.
	"""
	def send_sms(send_sms_variables):
		if 'key' in send_sms_variables:
			apikey = send_sms_variables['key']
		else:
			return 'The API key is required. Please obtain through here: https://www.fraudlabspro.com/pricing'
		if 'tel' in send_sms_variables:
			tel_no = send_sms_variables['tel']
		else:
			return 'Telephone number is required.'
		if 'country_code' in send_sms_variables:
			country_code = send_sms_variables['country_code']
		else:
			country_code = ''
		if 'mesg' in send_sms_variables:
			message = send_sms_variables['mesg']
		else:
			return 'Message is required.'
		send_sms_variables_list = {
			'key': apikey,
			'format': 'json',
			'tel': tel_no,
			'country_code': country_code,
			'mesg': message,
		}
		url = 'https://api.fraudlabspro.com/v1/verification/send'
		data = urllib.parse.urlencode(send_sms_variables_list)
		data = data.encode('utf-8')
		request = urllib.request.Request(url, data)
		with urllib.request.urlopen(request) as response:
			string = response.read().decode('utf-8')
		json_obj = json.loads(string)
		result = json.dumps(json_obj, indent=4)
		return(result)
		
	"""
	 # Get Verification result.
	 #
	 #Result will be return in json format.
	"""
	def verify_sms(verify_sms_variables):
		if 'key' in verify_sms_variables:
			apikey = verify_sms_variables['key']
		else:
			return 'The API key is required. Please obtain through here: https://www.fraudlabspro.com/pricing'
			
		if 'tran_id' in verify_sms_variables:
			transaction_id = verify_sms_variables['tran_id']
		else:
			return 'Transaction id is required.'
		if 'otp' in verify_sms_variables:
			otp = verify_sms_variables['otp']
		else:
			return 'OTP is required.'
		verify_sms_variables_list = {
			'key': apikey,
			'format': 'json',
			'tran_id': transaction_id,
			'otp': otp,
		}
		url = 'https://api.fraudlabspro.com/v1/verification/result'
		url_values = urllib.parse.urlencode(verify_sms_variables_list)
		full_url = url + '?' + url_values
		data = urllib.request.urlopen(full_url)
		string = data.read().decode('utf-8')
		json_obj = json.loads(string)
		result = json.dumps(json_obj, indent=4)
		return(result)