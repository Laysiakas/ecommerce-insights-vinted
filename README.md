# ecommerce-insights-vinted
🛍️ E-commerce Sales Analytics Dashboard
This project simulates a real-world e-commerce analytics workflow, covering data generation, database setup, business KPIs, and dashboard reporting — all built from scratch using SQL, Python, and Power BI.

📊 Project Overview
Simulated an e-commerce database (customers, products, orders, order items)

Used Python to generate and load data into PostgreSQL

Wrote advanced SQL queries for business insights

Built a Power BI dashboard to visualize key metrics

🛠 Tech Stack
PostgreSQL (relational database)

Python (pandas, psycopg2 for ETL)

Power BI Desktop (dashboard)

SQL (PostgreSQL flavor)

🧪 Dataset Structure
customers.csv

products.csv

orders.csv

order_items.csv

Data was generated using Faker (Python) and loaded via psycopg2 into PostgreSQL.

🔍 KPIs & Insights
📦 Total Revenue & Total Sales

📈 Revenue by Month

🧍 Top 5 Customers by Spend

🛒 Top-Selling Products

🌍 Orders by Country

📅 Order Trends over Time

📷 Visuals

Below are sample screenshots from the Power BI dashboard:

### 1. Orders and Customer Spend by Country
![Orders by Country](https://github.com/Laysiakas/ecommerce-insights-vinted/blob/main/sc1.png)

### 2. Product Performance and Revenue Trends
![Revenue Trends](https://github.com/Laysiakas/ecommerce-insights-vinted/blob/main/sc2.png)

### 3. Geographic Customer Spend Distribution
![Geographic Distribution](https://github.com/Laysiakas/ecommerce-insights-vinted/blob/main/sc3.png)




📁 Project Structure
ecommerce-dashboard/
load_data_to_postgres.py
schema.sql
customers.csv / orders.csv / ...
dashboard.pbix
README.md

🚀 How to Run
Install PostgreSQL & Power BI Desktop

Load schema.sql into a new database

Run the Python script to insert data

Open Power BI and connect to PostgreSQL

Explore or customize visuals

📬 Contact
Built by Edgaras — feel free to connect on [[LinkedIn](https://www.linkedin.com/in/edgaras-steponaitis-146452180/)]
