import sys
import mysql.connector
import pymysql
import datetime
from tabulate import tabulate
def allreports():
    connection = pymysql.connect(host="localhost", user="root", password="", database="billiing_system")
    cursor = connection.cursor()
    query1="SELECT * FROM stocks"
    query2="SELECT * FROM customer"
    cursor.execute(query1)
    result1=cursor.fetchall()
    cursor.execute(query2)
    result2=cursor.fetchall()
    print(tabulate(result1,headers=['product','Quantity','price'],tablefmt='psql'))
    print(tabulate(result2,headers=['Name','Phone_number','Date1','Date2','Date3'],tablefmt='psql'))
    connection.commit()
    cursor.close()
