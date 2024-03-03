import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def delete_product():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        product_id = item['values'][0]
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sagarme",
                database="grocery_store"
            )
            cursor = connection.cursor()
            query = "DELETE FROM products WHERE product_id = %s"
            cursor.execute(query, (product_id,))
            connection.commit()
            tree.delete(selected_item)
            connection.close()
            print(f"Deleted product with ID {product_id}")
        except mysql.connector.Error as error:
            print("Error:", error)
            messagebox.showerror("Error", f"Failed to delete product: {error}")
    else:
        print("Please select a product to delete.")
        messagebox.showerror("Error", "Please select a product to delete.")

def add_product():
    name = name_entry.get()
    category = category_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()
    
    if name and category and quantity and price:
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sagarme",
                database="grocery_store"
            )
            cursor = connection.cursor()
            query = "INSERT INTO products (name, category, quantity, price) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (name, category, quantity, price))
            connection.commit()
            connection.close()
            messagebox.showinfo("Success", "Product added successfully!")
            refresh_treeview()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to add product: {error}")
    else:
        messagebox.showerror("Error", "Please fill all fields.")
def update_product():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        product_id = item['values'][0]
        name = name_entry.get()
        category = category_entry.get()
        quantity = quantity_entry.get()
        price = price_entry.get()
        if name and category and quantity and price:
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="sagarme",
                    database="grocery_store"
                )
                cursor = connection.cursor()
                query = "UPDATE products SET name = %s, category = %s, quantity = %s, price = %s WHERE product_id = %s"
                cursor.execute(query, (name, category, quantity, price, product_id))
                connection.commit()
                connection.close()
                messagebox.showinfo("Success", "Product updated successfully!")
                refresh_treeview()
            except mysql.connector.Error as error:
                messagebox.showerror("Error", f"Failed to update product: {error}")
        else:
            messagebox.showerror("Error", "Please fill all fields.")
    else:
        messagebox.showerror("Error", "Please select a product to update.")


def refresh_treeview():
    tree.delete(*tree.get_children())
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sagarme",
            database="grocery_store"
        )
        cursor = connection.cursor()
        query = "SELECT * FROM products"
        cursor.execute(query)
        for product in cursor.fetchall():
            tree.insert('', 'end', values=product)
        connection.close()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to fetch products: {error}")

# Tkinter setup
root = tk.Tk()
root.title("Product Management")

# Create treeview
tree = ttk.Treeview(root, columns=("ID", "Name", "Category", "Quantity", "Price"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Category", text="Category")
tree.heading("Quantity", text="Quantity")
tree.heading("Price", text="Price")
tree.pack(padx=10, pady=10)

# Add scrollbars
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar.set)

# Create a frame for product details
details_frame = tk.Frame(root)
details_frame.pack(padx=10, pady=10)

tk.Label(details_frame, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
name_entry = tk.Entry(details_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(details_frame, text="Category:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
category_entry = tk.Entry(details_frame)
category_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(details_frame, text="Quantity:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
quantity_entry = tk.Entry(details_frame)
quantity_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(details_frame, text="Price:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
price_entry = tk.Entry(details_frame)
price_entry.grid(row=3, column=1, padx=5, pady=5)

# Add buttons for add, update, and delete
add_button = tk.Button(root, text="Add Product", command=add_product)
add_button.pack(side="left", padx=5, pady=5)

update_button = tk.Button(root, text="Update Product", command=update_product)
update_button.pack(side="left", padx=5, pady=5)

delete_button = tk.Button(root, text="Delete Product", command=delete_product)
delete_button.pack(side="left", padx=5, pady=5)

# Display products initially
refresh_treeview()

root.mainloop()
