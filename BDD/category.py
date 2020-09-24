from peewee import *
import database

class Category(Model):
    name = CharField()

    class Meta:
        database = database.db