from mysql.connector import connect
from getpass import getpass
db=connect(
    host='localhost',
    user=input('User: '),
    password=getpass(),
    database='RealEstateDB',
    collation='utf8mb4_unicode_520_ci'
)
