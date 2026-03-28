import time
from fitsms import FitSMS

# Initialize with your GCM credentials
api_token = "YOUR_BEARER_TOKEN_HERE"
sender_id = "YOUR_SENDER_ID_HERE"
phone = "947XXXXXXXX"

client = FitSMS(api_token, sender_id)

# 1. Check Balance
balance = client.get_balance()
print(f"Current Units: {balance.get('data', {})}")

# 2. Send Test SMS
response = client.send(phone, "GCM Python SDK Test - v4")
print(f"Send Status: {response.get('status')}")

ruid = response.get('data', {}).get('ruid')

if ruid:
    
    # 3. Check the status manually
    
    # Wait 10 seconds
    # This allows the telco to process the delivery
    print("Waiting 10 seconds for delivery status update...")
    time.sleep(10)
    
    # Note: In v4, real-time DLR comes via Webhook. 
    # Use this method only for manual sync.
    
    status = client.get_status(ruid, phone)
    print(f"Current Delivery Status: {status.get('data', {}).get('status')}")
