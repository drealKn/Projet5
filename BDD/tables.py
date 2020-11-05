import peewee

mysql_db = peewee.MySQLDatabase(
            "testdb5", 
            user = "root", 
            passwd = "dkanaMYSQL2!", 
            host = "localhost"
        )

class BaseModel(peewee.Model):
    class Meta:
        database = mysql_db

class Category(BaseModel):
    id = peewee.PrimaryKeyField(primary_key = True)
    name = peewee.CharField(50)

class Product_Categories(BaseModel):
    pass

class Product(BaseModel):
    id = peewee.PrimaryKeyField(primary_key = True)
    name = peewee.CharField(50)
    code = peewee.IntegerField()
    url = peewee.CharField(50)
    brands = peewee.CharField(50)
    stores = peewee.CharField(50)
    nutriscore = peewee.CharField(50)
    categories = peewee.ForeignKeyField(model = Category, backref = 'categories')

class Favorites(BaseModel):
    id = peewee.PrimaryKeyField(primary_key = True)
    product = peewee.ForeignKeyField(model = Product, backref = 'favorites')
