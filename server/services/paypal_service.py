import os
import requests
from dotenv import load_dotenv
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID")
SECRET = os.getenv("PAYPAL_SECRET")
API_BASE = os.getenv("PAYPAL_API_BASE", "https://api.sandbox.paypal.com")

def get_access_token():
    """Obtain PayPal API access token"""
    url = f"{API_BASE}/v1/oauth2/token"
    try:
        response = requests.post(
            url,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={"grant_type": "client_credentials"},
            auth=(CLIENT_ID, SECRET),
            timeout=10
        )
        if response.status_code == 200:
            return response.json().get("access_token")
        logger.error(f"Token request failed: {response.status_code} {response.text}")
    except Exception as e:
        logger.error(f"Token request exception: {str(e)}")
    return None

def create_paypal_order(total):
    """Create PayPal order and return approval URL"""
    token = get_access_token()
    if not token:
        return None

    url = f"{API_BASE}/v2/checkout/orders"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
        "Prefer": "return=representation"
    }
    
    # Format total to 2 decimal places
    formatted_total = f"{float(total):.2f}"
    
    payload = {
        "intent": "CAPTURE",
        "purchase_units": [{
            "amount": {
                "currency_code": "USD",
                "value": formatted_total
            }
        }],
        "application_context": {
            "return_url": "http://localhost:5173/success",
            "cancel_url": "http://localhost:5173/cancel",
            "brand_name": "Your Restaurant",
            "user_action": "PAY_NOW"
        }
    }
    
    try:
        response = requests.post(
            url, 
            json=payload, 
            headers=headers,
            timeout=15
        )
        if response.status_code == 201:
            # Find approval link
            for link in response.json().get("links", []):
                if link.get("rel") == "approve":
                    return {
                        "id": response.json().get("id"),
                        "approval_url": link.get("href")
                    }
        logger.error(f"Order creation failed: {response.status_code} {response.text}")
    except Exception as e:
        logger.error(f"Order creation exception: {str(e)}")
    return None