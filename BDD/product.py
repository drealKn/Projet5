from peewee import *
import BDD.database


class Product(Model):
    name = CharField()
    code = IntegerField()
    url = CharField()
    brand = CharField()
    stores = CharField()
    nutriscore = CharField()
    categories = ForeignKeyField()

    class Meta:
        database = BDD.database.mysql_db