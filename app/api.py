import requests


class FPLApi:

    def __init__(self, headers):

        self.headers = headers

    def get(self, url):

        response = requests.get(

            url,

            headers=self.headers,

            timeout=30

        )

        response.raise_for_status()

        return response.json()