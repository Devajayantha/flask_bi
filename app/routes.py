from app import app
from app.services.transaction_service import *
from app.services.auth_service import *

@app.route('/api/v1/auth', methods=['POST'])
def create_auth():
    return authentication()

@app.route('/api/v1/transaction', methods=['POST'])
def inquiry_transaction():
    return show_inquiry_va()