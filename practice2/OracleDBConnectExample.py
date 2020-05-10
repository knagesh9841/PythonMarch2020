import cx_Oracle

con = cx_Oracle.connect('system/root@localhost')

cursor = con.cursor()

cursor.execute("select * from emp")

MyResult = cursor.fetchall()

for i in MyResult:
    print(i)


cursor.close()
con.close()





