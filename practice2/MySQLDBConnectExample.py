import mysql.connector

MyDb = mysql.connector.connect(host="localhost", user="root", passwd="root")

MyCursor = MyDb.cursor()

MyCursor.execute("SHOW DATABASES")

print("Database List")

for i in MyCursor:
    print(i)


MyDb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="nagesh")

MyCursor = MyDb.cursor()

MyCursor.execute("SHOW TABLES")

print("Tables List")

for i in MyCursor:
    print(i)

MyDb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="nagesh") # Connect to Database

MyCursor = MyDb.cursor()

sql = "INSERT INTO emp VALUES (%s, %s)"
val = (11, "Shivai")
MyCursor.execute(sql, val)      # Execute the command

MyDb.commit()       # Commit changes to Database

MyCursor.execute("select * from emp")

MyRecord = MyCursor.fetchall()      # fetchall() method, which fetches all rows from the last executed statement.

for i in MyRecord:
    for j in i:
        print(j)

# The fetchone() method will return the first row of the result

MyDb.close()  # Close the connection
MyCursor.close()
