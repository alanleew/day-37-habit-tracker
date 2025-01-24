import requests

TOKEN = "asdfghjkl"
USERNAME = "alanleew"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Code below is for creating an account. If you run again, account is already created!
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "mi",
    "type": "float",
    "color": "sora",
}
requests.post(url=graph_endpoint,)