import json
from pathlib import Path

from config import *
from utils import get_json


def main():

    print("=" * 50)
    print("Loading League")
    print("=" * 50)

    league = get_json(LEAGUE_URL, HEADERS)

    standings = league["standings"]["results"]

    print(f"Managers Found : {len(standings)}")

    print("\nLoading Bootstrap...")

    bootstrap = get_json(BOOTSTRAP_URL, HEADERS)

    managers = []

    print("\nDownloading manager histories...\n")

    for i, manager in enumerate(standings, start=1):

        entry = manager["entry"]

        history = get_json(
            ENTRY_HISTORY_URL.format(entry),
            HEADERS
        )

        managers.append({

            "entry": entry,
            "player_name": manager["player_name"],
            "entry_name": manager["entry_name"],
            "rank": manager["rank"],
            "total": manager["total"],
            "history": history["current"]

        })

        print(f"[{i}/{len(standings)}] {manager['player_name']}")

    output = {

        "league": league["league"],
        "bootstrap": bootstrap,
        "managers": managers

    }

    Path("data").mkdir(exist_ok=True)

    with open("data/raw_data.json", "w", encoding="utf-8") as f:

        json.dump(
            output,
            f,
            indent=4,
            ensure_ascii=False
        )

    print("\n✅ raw_data.json created successfully!")


if __name__ == "__main__":
    main()