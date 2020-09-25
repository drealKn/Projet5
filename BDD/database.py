import mysql.connector as mysql
from peewee import *

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "dkanaMYSQL2!"
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE project5")

mysql_db = MySQLDatabase(
    "project5", 
    user = "root", 
    passwd = "dkanaMYSQL2!", 
    host = "localhost"
)