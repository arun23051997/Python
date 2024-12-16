


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import psycopg2
from psycopg2 import OperationalError, DatabaseError, Error
import os


csv_files = [
    ('customers.csv', 'customers'),
    ('geolocation.csv', 'location'),
    ('sales.csv', 'sales'),
    ('orders.csv', 'orders'),
    ('products.csv', 'products'),
    ('order_items.csv','orderitem'),
    ('payments.csv', 'payments')  
]

def connect_database():
    try:
        
        connection = psycopg2.connect(
            host="localhost",
            database="ecommerence",
            user="postgres",
            password="Arun@4032",
            port="5432",
        )
        print("Successfully connected to the database.")
        return connection
    except OperationalError as e:
        print(f"Error connecting to the database: {e}")
        

        
# connection = connect_database()

# if connection:
    
#     cursor = connection.cursor()



folder_path = "C:\\Users\\ARUNKUMAR\\OneDrive\\Desktop\\check"

def data_insert_to_database():
    
    
    
    def get_sql_type(dtype):
        if pd.api.types.is_integer_dtype(dtype):
            return 'INT'
        elif pd.api.types.is_float_dtype(dtype):
            return 'FLOAT'
        elif pd.api.types.is_bool_dtype(dtype):
            return 'BOOLEAN'
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            return 'DATETIME'
        else:
            return 'TEXT'


    for csv_file, table_name in csv_files:
    
        file_path_itrate = os.path.join(folder_path, csv_file)
    
  
        df_file_data = pd.read_csv(file_path_itrate)
    
   
        df_file_data  = df_file_data.where(pd.notnull(df_file_data ), None)
    
    
        print(f"Processing {csv_file}")
        print(f"NaN values before replacement:\n{df_file_data.isnull().sum()}\n")

    
        df_file_data.columns = [col.replace(' ', '_').replace('-', '_').replace('.', '_') for col in df_file_data.columns]

    
        columns = ', '.join([f' {col} {get_sql_type(df_file_data[col].dtype)}' for col in df_file_data.columns])
    
        create_table_query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns});'
        cursor.execute(create_table_query)
        print("create sucessfull")
    
        for _, row in df_file_data.iterrows():
       
            values = tuple(None if pd.isna(x) else x for x in row)
       
    
            sql = f"INSERT INTO {table_name} ({', '.join(['' + col + '' for col in df_file_data.columns])}) VALUES ({', '.join(['%s'] * len(row))})"
        
            cursor.execute(sql, values)
        print("one time completed")
          
        
# data_insert_to_database()
# connection.commit()

# connection.close()

# -----------------------------------------------------------------------------
# 1) List all unique cities where customers are located.
        # ==>query = "select distinct customer_city from customers"


# =============================================================================
# query = input("enter your query : ")
# connection = connect_database()
# 
# if connection:
#     
#     cursor = connection.cursor()
#     
# cursor.execute(query)
# 
# data = cursor.fetchall()
# 
# df = pd.DataFrame(data)
# print(df.head())
# =============================================================================

# ----------------------------------------------------------------------------------------------

# 2)Count the number of orders placed in 2017.
        # ==> query = "SELECT COUNT(order_id) FROM orders WHERE EXTRACT(YEAR FROM TO_TIMESTAMP(order_purchase_timestamp, 'DD-MM-YYYY HH24:MI')) = 2017;"
# =============================================================================

# =============================================================================
# query = """ select count(order_id) from orders where year(order_purchase_timestamp) = 2017 """
# 
# connection = connect_database()
# 
# if connection:
#     
#     cursor = connection.cursor()
# cursor.execute(query)
# 
# data = cursor.fetchall()
# print("total orders placed in 2017 are", data[0][0]) 
# =============================================================================

  
# -----------------------------------------------------------
# 3) Calculate the percentage of orders that were paid in installments
        # ==> query = "select ((sum(case when payment_installments >= 1 then 1
            # else 0 end))/count(*))*100 from payments"
    
# =============================================================================
# query = """ select ((sum(case when payment_installments >= 1 then 1
#               else 0 end))/count(*))*100 from payments """    
#     
# connection = connect_database()
# 
# if connection:
#     
#     cursor = connection.cursor()
#     
# cursor.execute(query)   
# data = cursor.fetchall()
# 
# print("the percentage of orders paid in installments is", data[0][0])   
# =============================================================================
    
    
# 4) Count the number of customers from each state.

# =============================================================================
# query = """ select customer_state ,count(customer_id)
# from customers group by customer_state
# """ 
# connection = connect_database()
# 
# if connection:
#     
#     cursor = connection.cursor()   
# cursor.execute(query)
# 
# data = cursor.fetchall()
# df = pd.DataFrame(data, columns = ["state", "customer_count" ])
# df = df.sort_values(by = "customer_count", ascending= False)
# 
# plt.figure(figsize = (8,4))
# plt.bar(df["state"], df["customer_count"])
# plt.xticks(rotation = 70)
# plt.xlabel("states")
# plt.ylabel("customer_count")
# plt.title("Count of Customers by States")
# plt.show()    
# =============================================================================
    
#  5) Calculate the number of orders per month in 2018. 
 
# =============================================================================
# query = """
# SELECT 
#     EXTRACT(MONTH FROM TO_TIMESTAMP(order_purchase_timestamp, 'DD-MM-YYYY HH24:MI:SS')) AS month,
#     COUNT(order_id) AS order_count
# FROM orders
# WHERE EXTRACT(YEAR FROM TO_TIMESTAMP(order_purchase_timestamp, 'DD-MM-YYYY HH24:MI:SS')) = 2017
# GROUP BY month
# ORDER BY month;
# """

# connection = connect_database()

# if connection:
    
#     cursor = connection.cursor() 
# cursor.execute(query)
# data = cursor.fetchall()


# cursor.close()
# connection.close()


# months = [int(row[0]) for row in data]  
# order_counts = [int(row[1]) for row in data]  


# plt.figure(figsize=(10, 6))
# plt.plot(months, order_counts, marker='o', color='b', label='Orders per Month')
# plt.title("Orders per Month (2017)")
# plt.xlabel("Month")
# plt.ylabel("Order Count")
# plt.xticks(range(1, 13))  # note :we can use month instead of number
# plt.grid(True)
# plt.legend()
# plt.show()
# =============================================================================
    












































