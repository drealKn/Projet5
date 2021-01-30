"""
This module handles the creation of the database and the different queries to the database
to get categories, products, favorites and substitutes within the program
"""

import mysql.connector as mysql
import peewee
import os
from dotenv import load_dotenv
from tqdm import tqdm
import BDD.tables

load_dotenv()


class Database:
    def __init__(self):
        self.db = mysql.connect(
            host=os.getenv("MYSQLHOST"),
            user=os.getenv("MYSQLUSER"),
            passwd=os.getenv("MYSQLPWD"),
        )
        try:
            self.create_db()
        except:
            print("Database already exists !")
        self.mysql_db = self.peewee_connect()
        self.create_tables()

    def create_db(self):
        """This function create the database"""
        cursor = self.db.cursor()

        cursor.execute("CREATE DATABASE substitutsdb")

    def delete_database(self):
        """This function delete the database"""
        cursor = self.db.cursor()
        cursor.execute("DROP DATABASE substitutsdb")
        self.db.commit()

    def peewee_connect(self):
        """This function handles the connection to the database"""
        mysql_db = peewee.MySQLDatabase(
            "substitutsdb", user=os.getenv("MYSQLUSER"), passwd=os.getenv("MYSQLPWD"), host=os.getenv("MYSQLHOST")
        )

        return mysql_db

    def create_tables(self):
        """This function handles the creation of the different tables of the database"""
        try:
            BDD.tables.Category.create_table()
        except peewee.OperationalError:
            print("Category table already exists!")

        try:
            BDD.tables.Product.create_table()
        except peewee.OperationalError:
            print("Product table already exists!")

        try:
            BDD.tables.Product_Categories.create_table()
        except peewee.OperationalError:
            print("Product_Categories table already exists!")

        try:
            BDD.tables.Favorites.create_table()
        except peewee.OperationalError:
            print("Favorites table already exists!")

    def add_categories(self, data):
        """This function adds the categories into the database"""
        for product in tqdm(data):
            category_names = product[4].split(",")
            for category in category_names:
                BDD.tables.Category.get_or_create(name=category)

    def add_products(self, data):
        """This function adds the products to the database"""
        for product in tqdm(data):
            BDD.tables.Product.get_or_create(
                name=product[0],
                url=product[1],
                brands=product[2],
                stores=product[3],
                nutriscore=product[5],
                code=int(product[6]),
            )

    def add_category_by_product(self, data):
        """This function adds the ids of the categories
        linked to the products in the intermediate table"""
        for product in tqdm(data):
            query1 = BDD.tables.Product.select().where(
                BDD.tables.Product.name == product[0]
            )
            for row1 in query1:
                product_id = row1.id
            category_list = product[4].split(",")
            for category in category_list:
                query2 = BDD.tables.Category.select().where(
                    BDD.tables.Category.name == category
                )
                for row2 in query2:
                    category_id = row2.id
                BDD.tables.Product_Categories.get_or_create(
                    category=category_id, product=product_id
                )

    def get_categories(self):
        """This function handles the query to get the different categories"""
        query = BDD.tables.Category.select().order_by(peewee.fn.Rand()).limit(9)
        categories = [row.name for row in query]
        return categories

    def get_products(self, category):
        """This function handles the query to get
        the products linked to the chosen category"""
        category = BDD.tables.Category.select().where(
            BDD.tables.Category.name == category
        )
        category_id = category[0].id
        query = (
            BDD.tables.Product_Categories.select(BDD.tables.Product_Categories.product)
            .where(BDD.tables.Product_Categories.category == category_id)
            .order_by(peewee.fn.Rand())
            .limit(9)
        )
        products_id = [row.product for row in query]
        products_names = []
        for product_id in products_id:
            query = BDD.tables.Product.select(BDD.tables.Product.name).where(
                BDD.tables.Product.id == product_id
            )
            for row in query:
                products_names.append(row.name)
        return products_names

    def _get_substitute_nutriscore(self, substitute):
        """This function handles the query to get
        the nutriscore of the substitute for the chosen product"""
        substitute_query = BDD.tables.Product.select().where(
            BDD.tables.Product.name == substitute
        )
        substitute_nutriscore = substitute_query[0].nutriscore
        return substitute_nutriscore

    def get_substitutes(self, product):
        """This function handles the query to get
        the substitutes of the chosen product"""
        product_query = BDD.tables.Product.select().where(
            BDD.tables.Product.name == product
        )
        product_id = product_query[0].id
        product_nutriscore = product_query[0].nutriscore
        query1 = (
            BDD.tables.Category.select(BDD.tables.Category.id)
            .join(BDD.tables.Product_Categories)
            .where(BDD.tables.Product_Categories.product == product_id)
        )
        categories_id = [row.id for row in query1]
        substitute_list = []
        count = 0
        common_products = (
            BDD.tables.Product.select()
            .join(BDD.tables.Product_Categories)
            .where(BDD.tables.Product_Categories.category << categories_id)
        )
        common_products_list = [
            row.name for row in common_products if row.name != product
        ]
        common_products_list_distinct = []
        for i in range(len(common_products_list)):
            if common_products_list[i] not in common_products_list_distinct:
                common_products_list_distinct.append(common_products_list[i])
        for substitute in common_products_list_distinct:
            substitute_count = common_products_list.count(substitute)
            substitute_nutriscore = self._get_substitute_nutriscore(substitute)
            if substitute_count > count and substitute_nutriscore < product_nutriscore:
                substitute_list = [substitute]
                count = substitute_count
                product_nutriscore = substitute_nutriscore
            elif (
                substitute_count == count and substitute_nutriscore < product_nutriscore
            ):
                substitute_list = [substitute]
                product_nutriscore = substitute_nutriscore
            elif (
                substitute_count > count and substitute_nutriscore == product_nutriscore
            ):
                substitute_list = [substitute]
                count = substitute_count
            elif (
                substitute_count == count
                and substitute_nutriscore == product_nutriscore
            ):
                substitute_list.append(substitute)
        return substitute_list

    def get_favorites(self):
        """This function handles the query to get the saved favorites"""
        query = BDD.tables.Product.select().join(BDD.tables.Favorites)
        favorites = [row.name for row in query]
        return favorites

    def add_favorite(self, favorite):
        """This function add a product to the favorites if the user chose to do so"""
        query = BDD.tables.Product.select().where(BDD.tables.Product.name == favorite)
        for row in query:
            favorite_id = row.id
        BDD.tables.Favorites.get_or_create(product=favorite_id)