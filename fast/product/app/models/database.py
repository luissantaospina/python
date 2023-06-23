from peewee import MySQLDatabase

database = MySQLDatabase(
    'product-fast',
    user='root',
    password='',
    host='localhost',
    port=3306
)
