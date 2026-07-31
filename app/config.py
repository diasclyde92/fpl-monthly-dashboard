from dotenv import load_dotenv
import os

load_dotenv()

LEAGUE_ID = os.getenv("LEAGUE_ID")

BASE_URL = "https://fantasy.premierleague.com/api"

BOOTSTRAP_URL = f"{BASE_URL}/bootstrap-static/"

LEAGUE_URL = f"{BASE_URL}/leagues-classic/{LEAGUE_ID}/standings/"

ENTRY_HISTORY_URL = f"{BASE_URL}/entry/{{}}/history/"

HEADERS = {

    "User-Agent": "Mozilla/5.0",

    "Accept": "application/json"

}