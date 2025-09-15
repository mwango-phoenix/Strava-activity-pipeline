from strava_auth import get_auth_code
from gen_token import exchange_code_for_token
from get_activities import get_activities
import pandas as pd

def run_pipeline():
    # Step 1: Get auth code
    auth_code = get_auth_code()

    # failed to get auth code
    if not auth_code:
        return

    # Step 2: Get access token
    access_token = exchange_code_for_token(auth_code)

    # Step 3: Fetch all user activities
    activities = get_activities(access_token)

    # Step 4: Save activities to CSV
    activities_df = pd.DataFrame(activities)
    filename = "strava_activities.csv"

    activities_df.to_csv(filename, index=False, mode='w', header=True)
    print(f"Created new file and saved activities to {filename}")



if __name__ == "__main__":
    run_pipeline()
