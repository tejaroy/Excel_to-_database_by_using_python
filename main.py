import csv
import mysql.connector
import pandas as pd
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="205101tejaT@",
    database='teja'
)

with open("E:\\TOM.csv") as df:
    df=csv.reader(df,delimiter=',')
    all_value=[]
    for row in df:
        valu=(row[0],row[1],row[2],row[3],row[4],row[5])
        all_value.append(valu)
query="INSERT INTO book(name,gender,address,age,emp_id,sal) values (%s,%s,%s,%s,%s,%s)"
mycursor=mydb.cursor()
mycursor.executemany(query,all_value)
mydb.commit()

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
mycursor.execute("SELECT * FROM book")
myresult=mycursor.fetchall()

for i in myresult:
    print(i)



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
z=[]
for i in myresult:
    z.append(i)
print(z)


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
y=[]
for i in myresult:
    y.append(i)
print(y)


# sal
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="205101tejaT@",
    database="teja"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT sal FROM book where sal>10000")
myresult = mycursor.fetchall()
x = []
for i in myresult:
    x.append(i)
print(x)


#delecting row by using function
def de(id):
    import mysql.connector
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="205101tejaT@",
        database="teja"
    )
    mycursor=mydb.cursor()
    mycursor.execute("DELETE FROM book where sno= 'id'")
    mydb.commit()
de(1)


'''