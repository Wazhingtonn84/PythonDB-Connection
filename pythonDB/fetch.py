import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="SOFTWARE"
)

mycursor=mydb.cursor()
mycursor.execute("SELECT *FROM STUDENTS_DETAILS")
for i in mycursor:
    print(i)
