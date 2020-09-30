import mysql.connector as mysql
from peewee import *
import BDD.tables


class Database():
    def __init__(self):
        self.db = mysql.connect(
            host = "localhost",
            user = "root",
            passwd = "dkanaMYSQL2!"
        )
        #self.create_db()
        self.mysql_db = self.peewee_connect()
        self.create_tables()

    def create_db(self):
        cursor = self.db.cursor()

        cursor.execute("CREATE DATABASE testdb2")

    def peewee_connect(self):
        mysql_db = MySQLDatabase(
            "testdb", 
            user = "root", 
            passwd = "dkanaMYSQL2!", 
            host = "localhost"
        )

        return mysql_db
    
    def create_tables(self):
        try:
            BDD.tables.Category.create_table()
        except OperationalError:
            print ("Category table already exists!")
    
        try:
            BDD.tables.Product.create_table()
        except OperationalError:
            print ("Product table already exists!")

    def add_categories(self, data):
        key = ['name']
        categories_to_add = []

        for product in data:
            if product[4][0] not in categories_to_add:
                categories_to_add.append(dict(zip(key, product[4][0])))

        with self.mysql_db.atomic():
            query = BDD.tables.Category.insert_many(categories_to_add)
            query.execute()

    def add_products(self, data):
        keys = ['name', 'url', 'brands', 'stores', 'categories', 'nutriscore', 'code']
        products_to_add = []

        for product in data:
            product[3] = product[3][0]
            product[4] = BDD.tables.Category.select(BDD.tables.Category.index).where(BDD.tables.Category.name == product[4][0])
            products_to_add.append(dict(zip(keys, product)))

        with self.mysql_db.atomic():
            query = BDD.tables.Product.insert_many(products_to_add)
            query.execute()

        test = BDD.tables.Product.select()
        print(test)

