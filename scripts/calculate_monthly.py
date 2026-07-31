import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path


MONTHS = [
    "August",
    "September",
    "October",
    "November",
    "December",
    "January",
    "February",
    "March",
    "April",
    "May"
]


def load_data():
    with open("data/raw_data.json", encoding="utf-8") as f:
        return json.load(f)


def event_month_lookup(events):
    """
    Maps Gameweek -> Month name using the deadline date.
    """
    lookup = {}

    for event in events:
        deadline = datetime.fromisoformat(
            event["deadline_time"].replace("Z", "+00:00")
        )

        lookup[event["id"]] = deadline.strftime("%B")

    return lookup


def build_monthly_table(raw):

    event_lookup = event_month_lookup(raw["bootstrap"]["events"])

    monthly = defaultdict(list)
    overall = []

    for manager in raw["managers"]:

        totals = defaultdict(int)

        for gw in manager["history"]:

            month = event_lookup.get(gw["event"])

            if month not in MONTHS:
                continue

            totals[month] += gw["points"]

        overall.append({
            "manager": manager["player_name"],
            "team": manager["entry_name"],
            "points": manager["total"]
        })

        for month in MONTHS:

            monthly[month].append({
                "manager": manager["player_name"],
                "team": manager["entry_name"],
                "points": totals[month]
            })

    # Sort each month
    for month in MONTHS:

        monthly[month] = sorted(
            monthly[month],
            key=lambda x: x["points"],
            reverse=True
        )

        # Assign ranks
        for rank, row in enumerate(monthly[month], start=1):
            row["rank"] = rank

    overall = sorted(
        overall,
        key=lambda x: x["points"],
        reverse=True
    )

    for rank, row in enumerate(overall, start=1):
        row["rank"] = rank

    return monthly, overall


def save(monthly, overall, league):

    output = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "league": league,
        "months": monthly,
        "overall": overall
    }

    with open("data/leaderboard.json", "w", encoding="utf-8") as f:
        json.dump(
            output,
            f,
            indent=4,
            ensure_ascii=False
        )

    print("✅ leaderboard.json created")


def main():

    raw = load_data()

    monthly, overall = build_monthly_table(raw)

    save(monthly, overall, raw["league"])


if __name__ == "__main__":
    main()