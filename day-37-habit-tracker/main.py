import requests
from datetime import datetime

USERNAME = "gukin"
pixela_endpoint = 'https://pixe.la/v1/users'
TOKEN = "lkj412lknelk54dlk4523ll"
ID_GRAPH = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": ID_GRAPH,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now().strftime("%Y%m%d")
# today = datetime(year=2022, month=7, day=8).strftime("%Y%m%d")
print(today)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID_GRAPH}"

pixel_data = {
    "date" : today,
    "quantity": input("how many cycle did you ride today?")
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
date_for_update = "20220707"

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID_GRAPH}/{date_for_update}"
update_data = {
    "quantity": "9"
}

# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID_GRAPH}/{today}"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
