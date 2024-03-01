import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="SOFTWARE"
)

mycursor=mydb.cursor()
sql="INSERT INTO STUDENTS_DETAILS(ID,NAME,AGE,ADDRESS,EMAIL) VALUES(%s,%s,%s,%s,%s)"
val=[("3180","Kevin","23","Nakuru","kevin80@gmail.com"),
     ("3181","Mael","20","Nyeri","mael81@gmail.com"),
     ("3182","Brenda","21","Kisumu","brenda82@gmail.com"),
     ("3183","Oluoch","24","Bungoma","oluoch83@gmail.com"),
     ("3184","Emmanuel","20","Austria","emmanuel84@gmail.com"),
     ("3185","Hart","22","Nairobi","hart85@gmail.com")]

mycursor.executemany(sql,val)
mydb.commit()

print(mycursor.rowcount, " details inserted")
mydb.close()
