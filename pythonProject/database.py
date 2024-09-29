import mysql.connector

host = '127.0.0.1'
username = 'root'
password = 'admin'
database = 'demofastapi'

class db:
    mydb = mysql.connector.connect(
        host = host,
        user = username,
        password = password,
        database = database
    )

    def __init__(self):
        if self.mydb.is_connected():
            print('Done!')
        else:
            print('Not done!')
