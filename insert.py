import sqlite3

conn = sqlite3.connect('acer db')
print("opened database successfully")

conn.execute('''INSERT INTO EMPLOYEE(ID,NAME,AGE,ADDRESS,SALARY)\
 VALUES(1, 'Jeff', 33, 'california',45000.00)''')

conn.execute('''INSERT INTO EMPLOYEE(ID,NAME,AGE,ADDRESS,SALARY)\
VALUES(2,'Allen',25,'texas',25000.00)''')
