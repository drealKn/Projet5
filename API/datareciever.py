"""
This is the datareciever module, it gets the data from the OpenFoodFacts API
"""

import requests
import os


class DataReciever:
    """This class handles the function to recieve the data from the API"""
    def __init__(self, url):
        self.request_url = url
        self.index = 0
        self.request_params = {
            "action": "process",
            "sort_by": "unique_scans_n",
            "tag_type_0": "countries",
            "tag_contains_0": "contains",
            "tag_0": "fr",
            "page_size": os.getenv("PAGE_SIZE"),
            "page": self.index,
            "json": True,
        }

    def get_data(self):
        """This is the function that gets the data from the API"""
        data = requests.get(self.request_url, self.request_params)
        self.request_params["page"] = self.index
        try:
            data.status_code == 200
        except:
            print("Unable to get the request, please try again")
        return data.json()["products"]
