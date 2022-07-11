import requests

FLIGHT_SEARCH_API_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
API_KEY = "-wElHJFXPxpfhNqXfq-iArS7NowbGZLa"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.header = {
            "apikey": API_KEY,
            "Content-Type": "application/json"}
        self.parameters = {
            "fly_from": "FRA",
            "date_from": "01/09/2022",
            "date_to": "02/09/2022"}
        self.response = requests.get(url=FLIGHT_SEARCH_API_ENDPOINT,
                                     params=self.parameters,
                                     headers=self.header)
        self.data = self.response.json()
        print(self.data)
        # print(self.response)

