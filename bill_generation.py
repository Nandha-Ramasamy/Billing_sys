import sys
import mysql.connector
import pymysql
import datetime

def Bill_generation(product1,quantity1):
    connection = pymysql.connect(host="localhost", user="root", password="", database="billiing_system")
    cursor = connection.cursor()
    query="SELECT Quantity FROM stocks WHERE Product=%s"
    cursor.execute(query,product1)
    result=cursor.fetchone()
    result=int(result[0])
    if result-quantity1 > 0:
        query1="SELECT Price FROM stocks WHERE Product=%s"
        query2="UPDATE stocks SET Quantity=Quantity-%s WHERE Product=%s"
        cursor.execute(query1,(product1,))
        result=cursor.fetchone()
        result=int(result[0])
        cursor.execute(query2,(quantity1,product1,))
        connection.commit()
        cursor.close()
        return quantity1*result
        #print("stock updated successfully")
    else:
        print("Low on quantity")
        print('error:try again')


