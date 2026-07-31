import sys

from scripts.fetch_data import fetch
from scripts.build_dashboard import build


def main():

    if len(sys.argv) != 2:

        print("""
Usage

python main.py fetch
python main.py build
""")
        return

    command = sys.argv[1].lower()

    if command == "fetch":
        fetch()

    elif command == "build":
        build()

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()