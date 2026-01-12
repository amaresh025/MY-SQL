import mysql.connector 
# connecting with database in sql
conn = mysql.connector.connect(host = "localhost", user = "root", password = "Amar", database = "mydb1")
# if connection is success print func executed 
print("connected")




