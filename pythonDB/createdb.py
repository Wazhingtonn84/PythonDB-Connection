import mysql.connector

# dataBase= mysql.connector.connect (host="localhost" user= "root" passwd="wazhingtonn3184")
dataBase=mysql.connector.connect(host="localhost", user="root", passwd="wazhingtonn3184")

cursorObject=dataBase.cursor()
cursorObject.execute("CREATE DATABASE SOFTWARE")
print("SOFTWARE DataBase is created")