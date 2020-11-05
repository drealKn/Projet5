"""DataCleaner module"""

class DataCleaner():
    def __init__(self):        
        self.clean_data = []        

    def cleaning(self, data_to_clean):
        for i in range(len(data_to_clean)):
            if data_to_clean[i].get('product_name_fr') and data_to_clean[i].get('url') and data_to_clean[i].get('brands') and data_to_clean[i].get('stores') and data_to_clean[i].get('categories') and data_to_clean[i].get('nutriscore_grade') and data_to_clean[i].get('code'):
                self.clean_data.append([data_to_clean[i].get('product_name_fr'), data_to_clean[i].get('url'), data_to_clean[i].get('brands'), [data_to_clean[i].get('stores').capitalize()], data_to_clean[i].get('categories').split(',')[0], data_to_clean[i].get('nutriscore_grade').upper(), data_to_clean[i].get('code')])