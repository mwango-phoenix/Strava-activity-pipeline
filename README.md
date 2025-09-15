#  Strava Activity Pipeline

A Python project that connects to the Strava API, retrieves activity data, and exports them into structured format (CSV) for analysis and visualization (e.g., in Power BI).

---

##  Features
- OAuth 2.0 authentication with Strava  
- Automatic token exchange for secure API access  
- Fetches all activities and details
- Prepares data as CSV

---

## How to use
1. Clone the repo
2. Install dependencies (dotenv)
3. Go to [Strava Developer](https://www.strava.com/settings/api) and get your client id and client secret. Update them in .env
4. Run the script `python pipeline.py`

This will create a file strava_activities.csv for your use
