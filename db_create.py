import mysql.connector 
# connecting with database in sql
conn = mysql.connector.connect(host = "localhost", user = "root", password = "Amar")

cur = conn.cursor()
#creating database
cur.execute("CREATE DATABASE mydb1")




