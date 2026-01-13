import mysql.connector 

conn = mysql.connector.connect(host = "localhost", user = "root", password = "your_password_here")

cur = conn.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS mydb1")
cur.execute("USE mydb1")

cur.execute("""CREATE TABLE IF NOT EXISTS emplo(name VARCHAR(30),
            salary INT,
            id INT PRIMARY KEY)""")
cur.execute("""INSERT IGNORE INTO emplo 
            (name, salary, id) 
            VALUES 
            ("amar", 25000, 1),
            ("am", 45000, 2)""")

conn.commit()
cur.execute("SELECT * FROM emplo")
row = cur.fetchall()
print(row)

cur.close()


