import tkinter as tk
from tkinter import messagebox
import mysql.connector

def delete_product():
    cpid = cpid_entry.get()

    # Connect to MySQL database
    conn = mysql.connector.connect(host='localhost', user='root', password='*****', database='grocery_store')
    cursor = conn.cursor()

    # Delete the record from the products table
    cursor.execute("DELETE FROM products WHERE product_ID=%s", (cpid,))
    conn.commit()

    # Close cursor and connection
    cursor.close()
    conn.close()

    # Show success message
    messagebox.showinfo("Success", f"Product with ID {cpid} has been deleted.")

root = tk.Tk()
root.title("Delete Product")

# Label and Entry for Product ID
tk.Label(root, text="Product ID:").grid(row=0, column=0)
cpid_entry = tk.Entry(root)
cpid_entry.grid(row=0, column=1)

# Delete button
delete_button = tk.Button(root, text="Delete Product", command=delete_product)
delete_button.grid(row=1, column=0, columnspan=2)

root.mainloop()
