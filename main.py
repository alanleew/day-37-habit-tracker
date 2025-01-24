import requests
from datetime import datetime

TOKEN = "asdfghjkl"
USERNAME = "alanleew"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "mi",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# https://pixe.la/v1/users/alanleew/graphs/graph1.html

today = datetime(year=2025, month=1, day=1).strftime("%Y%m%d")

# pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# pixel_config = {
#     "date": today,
#     "quantity": "10",
# }

# POST
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

# UPDATE
# update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
# update_pixel_config = {
#     "quantity": "0",
# }
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

# response = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(response.text)