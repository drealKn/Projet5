import API
import BDD
import Program
import os
from tqdm import tqdm
from dotenv import load_dotenv

os.system("clear")

load_dotenv()

api_url = os.getenv("API_URL")
number_of_pages = os.getenv("PAGE_NUMB")

db = BDD.database.Database()

program = Program.program.Program(db)
request = API.datareciever.DataReciever(api_url)
cleaner = API.datacleaner.DataCleaner()

for i in tqdm(range(int(number_of_pages))):
    request.index += 1
    data_to_clean = request.get_data()
    cleaner.cleaning(data_to_clean)

db.add_categories(cleaner.clean_data)
db.add_products(cleaner.clean_data)
db.add_category_by_product(cleaner.clean_data)

program.menu()
