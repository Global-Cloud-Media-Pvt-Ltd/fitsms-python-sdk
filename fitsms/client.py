import requests
import re

class FitSMS:
    def __init__(self, api_token, sender_id):
        self.api_token = api_token
        self.sender_id = sender_id
        self.v4_base = "https://app.fitsms.lk/api/v4"
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Accept": "application/json"
        }

    def _format_number(self, phone):
        """Standardizes SL numbers to 947XXXXXXXX format."""
        cleaned = re.sub(r'\D', '', str(phone))
        if cleaned.startswith('07') and len(cleaned) == 10:
            cleaned = '94' + cleaned[1:]
        elif cleaned.startswith('7') and len(cleaned) == 9:
            cleaned = '94' + cleaned
        return cleaned

    def send(self, recipients, message, sms_type="plain"):
        """Sends SMS to one or more recipients."""
        if isinstance(recipients, list):
            recipients = ",".join([self._format_number(n) for n in recipients])
        else:
            recipients = self._format_number(recipients)

        payload = {
            "recipient": recipients,
            "sender_id": self.sender_id,
            "type": sms_type,
            "message": message
        }

        try:
            response = requests.post(f"{self.v4_base}/sms/send", json=payload, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"status": "error", "message": str(e)}
      
    def get_status(self, ruid, phone):
        """
        Check the status of an existing SMS (v4 API).
        :param ruid: The unique reference ID (received after sending)
        :param phone: The recipient number
        """
        params = {
            "recipient": self._format_number(phone)
        }
        
        try:
            # v4 uses the ruid in the URL path
            response = requests.get(
                f"{self.v4_base}/sms/{ruid}", 
                params=params, 
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            # Handle cases where RUID is not found or API is down
            return {
                "status": "error", 
                "message": f"FitSMS Status Check Failed: {str(e)}"
            }

    def get_balance(self):
        """Retrieves account balance."""
        response = requests.get(f"{self.v4_base}/balance", headers=self.headers)
        return response.json()
    
    def get_profile(self):
        response = requests.get(f"{self.v4_base}/me", headers=self.headers)
        return response.json()