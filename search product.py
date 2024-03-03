import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def search_products():
    product_id = (product_id_entry.get())
    
    name = name_entry.get()
    category = category_entry.get()
    price_str = price_entry.get()
    quantity_str = quantity_entry.get()
    
    # Check if price and quantity are not empty strings
    if price_str and quantity_str:
        try:
            price = float(price_str)
            quantity = int(quantity_str)
            
            # Connect to the database
            db = mysql.connector.connect(host="localhost", user="root", passwd="*****", database="grocery_store")
            cursor = db.cursor()

            # Execute the query to search for the product
            cursor.execute(f"SELECT * FROM PRODUCTS WHERE product_ID={product_id}  AND name='{name}' AND category='{category}' AND price={price} AND quantity={quantity}")

            result = cursor.fetchall()
            
            # Clear the treeview before inserting new data
            for row in products_treeview.get_children():
                products_treeview.delete(row)

            # Insert the search results into the treeview
            for row in result:
                products_treeview.insert("", "end", values=row)
            
            db.close()
        except ValueError:
            # Handle invalid price or quantity
            messagebox.showerror("Error", "Invalid price or quantity. Please enter valid numbers.")
    else:
        # Handle empty price or quantity
        messagebox.showerror("Error", "Please enter both price and quantity.")

# Create the main window
root = tk.Tk()
root.title("Search Product")

# Create labels and entry fields
tk.Label(root, text="Product ID:").grid(row=0, column=0, padx=5, pady=5)
product_id_entry = tk.Entry(root)
product_id_entry.grid(row=0, column=1, padx=5, pady=5)





tk.Label(root, text=" Name:").grid(row=2, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Category:").grid(row=1, column=0, padx=5, pady=5)
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1, padx=5, pady=5)






tk.Label(root, text="Price:").grid(row=3, column=0, padx=5, pady=5)
price_entry = tk.Entry(root)
price_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Quantity:").grid(row=4, column=0, padx=5, pady=5)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=4, column=1, padx=5, pady=5)

# Create a search button
search_button = tk.Button(root, text="Search", command=search_products)
search_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Create a treeview to display search results
products_treeview = ttk.Treeview(root, columns=("product_ID", "Name","category", "Price", "Quantity"))
products_treeview.heading("#0", text="product_ID")
products_treeview.heading("#1", text="Name")
products_treeview.heading("#2", text="Category")
products_treeview.heading("#3", text="Price")
products_treeview.heading("#4", text="Quantity")
products_treeview.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()


