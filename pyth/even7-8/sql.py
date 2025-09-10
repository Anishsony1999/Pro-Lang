
import mysql.connector

connect = mysql.connector.connect(
    host="localhost", # 127.0.0.1 , IP Address
    port=3306,
    user="root",
    password="root",
    
)

cursor  = connect.cursor()


cursor.execute("SELECT * FROM py.playground_student")

for row in cursor:
    print(row[1])


