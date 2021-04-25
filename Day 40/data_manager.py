#This class is responsible for talking to the Google Sheet.

import requests
import os
from dotenv import load_dotenv
from requests.models import Response


class DataManager:

    def __init__(self):
        load_dotenv()
        self.destination_data = {}


    def get_destination_data(self):
        response = requests.get(url=os.getenv("SHEETY_PRICES_ENDPOINT"))
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data


    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            Response = requests.put(
                url=f"{os.getenv('SHEETY_PRICES_ENDPOINT')}/{city['id']}",
                json=new_data
            )
            print(Response.text)