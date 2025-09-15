import requests
from urllib.parse import urlencode, urlparse, parse_qs
from dotenv import load_dotenv

load_dotenv()

activities_url = "https://www.strava.com/api/v3/athlete/activities"
 
def get_activities(access_token, per_page=200):
    """
    Fetch all activities from Strava API.
    Args:
        access_token (str): OAuth access token with activity:read or activity:read_all scope.
        per_page (int): Number of activities per page.
        Returns:
        list: List of activity objects.
    """
    
    all_activities = []
    page = 1
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"page": page, "per_page": per_page}

    while True:
        response = requests.get(activities_url, headers=headers, params=params)
        
        if response.status_code == 200:
            activities = response.json()
            if not activities:  # No activities left
                break
            # Append new activities to the list
            all_activities.extend(activities)
            page += 1
            params["page"] = page

        else:
            print("Error fetching:", response.json())
            break

    return all_activities