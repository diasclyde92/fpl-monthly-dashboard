from pathlib import Path

folders = [
    "data",
    "scripts",
    "website",
    ".github/workflows"
]

files = [
    "scripts/config.py",
    "scripts/fetch_data.py",
    "scripts/calculate_monthly.py",
    "website/index.html",
    "website/style.css",
    "website/script.js",
    "requirements.txt",
    "README.md",
    ".gitignore",
    ".env"
]

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

for file in files:
    Path(file).touch(exist_ok=True)

print("✅ Project structure created successfully!")