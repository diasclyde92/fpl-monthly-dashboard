import json
from collections import defaultdict
from datetime import datetime

import requests

from config import LEAGUE_URL, BOOTSTRAP_URL, ENTRY_HISTORY_URL
from pathlib import Path

Path("data").mkdir(exist_ok=True)

def get_json(url):
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.json()


print("Downloading league...")

league = get_json(LEAGUE_URL)

print("Downloading bootstrap...")

bootstrap = get_json(BOOTSTRAP_URL)

print("Building month lookup...")

month_lookup = {}

for event in bootstrap["events"]:
    dt = datetime.fromisoformat(
        event["deadline_time"].replace("Z", "+00:00")
    )

    month_lookup[event["id"]] = dt.strftime("%B")


histories = {}

print("Downloading manager histories...")

for manager in league["standings"]["results"]:

    entry = manager["entry"]

    print(manager["player_name"])

    histories[entry] = get_json(
        ENTRY_HISTORY_URL.format(entry)
    )


print("Saving raw data...")

with open("data/raw.json", "w", encoding="utf8") as f:
    json.dump(
        {
            "league": league,
            "bootstrap": bootstrap,
            "histories": histories,
        },
        f,
        indent=4,
    )


overall = []

monthly = defaultdict(list)


print("Calculating monthly leaderboard...")

for manager in league["standings"]["results"]:

    entry = manager["entry"]

    history = histories[entry]["current"]

    totals = defaultdict(int)

    for gw in history:

        month = month_lookup[gw["event"]]

        totals[month] += gw["points"]

    overall.append(
        {
            "rank": manager["rank"],
            "manager": manager["player_name"],
            "team": manager["entry_name"],
            "points": manager["total"],
        }
    )

    for month, pts in totals.items():

        monthly[month].append(
            {
                "manager": manager["player_name"],
                "team": manager["entry_name"],
                "points": pts,
            }
        )


for month in monthly:

    monthly[month].sort(
        key=lambda x: x["points"],
        reverse=True,
    )

    for rank, manager in enumerate(monthly[month], start=1):

        manager["rank"] = rank


dashboard = {
    "league_name": league["league"]["name"],
    "last_updated": datetime.now().strftime("%d %B %Y %H:%M"),
    "overall": overall,
    "months": monthly,
}

print("Saving dashboard...")

with open(
        "leaderboard.json",
    "w",
    encoding="utf8",
) as f:

    json.dump(dashboard, f, indent=4)

print("Done.")