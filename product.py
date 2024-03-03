import tkinter as tk
from tkinter import ttk
import mysql.connector
# Function to establish a MySQL connection
def get_sql_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='*******',
        database='grocery_store'
    )

# Function to retrieve products from the database
def get_all_products(connection):
    cursor = connection.cursor()
    query = "SELECT product_id, name, price, quantity, category FROM products"
    cursor.execute(query)
    products = cursor.fetchall()
    cursor.close()
    return products

# Function to display products in the Tkinter window
def display_products():
    connection = get_sql_connection()
    products = get_all_products(connection)
    connection.close()

    # Clear existing content
    product_text.delete('1.0', tk.END)

    # Display products in the Text widget
    for product in products:
        product_text.insert(tk.END, f"Product ID: {product[0]}\n")
        product_text.insert(tk.END, f"Name: {product[1]}\n")
        product_text.insert(tk.END, f"Price: {product[2]}\n")
        product_text.insert(tk.END, f"Quantity: {product[3]}\n")
        product_text.insert(tk.END, f"Category: {product[4]}\n")
        product_text.insert(tk.END, "\n")

# Create the main Tkinter window
root = tk.Tk()
root.title("Product Management System")

# Create a frame for displaying products
display_frame = ttk.LabelFrame(root, text="Products")
display_frame.grid(row=0, column=0, padx=10, pady=10)

# Create a Text widget to display products
product_text = tk.Text(display_frame, height=20, width=50)
product_text.grid(row=0, column=0, padx=5, pady=5)

# Create a button to fetch and display products
fetch_button = ttk.Button(root, text="Fetch Products", command=display_products)
fetch_button.grid(row=1, column=0, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()


