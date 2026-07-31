import requests


def get_json(url, headers):
    """
    Download JSON safely.
    """

    response = requests.get(url, headers=headers, timeout=30)

    response.raise_for_status()

    return response.json()