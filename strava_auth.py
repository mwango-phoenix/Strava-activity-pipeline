import os
from urllib.parse import urlencode, urlparse, parse_qs
from dotenv import load_dotenv
import webbrowser

load_dotenv()

auth_url = "http://www.strava.com/oauth/authorize"
token_url = "https://www.strava.com/oauth/token"
activities_url = "https://www.strava.com/api/v3/athlete/activities"
client_id = os.getenv("client_id")
client_secret = os.getenv('client_secret')
refresh_token = os.getenv('refresh_token')
scope="activity:read_all"


def generate_auth_url():
    params = {
        "client_id": client_id,
        "response_type": "code",  
        "redirect_uri": "http://localhost/exchange_token",
        "scope": scope,
    }
    return f"{auth_url}?{urlencode(params)}"


def get_auth_code():
    """
    Get authorization code from user login
    Returns:
        str: Authorization code
    """
    auth_url = generate_auth_url()
    webbrowser.open(auth_url)

    url = input("Paste the redirected URL here: ")
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return query_params.get("code", [None])[0]