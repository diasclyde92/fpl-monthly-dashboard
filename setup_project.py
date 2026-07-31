from pathlib import Path

PROJECT_NAME = "fpl-monthly-dashboard"

folders = [
    "data",
    "website",
    ".github/workflows",
]

files = {
    "main.py": "",
    "config.py": "",
    "requirements.txt": "",
    "README.md": "# FPL Monthly Dashboard\n",
    ".gitignore": "",
    "website/index.html": "",
    "website/style.css": "",
    "website/script.js": "",
    ".github/workflows/update.yml": "",
}

project = Path(PROJECT_NAME)

project.mkdir(exist_ok=True)

for folder in folders:
    (project / folder).mkdir(parents=True, exist_ok=True)

for file, content in files.items():
    path = project / file
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        path.write_text(content, encoding="utf-8")

print("=" * 50)
print("Project created successfully!")
print("=" * 50)
print(project.resolve())
print("\nFolder structure:\n")

for p in sorted(project.rglob("*")):
    indent = "    " * (len(p.relative_to(project).parts) - 1)
    print(f"{indent}{p.name}")