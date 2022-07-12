from flight_search import FlightSearch
from data_manager import DataManager
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.sheet_data()

for entry in enumerate(sheet_data):
    data = entry[1]
    row_num = entry[0] + 2
    iata_code = data['iataCode']

    if len(iata_code) == 0:  # if it doesn't contain IATA code.
        city_name = data['city']  # extract City name from sheet data.
        print(city_name)
        data_manager.iata_update(flight_search.iata_search(city_name), row_num)


