"""
This module handles the different tables of the database
"""

import peewee
import os
from dotenv import load_dotenv

load_dotenv()

mysql_db = peewee.MySQLDatabase(
    "substitutsdb", user=os.getenv("MYSQLUSER"), passwd=os.getenv("MYSQLPWD"), host=os.getenv("MYSQLPWD")
)


class BaseModel(peewee.Model):
    class Meta:
        database = mysql_db


class Category(BaseModel):
    id = peewee.PrimaryKeyField(primary_key=True)
    name = peewee.CharField(50)


class Product(BaseModel):
    id = peewee.PrimaryKeyField(primary_key=True)
    name = peewee.CharField(50)
    code = peewee.IntegerField()
    url = peewee.CharField(50)
    brands = peewee.CharField(50)
    stores = peewee.CharField(50)
    nutriscore = peewee.CharField(50)


class Product_Categories(BaseModel):
    id = peewee.PrimaryKeyField(primary_key=True)
    category = peewee.ForeignKeyField(model=Category, backref="category")
    product = peewee.ForeignKeyField(model=Product, backref="product")


class Favorites(BaseModel):
    id = peewee.PrimaryKeyField(primary_key=True)
    product = peewee.ForeignKeyField(model=Product, backref="favorites")
    