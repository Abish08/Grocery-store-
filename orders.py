import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import mysql.connector

# Define order_details globally
order_details = []

# Function to establish a MySQL connection
def get_sql_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='******',
        database='grocery_store'
    )

# Function to insert a new order into the database
def insert_order():
    global order_details  # Access the global order_details variable
    customer_name = customer_name_entry.get()
    total = float(total_entry.get())
    
    if customer_name and total:
        try:
            connection = get_sql_connection()
            cursor = connection.cursor()
            
            # Insert order into 'orders' table
            order_query = ("INSERT INTO orders (customer_name, total, datetime) "
                           "VALUES (%s, %s, %s)")
            order_data = (customer_name, total, datetime.now())
            cursor.execute(order_query, order_data)
            order_id = cursor.lastrowid
            
            # Insert order details into 'order_details' table
            order_details_query = ("INSERT INTO order_details (order_id, product_id, quantity, total_price) "
                                   "VALUES (%s, %s, %s, %s)")
            for product in order_details:
                order_details_data = (order_id, product['product_id'], product['quantity'], product['total_price'])
                cursor.execute(order_details_query, order_details_data)
            
            connection.commit()
            connection.close()
            
            messagebox.showinfo("Success", "Order inserted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Please fill all fields.")

# Function to fetch and display all orders
def fetch_orders():
    try:
        connection = get_sql_connection()
        cursor = connection.cursor()
        
        # Fetch all orders
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
        
        # Display orders in the treeview
        for item in orders_tree.get_children():
            orders_tree.delete(item)
        
        for order in orders:
            orders_tree.insert('', tk.END, values=order)
        
        connection.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to display order details for a selected order
# Function to display order details for a selected order
def display_order_details(order,self):
    selected_items = orders_tree.selection()
    if not selected_items:
        print("No order selected!")  # Debugging message
        messagebox.showerror("Error", "Please select an order.")
        return
    
    selected_item = selected_items[0]
    order_id = orders_tree.item(selected_item, 'values')[0]
    
    try:
        connection = get_sql_connection()
        cursor = connection.cursor()
        
        # Fetch order details for the selected order
        cursor.execute("SELECT * FROM order_details WHERE order_id = %s", (order_id,))
        order_details = cursor.fetchall()
        
        # Display order details in the treeview
        for item in order_details_tree.get_children():
            order_details_tree.delete(item)
        
        for detail in order_details:
            order_details_tree.insert('', tk.END, values=detail)
        
        connection.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create the main window
root = tk.Tk()
root.title("Order Management System")

# Create a frame for inserting orders
insert_frame = ttk.LabelFrame(root, text="Insert Order")
insert_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

customer_name_label = ttk.Label(insert_frame, text="Customer Name:")
customer_name_label.grid(row=0, column=0, padx=5, pady=5)
customer_name_entry = ttk.Entry(insert_frame)
customer_name_entry.grid(row=0, column=1, padx=5, pady=5)

total_label = ttk.Label(insert_frame, text="Total:")
total_label.grid(row=1, column=0, padx=5, pady=5)
total_entry = ttk.Entry(insert_frame)
total_entry.grid(row=1, column=1, padx=5, pady=5)

insert_button = ttk.Button(insert_frame, text="Insert Order", command=insert_order)
insert_button.grid(row=2, columnspan=2, padx=5, pady=5, sticky="we")

# Create a frame for displaying orders
orders_frame = ttk.LabelFrame(root, text="Orders")
orders_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

orders_tree = ttk.Treeview(orders_frame, columns=("Order ID", "Customer Name", "Total", "Datetime"), show="headings")
orders_tree.heading("Order ID", text="Order ID")
orders_tree.heading("Customer Name", text="Customer Name")
orders_tree.heading("Total", text="Total")
orders_tree.heading("Datetime", text="Datetime")
orders_tree.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

fetch_button = ttk.Button(orders_frame, text="Fetch Orders", command=fetch_orders)
fetch_button.grid(row=1, column=0, padx=5, pady=5, sticky="we")

# Create a frame for displaying order details
order_details_frame = ttk.LabelFrame(root, text="Order Details")
order_details_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

order_details_tree = ttk.Treeview(order_details_frame, columns=("Order ID", "Product ID", "Quantity", "Total Price"), show="headings")
order_details_tree.heading("Order ID", text="Order ID")
order_details_tree.heading("Product ID", text="Product ID")
order_details_tree.heading("Quantity", text="Quantity")
order_details_tree.heading("Total Price", text="Total Price")
order_details_tree.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

display_button = ttk.Button(order_details_frame, text="Display Order Details", command=display_order_details)
display_button.grid(row=1, column=0, padx=5, pady=5, sticky="we")

# Set column and row weights for resizing
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
orders_frame.columnconfigure(0, weight=1)
orders_frame.rowconfigure(0, weight=1)
order_details_frame.columnconfigure(0, weight=1)
order_details_frame.rowconfigure(0, weight=1)

root.mainloop()
