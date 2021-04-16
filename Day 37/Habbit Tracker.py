import requests
from datetime import datetime as dt


# Step 1 - Create your user account
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "prit"
TOKEN = ""
GRAPH_ID = "graph1"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Run this create a new user
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)


# Step 2 - Create a graph definition
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Run this to create a new graph
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)


# Step 3 - Get the graph!
# https://pixe.la/v1/users/a-know/graphs/test-graph.html


# Step 4 - Post value to the graph
pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = dt(year=2021, month=4, day=16)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2.4",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)


# Step 5 - Refresh the graph
# https://pixe.la/v1/users/a-know/graphs/test-graph.html


#-----------------------------------------------------------------------#


# Update the pixels
update_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}'

new_pixel_data = {
    "quantity": "3.2"
}

# Run this code to update pixel
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


# Delete a pixel
delete_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}'

# Run this code to delete a pixel
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)


# Update a graph
update_graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

graph_update_data = {
    "color": "shibafu"
}

# Run this code to update the graph
# response = requests.put(url=update_graph_endpoint, json=graph_update_data, headers=headers)
# print(response.text)