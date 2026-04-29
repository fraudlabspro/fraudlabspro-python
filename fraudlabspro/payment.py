import json
import urllib.parse
import urllib.request
from urllib.parse import urljoin

from .constants import BASE_URL, MODULE_VERSION


class Payment:
    """
    FraudLabsPro Payment module.

    Allows merchants to report the final payment status back to the system,
    helping improve fraud detection and risk assessment.
    """

    def __init__(self, api_key):
        self.api_key = api_key

    def feedback(self, feedback_variables):
        # Validate required fields
        required_fields = ['email', 'status', 'message']
        for field in required_fields:
            if field not in feedback_variables:
                return json.dumps({"error": f"{field} is required"})

        # Prepare payload
        payload = {
            'key': self.api_key,
            'source_version': MODULE_VERSION,
            'email': feedback_variables['email'],
            'status': feedback_variables['status'],
            'message': feedback_variables['message'],
        }

        # Handle optional fraudlabspro_id
        if 'fraudlabspro_id' in feedback_variables:
            payload['id'] = feedback_variables['fraudlabspro_id']

        url = urljoin(BASE_URL, 'payment/feedback')
        data = urllib.parse.urlencode(payload).encode('utf-8')

        try:
            request = urllib.request.Request(url, data=data)
            with urllib.request.urlopen(request) as response:
                raw_data = response.read().decode('utf-8')
            json_obj = json.loads(raw_data)
        except urllib.error.HTTPError as http_error:
            error_data = http_error.read().decode('utf-8')
            json_obj = json.loads(error_data)
        except Exception as e:
            return json.dumps({"error": str(e)})

        return json.dumps(json_obj, indent=4)