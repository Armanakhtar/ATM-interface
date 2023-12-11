import pymysql
class DbConnection:
    @staticmethod
    def connection():
        con=pymysql.connect(host="localhost", user="root", password="Root", database="ATM")
        return con