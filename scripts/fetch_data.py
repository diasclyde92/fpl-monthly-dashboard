from app.api import FPLApi
from app.config import (
    HEADERS,
    LEAGUE_URL,
    BOOTSTRAP_URL,
    ENTRY_HISTORY_URL
)
from app.paths import RAW_DATA
from app.utils import save_json


def fetch():

    api = FPLApi(HEADERS)

    print("=" * 50)
    print("Downloading League")
    print("=" * 50)

    league = api.get(LEAGUE_URL)

    standings = league["standings"]["results"]

    print(f"Managers : {len(standings)}")

    print("\nDownloading Bootstrap")

    bootstrap = api.get(BOOTSTRAP_URL)

    managers = []

    print("\nDownloading Manager Histories\n")

    total = len(standings)

    for index, manager in enumerate(standings, start=1):

        history = api.get(
            ENTRY_HISTORY_URL.format(manager["entry"])
        )

        managers.append({

            "entry": manager["entry"],
            "player_name": manager["player_name"],
            "entry_name": manager["entry_name"],
            "rank": manager["rank"],
            "total": manager["total"],
            "history": history["current"]

        })

        print(f"[{index}/{total}] {manager['player_name']}")

    output = {

        "league": league["league"],

        "bootstrap": bootstrap,

        "managers": managers

    }

    save_json(RAW_DATA, output)

    print()
    print("=" * 50)
    print("raw_data.json saved successfully")
    print("=" * 50)