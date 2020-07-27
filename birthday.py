import sys
import mysql.connector
import pymysql
import datetime
def temp():
    t=1
    t=int(t)
    tt=1
    tt=int(tt)
    date=[100]
    connection = pymysql.connect(host="localhost", user="root", password="", database="billiing_system")
    cursor = connection.cursor()
    print("Enter your name:")
    name = input()
    print("Enter your phone number")
    phno = input()
    print("enter your birthdate\neg:-12/02/2001")
    date[0]=input()
    print("enter any one or two dates of your relatives or your closed ones")
    date.append('')
    date.append('')
    while t<3:
        tt = int(input("enter 1 to continue 3 to stop"))
        if tt == 3:
            t = tt
        else:
            date[t] = input("enter the date")
            t+=1
            tt+=1
    query = "INSERT INTO customer (Name,Ph_no,imp_dates,imp_dates1,imp_dates2) VALUES (%s,%s,%s,%s,%s);"
    cursor.execute(query, (name, phno, date[0],date[1],date[2]))
    connection.commit()
    cursor.close()