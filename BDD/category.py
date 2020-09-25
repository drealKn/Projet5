from peewee import *
import BDD.database


class Category(Model):
    name = CharField()

    class Meta:
        database = BDD.database.mysql_db