import csv

import psycopg2
class Dbconnection:
    def __init__(self):
        db = psycopg2.connect (database="postgres", user='root', password='', host='127.0.0.1', port= '5432')
        self.cursor = db.cursor ()
        self.commit=db.commit()
    def query(self, sql):
        self.cursor.execute (sql)
        return self.cursor.fetchone ()

    def rows(self):
        return self.cursor.rowcount

    def getConnection(self):
        self.conn = psycopg2.connect(
        database="postgres", user='root', password='', host='127.0.0.1', port= '5432')
dbconnection=Dbconnection()
cursor=dbconnection.cursor
commit=dbconnection.commit

