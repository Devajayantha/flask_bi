import os

class Config:
    BASE_URL_SNAP = os.getenv("BASE_URL_SNAP", "https://apidevportal.aspi-indonesia.or.id:44310")
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    PUBLIC_KEY = os.getenv("PUBLIC_KEY")
    PRIVATE_KEY = os.getenv("PRIVATE_KEY")