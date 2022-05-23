
'''
#display gender
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="205101tejaT@",
    database="teja"
)
mycursor=mydb.cursor()
mycursor.execute("SELECT gender FROM book")
myresult=mycursor.fetchall()
for i in myresult:
    print(i)

#age
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="205101tejaT@",
    database="teja"
)
mycursor=mydb.cursor()
mycursor.execute("SELECT age FROM book where age>20")
myresult=mycursor.fetchall()
for i in myresult:
    print(i)

#sal
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="205101tejaT@",
    database="teja"
)
mycursor=mydb.cursor()
mycursor.execute("SELECT sal FROM book where sal>10000")
myresult=mycursor.fetchall()
for i in myresult:
    print(i)
'''