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
     a. It will take you to this page <img width="552" height="536" alt="image" src="https://github.com/user-attachments/assets/bd4c2581-b873-4e78-a6f5-5f5998f7c4fa" />
         Click authorize and copy the link in the next page which will look like <img width="704" height="527" alt="image" src="https://github.com/user-attachments/assets/eda26c46-1321-401f-b5e2-ced2d5857be2" />
     b. Paste the link into the terminal <img width="309" height="28" alt="image" src="https://github.com/user-attachments/assets/32b7b9db-4092-480f-a492-6ba611454dc4" />


This will create a file strava_activities.csv for your use
