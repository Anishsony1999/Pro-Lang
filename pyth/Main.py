import mysql.connector

try:
    connection = mysql.connector.connect(
        host = "localhost", # host Name
        user = "root",      # user Name
        password = "root",  # password
        database = "py"     # DB Name
    )

    mycursor = connection.cursor() # create a cursor object

    mycursor.execute("insert into py.student_products (name,category,price,description,date,slug,remarks) value ('gopika','py',2000,'nothing','2023-02-02','slugurl_gopika','remark');")

    connection.commit()
    # mycursor.execute("select * from student_products")

    # for i in list(mycursor):
    #    print(i)

except Exception as e:
    print(e)

# let Start the Project  -> Django -> pip install django
