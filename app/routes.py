from app import app
from app.services.transaction_service import *
from app.services.auth_service import *

@app.route('/api/v1/auth')
def create_auth():
    return authentication()
