# pip install mysql-connector-python or PyMySQL

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "std"
)

cursor = con.cursor()

# cursor.execute("create table student(id int,name varchar(30));")
# cursor.execute("drop table student")

cursor.execute("insert into student(id,name) value (%s,%s)",(2,"Anusha"))
# value = (2,"Anusha")

# cursor.execute("select * from student where id=1")

# rows = cursor.fetchall()

# for row in rows:
#     print(row)

con.commit()

cursor.close()
con.close()
