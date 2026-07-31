from pathlib import Path

PROJECT = {
    "folders": [
        "app",
        "scripts",
        "website",
        "website/assets",
        "data",
        ".github/workflows",
    ],
    "files": [
        ".env",
        ".gitignore",
        "README.md",
        "requirements.txt",
        "main.py",

        "app/__init__.py",
        "app/config.py",
        "app/paths.py",
        "app/api.py",
        "app/calculator.py",
        "app/models.py",
        "app/utils.py",

        "scripts/fetch_data.py",
        "scripts/build_dashboard.py",

        "website/index.html",
        "website/style.css",
        "website/script.js",

        ".github/workflows/update.yml",
    ]
}

for folder in PROJECT["folders"]:
    Path(folder).mkdir(parents=True, exist_ok=True)

for file in PROJECT["files"]:
    Path(file).touch(exist_ok=True)

print("=" * 50)
print("✅ FPL Monthly Dashboard Project Created")
print("=" * 50)

print("\nFolders:")

for folder in PROJECT["folders"]:
    print("📁", folder)

print("\nFiles:")

for file in PROJECT["files"]:
    print("📄", file)

print("\nReady to code 🚀")