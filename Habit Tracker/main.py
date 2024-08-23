import requests
from datetime import datetime
import os

USERNAME = "helloiamcoder"
TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token" : TOKEN,
    "username" : USERNAME, 
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_configuration = {
    "id" : GRAPH_ID,
    "name" : "Coding Graph",
    "unit" : "Hrs",
    "type" : "float",
    "color" : "momiji"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_configuration, headers=headers)
# print(response.text)

create_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
today_formatted = today.strftime("%Y%m%d")
create_pixel_configuration = {
    "date" : today_formatted,
    "quantity" : "1.5",
}

# response = requests.post(url=create_pixel_endpoint, json=create_pixel_configuration, headers=headers)
# print(response)

update_pixel_endpoint = f"{create_pixel_endpoint}/{today_formatted}"

new_pixel_data = {
    "quantity" : ".0"
}
# response = requests.put(url=update_pixel_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{update_pixel_endpoint}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)