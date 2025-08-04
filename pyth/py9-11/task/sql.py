
import mysql.connector


con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "std"
)

cursor = con.cursor()

def insert_data(user):

    cursor.execute("insert into user(name,password,email,balance) value (%s,%s,%s,%s)",
                   (user.get_username(),
                   user.get_password(),
                   user.get_email(),
                   user.get_balance()
                   ))
    
    con.commit()
