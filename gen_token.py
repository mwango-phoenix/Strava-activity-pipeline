import os
import requests
from dotenv import load_dotenv

load_dotenv()

token_url = "https://www.strava.com/oauth/token"
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

  
def exchange_code_for_token(auth_code):
    """
    Exchange authorization code for access token
    Args:
        auth_code (str): get authorization code from Strava
    Returns:
        string: Access Token.
    """

    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": auth_code,
        "grant_type": "authorization_code",
    }
    res = requests.post(token_url, data=payload)
    res.raise_for_status()
    return res.json()["access_token"]


