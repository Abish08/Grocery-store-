root = tk.Tk()
root.title("Product Management System")
 
# Create a frame for the header
header_frame = ttk.Frame(root)
header_frame.pack(fill='x')
 
header_label = ttk.Label(header_frame, text="Product Management System", font=('Helvetica', 18, 'bold'))
header_label.pack(pady=10)
 
# Create a frame for inserting products
insert_frame = ttk.LabelFrame(root, text="Insert Product")
insert_frame.pack(padx=10, pady=10, fill='both', expand=True)
 
name_label = ttk.Label(insert_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
name_entry = ttk.Entry(insert_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')
 
category_label = ttk.Label(insert_frame, text="Category:")
category_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
category_entry = ttk.Entry(insert_frame)
category_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')
 
quantity_label = ttk.Label(insert_frame, text="Quantity:")
quantity_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
quantity_entry = ttk.Entry(insert_frame)
quantity_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')
 
price_label = ttk.Label(insert_frame, text="Price:")
price_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
price_entry = ttk.Entry(insert_frame)
price_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')
 
insert_button = ttk.Button(insert_frame, text="Insert", command=insert_product)
insert_button.grid(row=4, columnspan=2, padx=5, pady=5, sticky='we')
 
# Create a frame for deleting products
delete_frame = ttk.LabelFrame(root, text="Delete Product")
delete_frame.pack(padx=10, pady=10, fill='both', expand=True)
 
product_id_label = ttk.Label(delete_frame, text="Product ID:")
product_id_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
product_id_entry = ttk.Entry(delete_frame)
product_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')
 
delete_button = ttk.Button(delete_frame, text="Delete", command=delete_product)
delete_button.grid(row=1, columnspan=2, padx=5, pady=5, sticky='we')
 
# Create a frame for displaying products
display_frame = ttk.LabelFrame(root, text="Products")
display_frame.pack(side="left", padx=10, pady=10)
 
# Create a Text widget to display products
product_text = tk.Text(display_frame, height=20, width=50)
product_text.pack(padx=5, pady=5)
 
# Create a button to fetch and display products
fetch_button = ttk.Button(root, text="Fetch Products", command=display_products)
fetch_button.pack(padx=10, pady=10, side="left")
 
root.mainloop()
 