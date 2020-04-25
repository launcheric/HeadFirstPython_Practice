# Telusko demo;

import mysql.connector

mydb = mysql.connector.connect(
                                host="localhost",
                                user="navin",
                                passwd="1234",
                                database="telusko_demo",)

mycursor = mydb.cursor()

mycursor.execute("select * from student")

result = mycursor.fetchall()

for i in mycursor:
    print(i)
