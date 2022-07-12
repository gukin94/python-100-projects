import requests
from datetime import datetime, timedelta

FLIGHT_SEARCH_API_ENDPOINT = "https://tequila-api.kiwi.com/"
API_KEY = "-wElHJFXPxpfhNqXfq-iArS7NowbGZLa"

TODAY = datetime.today()
TOMORROW = TODAY + timedelta(days=1)
SIX_MONTHS_LATER = TODAY + timedelta(days=180)


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.header = {
            "apikey": API_KEY,
            "Content-Type": "application/json"}
        self.parameters = {}
        self.search_location_endpoint = FLIGHT_SEARCH_API_ENDPOINT + "locations/query"
        self.response = None

    def iata_search(self, city_name):
        self.parameters = {
            "term": "Paris"}

        self.response = requests.get(url=self.search_location_endpoint, params=self.parameters, headers=self.header)
        print(self.response.json())
        return "TESTING"


