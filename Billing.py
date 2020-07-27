import sys
import mysql.connector
import pymysql
import datetime
from tabulate import tabulate
from stocks import stock_list

from temp1 import temp #F3 birthday/feedback
from bill_generation import Bill_generation #F2 bill generation
from reports import allreports
from offer_to_customer import offers
from get_date import date

now=datetime.datetime.now()

"""--------------------- main function-------------------------"""
flag=1
while flag:
    print("---------------------------AMBI'S CAFE-----------------------")
    print("choose the option to be executed:\n")
    print("1.Billing\n")
    print("2.report\n")
    print("3.stocks\n")
    print("4.offers\n")
    print("5.customer details\n")
    print("6.messaging\n")
    ch=int(input("enter your choice or press 7 to exit"))
    if ch == 1:
        total=0
        connection=pymysql.connect(host="localhost",user="root",password="",database="billiing_system")
        cursor=connection.cursor()
        query="SELECT product FROM stocks"
        cursor.execute(query)
        result=cursor.fetchall()
        print(tabulate(result, headers=['product'], tablefmt='psql'))
        for i in range(3):
            print("enter the product")
            product=input()
            print("enter the quantity")
            quantity=int(input())
            res=Bill_generation(product,quantity)
            total=total+res
        print('total=',total)
        connection.commit()
        cursor.close()
    elif ch == 2:
        print("-----------------------------Report--------------------------")
        allreports()
    elif ch == 3:
        print("----------------------------stocks---------------------------")
        stock_list()
    elif ch == 4:
        print("-------------------------Offers-------------------------------")
        offers()
    elif ch == 5:
        print("----------------------customer-details----------------")
        temp()
    elif ch == 6:
        print("------------------------messageing--------------------------")
        date()
    elif ch == 7:
        flag = 0
    else:
        print("enter a number with a valid function")








