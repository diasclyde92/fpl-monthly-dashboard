from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DATA = ROOT / "data"

WEBSITE = ROOT / "website"

RAW_DATA = DATA / "raw_data.json"

LEADERBOARD = DATA / "leaderboard.json"

DATA.mkdir(exist_ok=True)

WEBSITE.mkdir(exist_ok=True)