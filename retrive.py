import sqlite3

conn = sqlite3.connect('acer db')
print("opened database successfully")

cursor = conn.execute("SELECT id,name,age,address,salary from EMPLOYEE")
for row in cursor:
    print("ID = " ,row[0])
    print("ID = " ,row[0])
    print("ID = " ,row[0])
    print("ID = " ,row[0])