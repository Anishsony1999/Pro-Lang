import mysql.connector


try:
    connection = mysql.connector.connect(
        host = "localhost", # host Name
        user = "root",      # user Name
        password = "root",  # password
        database = "py"     # DB Name
    )

    mycursor = connection.cursor() # create a cursor object

    mycursor.execute("select * from student_products")

    for i in list(mycursor):
       print(i)


except Exception as e:
    print(e)

