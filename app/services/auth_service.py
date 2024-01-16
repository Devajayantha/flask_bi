from app import app
from app.helpers import get_current_timestamp
from flask import jsonify
import json
import requests

def authentication():
    """
    This function is used to authentication to SNAP BI and get the access token
    """
    try:
        sign_auth = generate_signature_auth()

        url = app.config['BASE_URL_SNAP'] + '/api/v1.0/access-token/b2b'

        header = {
            "Content-Type": "application/json",
            "X-TIMESTAMP": get_current_timestamp(),
            "X-CLIENT-KEY": app.config['CLIENT_ID'],
            "X-SIGNATURE": sign_auth,
        }

        payload = {
            "grantType": "client_credentials"
        }

        response = requests.post(url, data=json.dumps(payload), headers=header)

        if response.status_code == 200:
            token: str = response.json()['accessToken']
            app.config['ACCESS_TOKEN'] = token

            return jsonify({"token": token}), 200

        return jsonify({"message": "failed authentitcation"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def generate_signature_auth():
    """
    This function is used to generate signature for authentication
    """
    url = app.config['BASE_URL_SNAP'] + '/api/v1.0/utilities/signature-auth'

    header = {
        "X-TIMESTAMP": get_current_timestamp(),
        "X-CLIENT-KEY": app.config['CLIENT_ID'],
        "Private_Key": app.config['PRIVATE_KEY'],
    }

    response = requests.post(url, data={}, headers=header)

    return response.json()['signature']

def generate_signature_service(service_url: str, payload, method = 'POST'):
    """
    This function will used to generate signature for each service
    :param service_url:
    :param payload:
    :param method:
    """
    url = app.config['BASE_URL_SNAP'] + '/api/v1.0/utilities/signature-service'

    header = {
        "Content-Type": "application/json",
        "X-TIMESTAMP": get_current_timestamp(),
        "X-CLIENT-SECRET": app.config['CLIENT_SECRET'],
        "HttpMethod": method,
        "EndpoinUrl": service_url,
        "AccessToken": app.config['ACCESS_TOKEN'],
    }

    response = requests.post(url, data=json.dumps(payload), headers=header)

    if response.status_code == 200:
        response_json = response.json()

        return response_json['signature']

    return None