import sys
import mysql.connector
import pymysql
import datetime
from tabulate import tabulate

def offers():
    '''
    connection = pymysql.connect(host="localhost", user="root", password="", database="billiing_system")
    cursor = connection.cursor()
    #query="INSERT INTO customer (`imp_dates`) VALUES (STR_TO_DATE('%d/%d/%d','%d/%m/%Y'))"
    query="SELECT imp_dates,imp_dates1,imp_dates2 FROM customer"
    cursor.execute(query)
    result=cursor.fetchall()
    for a,b,c in result:
        for t in a,b,c:
            if t == '' or t== None:
                continue
            else:
                res=t.split('/')
                print(res)
    connection.commit()
    cursor.close()'''
    print("for senior citizen:-20% discount\n")
    print("for couples:-15% discount\n")
    print("for age 25 above 10% discount\n")
    print("for kids less than 12 7% discount\n")



