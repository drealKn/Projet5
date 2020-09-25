import API
import BDD
import os
from dotenv import load_dotenv

load_dotenv()

api_url = os.getenv("API_URL")
number_of_pages = os.getenv("PAGE_NUM")


request = API.datareciever.DataReciever(api_url)
cleaner = API.datacleaner.DataCleaner()

for i in range(int(number_of_pages)):
    request.index += 1
    data_to_clean = request.get_data()
    cleaner.cleaning(data_to_clean)

#print(cleaner.clean_data)