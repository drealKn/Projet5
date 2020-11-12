import mysql.connector as mysql
import peewee
import BDD.tables


class Database():
    def __init__(self):
        self.db = mysql.connect(
            host = "localhost",
            user = "root",
            passwd = "dkanaMYSQL2!"
        )
        self.delete_database()
        try:
            self.create_db()
        except:
            print("Database already exists !")
        self.mysql_db = self.peewee_connect()
        self.create_tables()

    def create_db(self):
        cursor = self.db.cursor()

        cursor.execute("CREATE DATABASE testdb5")

    def delete_database(self):
            cursor = self.db.cursor()            
            cursor.execute("DROP DATABASE testdb5")
            self.db.commit()            

    def peewee_connect(self):
        mysql_db = peewee.MySQLDatabase(
            "testdb5", 
            user = "root", 
            passwd = "dkanaMYSQL2!", 
            host = "localhost"
        )

        return mysql_db
    
    def create_tables(self):
        try:
            BDD.tables.Category.create_table()
        except peewee.OperationalError:
            print ("Category table already exists!")
    
        try:
            BDD.tables.Product.create_table()
        except peewee.OperationalError:
            print ("Product table already exists!")

        try:
            BDD.tables.Product_Categories.create_table()
        except peewee.OperationalError:
            print ("Product_Categories table already exists!")

        try:
            BDD.tables.Favorites.create_table()
        except peewee.OperationalError:
            print ("Favorites table already exists!")

    def add_categories(self, data):        
        for product in data:
            category_names = product[4].split(',')
            for category in category_names:           
                BDD.tables.Category.get_or_create(name=category)

    def add_products(self, data):
        for product in data:
            BDD.tables.Product.get_or_create(name=product[0], url=product[1], brands=product[2], stores=product[3], nutriscore=product[5], code=int(product[6]))

    def add_category_by_product(self, data):
        for product in data:
            query1 = BDD.tables.Product.select().where(BDD.tables.Product.name == product[0])
            for row1 in query1:
                product_id = row1.id
            category_list = product[4].split(',')
            for category in category_list:
                query2 = BDD.tables.Category.select().where(BDD.tables.Category.name == category)
                for row2 in query2:
                    category_id = row2.id
                BDD.tables.Product_Categories.get_or_create(category = category_id, product = product_id)

    def get_categories(self):
        query = BDD.tables.Category.select().order_by(peewee.fn.Rand()).limit(9)
        categories = [row.name for row in query]
        return categories

    def get_products(self, category):
        category = BDD.tables.Category.select().where(BDD.tables.Category.name == category)
        category_id = category[0].id
        query = BDD.tables.Product_Categories.select(BDD.tables.Product_Categories.product).where(BDD.tables.Product_Categories.category == category_id).order_by(peewee.fn.Rand()).limit(9)
        products_id = [row.product for row in query]
        products_names = []
        for product_id in products_id:
            query = BDD.tables.Product.select(BDD.tables.Product.name).where(BDD.tables.Product.id == product_id)
            for row in query:
                products_names.append(row.name)
        return products_names

    def get_substitutes(self, product):
        product_query = BDD.tables.Product.select().where(BDD.tables.Product.name == product)
        product_id = product_query[0].id
        product_nutriscore = product_query[0].nutriscore
        query1 = BDD.tables.Category.select(BDD.tables.Category.id).join(BDD.tables.Product_Categories).where(BDD.tables.Product_Categories.product == product_id)
        categories_id = [row.id for row in query1]        
        substitute_list = []
        count = 0
        for category in categories_id:
            query2 = BDD.tables.Product.select().join(BDD.tables.Product_Categories).where(BDD.tables.Product_Categories.category == category and BDD.tables.Product.nutriscore <= product_nutriscore)
            name_list = [row.name for row in query2]
            substitute_nutriscore = query2[0].nutriscore
            if len(name_list) > count and substitute_nutriscore < product_nutriscore:
                substitute_list = [name_list[0]]
                count = len(name_list)
                product_nutriscore = substitute_nutriscore
            elif len(name_list) == count and substitute_nutriscore < product_nutriscore:
                substitute_list = [name_list[0]]
            elif len(name_list) > count and substitute_nutriscore == product_nutriscore:
                substitute_list = [name_list[0]]
                count = len(name_list)
            elif len(name_list) == count and substitute_nutriscore == product_nutriscore:
                substitute_list.append(name_list[0])
        return substitute_list
