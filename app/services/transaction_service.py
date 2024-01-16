from app.services.auth_service import *
from app import app
from flask import request, jsonify

def show_inquiry_va():
    """
    This function is used to inquiry VA from SNAP BI
    """
    try:
        requests = request.get_json()

        if app.config['ACCESS_TOKEN'] is "":
            return jsonify({"message": "Please authentication first"}), 400

        if requests is None or requests == {}:
            return jsonify({"message": "Request body is empty"}), 400

        signature = generate_signature_service('/api/v1.0/transfer-va/inquiry', requests)

        if signature is None:
            return jsonify({"message": "Failed to generate signature"}), 400

        inquiry_response = inquiry_va(signature, requests)

        if inquiry_response is None:
            return jsonify({"message": "Failed to inquiry VA"}), 400

        return jsonify({"data": inquiry_response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Implement inquiry VA from SNAP BI
def inquiry_va(signature, payload, method = 'POST'):
    """
    This function is used to connect inquiry VA API
    :param signature:
    :param payload:
    :param method:
    """
    url = app.config['BASE_URL_SNAP'] + '/api/v1.0/transfer-va/inquiry'

    header = {
        "Content-Type": "application/json",
        "Authorization": app.config['ACCESS_TOKEN'],
        "X-TIMESTAMP": get_current_timestamp(),
        "X-CLIENT-SECRET": app.config['CLIENT_SECRET'],
        "HttpMethod": method,
        "X-PARTNER-ID": app.config['CLIENT_ID'],
        "X-SIGNATURE": signature,
        "X-EXTERNAL-ID": "41807553358950093184162180797837", #random
        "CHANNEL_ID": "41807553358950093184162180797837", #random
    }

    response = requests.post(url, data=json.dumps(payload), headers=header)

    if response.status_code == 200:
        return response.json()['data']

    return None