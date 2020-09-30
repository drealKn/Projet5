from peewee import *

mysql_db = MySQLDatabase(
            "testdb2", 
            user = "root", 
            passwd = "dkanaMYSQL2!", 
            host = "localhost"
        )

class BaseModel(Model):
    class Meta:
        database = mysql_db

class Category(BaseModel):    
    name = CharField(unique = True)

class Product(BaseModel):    
    name = CharField()
    code = BigIntegerField()
    url = CharField()
    brands = CharField()
    stores = TextField()
    nutriscore = CharField()
    categories = ForeignKeyField(model = Category, backref = 'categories')
