from wsgiref import headers
import mysql.connector
import pymysql
import datetime
from tabulate import tabulate

def stock_list():
    connection = pymysql.connect(host="localhost", user="root", password="", database="billiing_system")
    cursor = connection.cursor()
    query1 = """SELECT * FROM stocks"""
    cursor.execute(query1)
    result = cursor.fetchall()
    print(tabulate(result,headers=['product','Quantity','price'],tablefmt='psql'))
    connection.commit()
    cursor.close()