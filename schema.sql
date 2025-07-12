-- Create customers table
CREATE TABLE public.customers (
    customer_id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    country TEXT
);

-- Create products table
CREATE TABLE public.products (
    product_id SERIAL PRIMARY KEY,
    product_name TEXT,
    price NUMERIC
);

-- Create orders table
CREATE TABLE public.orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES public.customers(customer_id),
    order_date DATE
);

-- Create order_items table
CREATE TABLE public.order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES public.orders(order_id),
    product_id INTEGER REFERENCES public.products(product_id),
    quantity INTEGER,
    price NUMERIC
);
