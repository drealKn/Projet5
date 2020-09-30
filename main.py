import API
import BDD
import Program
import os
from dotenv import load_dotenv

load_dotenv()

api_url = os.getenv("API_URL")
number_of_pages = os.getenv("PAGE_NUM")

program = Program.program.Program()
request = API.datareciever.DataReciever(api_url)
cleaner = API.datacleaner.DataCleaner()

for i in range(int(number_of_pages)):
    request.index += 1
    data_to_clean = request.get_data()
    cleaner.cleaning(data_to_clean)

db = BDD.database.Database()

db.add_categories(cleaner.clean_data)
db.add_products(cleaner.clean_data)

#print(cleaner.clean_data)