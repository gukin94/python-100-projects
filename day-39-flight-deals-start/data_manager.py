import requests

FLIGHT_DEALS_ENDPOINT = "https://api.sheety.co/8a1193a659d279e3e48a595d51597e2e/flightDeals/prices"
SHEET_CELL_NAME = 'prices'

class DataManager:
    def __init__(self):
        self.response = requests.get(url=FLIGHT_DEALS_ENDPOINT)
        self.data = self.response.json()
        self.iata_record = {}

    def sheet_data(self):
        """it returns sheet data"""
        return self.data[SHEET_CELL_NAME]

    def iata_update(self, code, row_num):
        self.iata_record = {
            "price": {
                "iataCode": code
            }
        }
        requests.put(url=FLIGHT_DEALS_ENDPOINT+f'/{row_num}', json=self.iata_record)