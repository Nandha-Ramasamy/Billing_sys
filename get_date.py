import sys
import mysql.connector
import pymysql
import datetime
from tabulate import tabulate
from invitation import invitation_to_customers


def date():
    connection = pymysql.connect(host="localhost", user="root", password="", database="billiing_system")
    cursor = connection.cursor()
    query="SELECT name,Ph_no,imp_dates,imp_dates1,imp_dates2 FROM customer"
    cursor.execute(query)
    res=cursor.fetchall()
    for d,e,a,b,c in res:
        for all in a,b,c:
            da=all.split('/')
            if len(da) == 3:
                invitation_to_customers(d,e,int(str(da[0])),int(str(da[1])),int(str(da[2])))
