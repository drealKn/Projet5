from peewee import *
import database

class Product(Model):
    name = CharField()
    code = IntField()
    url = CharField()
    brand = CharField()
    stores = CharField()
    nutriscore = CharField()
    categories = CharField()

    class Meta:
        database = database.db