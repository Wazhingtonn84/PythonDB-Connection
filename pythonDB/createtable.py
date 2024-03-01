import mysql.connector
# connecting to the database
dataBase= mysql.connector.connect(host="localhost", user="root", passwd="wazhingtonn3184", database="SOFTWARE")
# preparing a cursor object
cursorObject= dataBase.cursor()
# creating table
studentRecord= """CREATE TABLE STUDENTS_DETAILS(
    ID INT NOT NULL,
    NAME VARCHAR(60) NOT NULL,
    AGE INT NOT NULL,
    ADDRESS VARCHAR(60) NOT NULL,
    EMAIL VARCHAR(60) NOT NULL,
    PRIMARY KEY(ID)
)"""
# table created
cursorObject.execute(studentRecord)
# disconnecting from the server
dataBase.close()
print("STUDENTS_DETAILS Table is created in the database")