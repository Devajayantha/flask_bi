import requests
from config import Config
from app.helpers import get_current_timestamp
import json

def authentication():
    sign_auth = generate_signature_auth()

    url = Config.BASE_URL_SNAP + '/api/v1.0/access-token/b2b'

    header = {
        "Content-Type": "application/json",
        "X-TIMESTAMP": get_current_timestamp(),
        "X-CLIENT-KEY": Config.CLIENT_ID,
        "X-SIGNATURE": sign_auth,
    }

    data = {
        "grantType": "client_credentials"
    }

    response = requests.post(url, data=json.dumps(data), headers=header)

    if response.status_code == 200:
        return response.json()['accessToken']

    return None


def generate_signature_auth():
    url = Config.BASE_URL_SNAP + '/api/v1.0/utilities/signature-auth'

    header = {
        "X-TIMESTAMP": get_current_timestamp(),
        "X-CLIENT-KEY": Config.CLIENT_ID,
        "Private_Key": Config.PRIVATE_KEY,
    }

    response = requests.post(url, data={}, headers=header)

    return response.json()['signature']