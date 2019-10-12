from os import path, getcwd
import pymysql


class Database:

    def __init__(self):
        # in local change to self.connection = pymysql.connect("localhost","root","valaparla","face" ) depends on in config

        self.connection = pymysql.connect("localhost","root","valaparla","face" )
    def query(self, q, arg=()):
        
        cursor = self.connection.cursor()

        cursor.execute(q, arg)
        results = cursor.fetchall()
        cursor.close()

        return results

    def insert(self, q, arg=()):
        
        cursor = self.connection.cursor()
        cursor.execute(q, arg)
        self.connection.commit()
        result = cursor.lastrowid
        cursor.close()
        return result

    def select(self, q, arg=()):
        
        cursor = self.connection.cursor()
        cursor.execute(q, arg)
        return cursor.fetchall()

    def delete(self, q, arg=()):
       
        cursor = self.connection.cursor()
        result = cursor.execute(q, arg)
        self.connection.commit()
        return result
