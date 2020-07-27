import sys
import mysql.connector
import pymysql
import datetime
from tabulate import tabulate
from message import message_send
now=datetime.datetime.now()

def invitation_to_customers (name,ph_no,d,m,y):
    if d is now.day and m is now.month:
        message_send(name,ph_no)
        '''print("Happy Birthday")
        print("you are ",now.year-y,"years old")
        print("There is surprise waiting for you")'''