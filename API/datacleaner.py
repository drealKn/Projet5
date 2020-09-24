"""DataCleaner module"""

class DataCleaner():
    def __init__(self, data_to_clean):
        self.data_to_clean = data_to_clean
        self.clean_data = []
        self.first_cleaning()

    def first_cleaning(self):
        for i in range(len(self.data_to_clean)):
            if self.data_to_clean[i].get('product_name_fr') and self.data_to_clean[i].get('url') and self.data_to_clean[i].get('brands') and self.data_to_clean[i].get('stores') and self.data_to_clean[i].get('categories') and self.data_to_clean[i].get('nutriscore_grade') and self.data_to_clean[i].get('code'):
                self.clean_data.append([self.data_to_clean[i].get('product_name_fr'), self.data_to_clean[i].get('url'), self.data_to_clean[i].get('brands'), [self.data_to_clean[i].get('stores').capitalize()], [self.data_to_clean[i].get('categories')], self.data_to_clean[i].get('nutriscore_grade').upper(), self.data_to_clean[i].get('code')])
