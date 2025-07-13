import pandas as pd
import psycopg2

# Define connection
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="ecommerce",
    user="postgres",
    password="123lopas123" 
)
cur = conn.cursor()

# Helper function to load CSV into table
def load_csv_to_table(csv_path, table_name, columns):
    df = pd.read_csv(csv_path)
    for row in df.itertuples(index=False):
        values = tuple(getattr(row, col) for col in columns)
        placeholders = ','.join(['%s'] * len(values))
        insert_query = f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({placeholders})"
        cur.execute(insert_query, values)

# Load data
load_csv_to_table(r"C:\Users\nepra\Desktop\Projektas/customers.csv", "customers", ["customer_id", "name", "email", "country"])
load_csv_to_table(r"C:\Users\nepra\Desktop\Projektas/products.csv", "products", ["product_id", "product_name", "price"])
load_csv_to_table(r"C:\Users\nepra\Desktop\Projektas/orders.csv", "orders", ["order_id", "customer_id", "order_date"])
load_csv_to_table(r"C:\Users\nepra\Desktop\Projektas/order_items.csv", "order_items", ["order_id", "product_id", "quantity", "price"])

# Commit & close
conn.commit()
cur.close()
conn.close()
print("Data loaded successfully.")
