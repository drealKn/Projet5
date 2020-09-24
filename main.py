import API
import BDD
import os
from dotenv import load_dotenv

load_dotenv()

api_url = os.getenv("API_URL")
number_of_pages = os.getenv("NUMBER_OF_PAGES")

request = API.datareciever.DataReciever(api_url)

data_to_clean = request.get_data()

cleaning = API.datacleaner.DataCleaner(data_to_clean)

