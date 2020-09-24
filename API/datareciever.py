import requests
import os


class DataReciever():
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
            "json": True
        }

    def get_data(self):
        data = requests.get(self.request_url, self.request_params)
        self.request_params['page'] = self.index
        try:
            data.status_code == 200
        except:
            print("Unable to get the request, please try again")        
        print("Downloading products : " + str(self.index * (100/int(os.getenv("PAGE_NUM"))))+ "%")
        return data.json()['products']
        