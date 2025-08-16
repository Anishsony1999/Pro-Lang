
import mysql.connector
import pandas as pd


bd_config ={
    'host' : 'localhost', # IP
    'user' : 'root',
    'password': 'root',
    'database':'py'
}

table = 'products'

file_path = "C:/Users/HP/OneDrive/Desktop/Lang/pyth/satur/users.csv"
conn = None
out = 'out.csv'

try :

    df = pd.read_csv(file_path)

    conn = mysql.connector.connect(**bd_config)

    cursor  = conn.cursor()
    df['total'] = df['Amount']* df['Quantity']

    for j,i in df.iterrows():
        cursor.execute("insert into products (name,gender,product,amount,quntity,total) value(%s,%s,%s,%s,%s,%s)",(i['Name'],i['Gender'],i['Product'],int(i['Amount']),int(i['Quantity']),int(i['total'])))

    conn.commit()

    data = df.groupby('Product')['total'].sum().reset_index()

    data1 = data.sort_values(by='total',ascending=False)

    print(data1)
    
    # query = f"select * from {table}"

    df = pd.read_sql(query,conn)
    
    df.to_csv(out,index=False)

except mysql.connector.Error as e:
    print(e)

except Exception as e :
    print(e)

finally:

    if conn and conn.is_connected():
        conn.close()