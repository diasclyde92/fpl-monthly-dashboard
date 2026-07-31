from collections import defaultdict
from datetime import datetime, UTC

from app.paths import RAW_DATA, LEADERBOARD
from app.utils import load_json, save_json

MONTH_ORDER = [
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


def get_event_month_lookup(events):

    lookup = {}

    for event in events:

        deadline = datetime.fromisoformat(
            event["deadline_time"].replace("Z", "+00:00")
        )

        lookup[event["id"]] = deadline.strftime("%B")

    return lookup


def build():

    raw = load_json(RAW_DATA)

    lookup = get_event_month_lookup(
        raw["bootstrap"]["events"]
    )

    monthly = defaultdict(list)

    overall = []

    for manager in raw["managers"]:

        totals = defaultdict(int)

        for gw in manager["history"]:

            month = lookup.get(gw["event"])

            if month in MONTH_ORDER:

                totals[month] += gw["points"]

        overall.append({

            "manager": manager["player_name"],
            "team": manager["entry_name"],
            "points": manager["total"]

        })

        for month in MONTH_ORDER:

            monthly[month].append({

                "manager": manager["player_name"],

                "team": manager["entry_name"],

                "points": totals[month]

            })

    # Monthly Ranking

    for month in MONTH_ORDER:

        monthly[month] = sorted(

            monthly[month],

            key=lambda x: x["points"],

            reverse=True

        )

        for rank, item in enumerate(monthly[month], start=1):

            item["rank"] = rank

    # Overall Ranking

    overall = sorted(

        overall,

        key=lambda x: x["points"],

        reverse=True

    )

    for rank, item in enumerate(overall, start=1):

        item["rank"] = rank

    output = {

        "generated_at": datetime.now(UTC).isoformat(),

        "league": raw["league"],

        "months": monthly,

        "overall": overall

    }

    save_json(

        LEADERBOARD,

        output

    )

    print()

    print("========================================")

    print("Leaderboard generated successfully")

    print("========================================")