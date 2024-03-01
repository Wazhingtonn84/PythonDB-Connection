import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="wazhingtonn3184"
)
mycursor=mydb.cursor()
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)