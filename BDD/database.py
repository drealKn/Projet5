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
        try:
            self.create_db()
        except:
            print("Database already exists !")
        self.mysql_db = self.peewee_connect()
        self.create_tables()

    def create_db(self):
        cursor = self.db.cursor()

        cursor.execute("CREATE DATABASE testdb5")

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
            BDD.tables.Favorites.create_table()
        except peewee.OperationalError:
            print ("Product table already exists!")

    def add_categories(self, data):        
        for product in data:            
            BDD.tables.Category.get_or_create(name=product[4])

    def add_products(self, data):
        for product in data:
            query = BDD.tables.Category.select(BDD.tables.Category.id).where(BDD.tables.Category.name == product[4])
            for row in query:
                category = row
            BDD.tables.Product.get_or_create(name=product[0], url=product[1], brands=product[2], stores=product[3],categories=category, nutriscore=product[5], code=int(product[6]))

    def get_categories(self):
        query = BDD.tables.Category.select().order_by(peewee.fn.Rand()).limit(5)
        categories = [row.name for row in query]
        return categories

    def get_products(self, category):
        category = BDD.tables.Category.select().where(BDD.tables.Category.name == category)
        category_id = category[0].id
        query = BDD.tables.Product.select().where(BDD.tables.Product.id == category_id).order_by(peewee.fn.Rand()).limit(9)
        products_names = [row.name for row in query]
        return products_names


