import tempfile
from tkinter import *
from tkinter import ttk, messagebox
import random
import mysql.connector
import datetime
 
class bill_app:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1270x700+0+0")
        self.root.title("Bill Management System")
 
        self.bill_no = StringVar()
        self.customername = StringVar()
        self.phone = StringVar()
        self.email = StringVar()
        self.productname = StringVar()
        self.price = IntVar()
        self.category = StringVar()
        self.quantity = IntVar()
        self.tax = StringVar()
        self.sub_total = StringVar()
        self.total = StringVar()
        self.search_bill = StringVar()
 
        Z = random.randint(1000, 9999)
        self.bill_no.set(Z)
        categories, product_names, prices = self.populate_comboboxes()
        self.l = []
 
        label_title = Label(self.root, text="Bill Management System", font=("times new roman", '35', "bold"), bg="white")
        label_title.place(x=0, y=40, width=1270, height=45)
 
        # main frame
        main_frame = Frame(self.root, bd=5, relief=RIDGE, bg="light blue")
        main_frame.place(x=5, y=90, width=1270, height=550)
 
        customer_frame = LabelFrame(main_frame, text="Customer", font=("times new roman", 12, "bold"), bg="white", fg="red")
        customer_frame.place(x=5, y=5, width=290, height=140)
 
        self.lbl_mob = Label(customer_frame, text="Mobile no:", font=("times new roman", 12, "bold"), bg="white")
        self.lbl_mob.grid(row=0, column=0, sticky=W, padx=5, pady=2)
 
        self.entry_mob = ttk.Entry(customer_frame, textvariable=self.phone, font=("times new roman", 10, "bold"), width=22)
        self.entry_mob.grid(row=0, column=1, padx=5, pady=2)
 
        self.lbl_customername = Label(customer_frame, text="Customer name:", font=("times new roman", 12, "bold"), bg="white")
        self.lbl_customername.grid(row=1, column=0, sticky=W, padx=5, pady=2)
 
        self.entry_customername = ttk.Entry(customer_frame, textvariable=self.customername, font=("times new roman", 10, "bold"), width=22)
        self.entry_customername.grid(row=1, column=1, padx=5, pady=2)
 
        self.lbl_email = Label(customer_frame, text="Email:", font=("times new roman", 12, "bold"), bg="white")
        self.lbl_email.grid(row=3, column=0, sticky=W, padx=5, pady=2)
 
        self.entry_email = ttk.Entry(customer_frame, textvariable=self.email, font=("times new roman", 10, "bold"), width=22)
        self.entry_email.grid(row=3, column=1, sticky=W, padx=5, pady=2)
 
        product_frame = LabelFrame(main_frame, text="Product", font=("times new roman", 12, "bold"), bg="white", fg="red")
        product_frame.place(x=300, y=5, width=350, height=190)
 
        self.lbl_category = Label(product_frame, text="Select category:", font=("times new roman", 12, "bold"), bg="white")
        self.lbl_category.grid(row=0, column=0, sticky=W, padx=5, pady=2)
 
        self.combobox_category = ttk.Combobox(product_frame, textvariable=self.category, font=("times new roman", 10, "bold"), width=24, state="readonly")
        self.combobox_category["values"] = [category[0] for category in categories]
        self.combobox_category.grid(row=0, column=1, padx=5, pady=2)
 
        self.lbl_productname = Label(product_frame, text="Product name:", font=("times new roman", 12, "bold"), bg="white")
        self.lbl_productname.grid(row=1, column=0, sticky=W, padx=5, pady=2)
 
        self.combobox_productname = ttk.Combobox(product_frame, textvariable=self.productname, font=("times new roman", 10, "bold"), width=24, state="readonly")
        self.combobox_productname["values"] = [product_name[0] for product_name in product_names]
        self.combobox_productname.grid(row=1, column=1, padx=5, pady=2)
 
        self.lbl_price = Label(product_frame, text="Price:", font=("times new roman", 12, "bold"), bg="white")
        self.lbl_price.grid(row=2, column=0, sticky=W, padx=5, pady=2)
 
        self.combobox_price = ttk.Combobox(product_frame, textvariable=self.price, font=("times new roman", 10, "bold"), width=24, state="readonly")
        self.combobox_price["values"] = [price[0] for price in prices]
        self.combobox_price.grid(row=2, column=1, padx=5, pady=2)
 
        self.lbl_quantity = Label(product_frame, text="Quantity:", font=("times new roman", 12, "bold"), bg="white")
        self.lbl_quantity.grid(row=3, column=0, sticky=W, padx=5, pady=2)
 
        self.entry_quantity = ttk.Entry(product_frame, textvariable=self.quantity, font=("times new roman", 10, "bold"), width=27)
        self.entry_quantity.grid(row=3, column=1, padx=5, pady=2)
 
        search_frame = Frame(main_frame, bd=2, bg="white")
        search_frame.place(x=785, y=0, width=470, height=40)
 
        self.lbl_bill_no = Label(search_frame, text="Bill no :", font=("times new roman", 12, "bold"), fg="green")
        self.lbl_bill_no.grid(row=0, column=0, sticky=W, padx=5, pady=2)
 
        self.entry_search = ttk.Entry(search_frame, textvariable=self.search_bill, font=("times new roman", 10, "bold"), width=25)
        self.entry_search.grid(row=0, column=1, padx=5, pady=2)
 
        self.search = Button(search_frame, text="Search", font=("arial", 12, 'bold'), bg="light blue", fg="black", width=11, cursor="hand2")
        self.search.grid(row=0, column=3)
 
        right_lbl_frame = LabelFrame(main_frame, text="Bill area", font=("times new roman", 12, "bold"), bg="white", fg="red")
        right_lbl_frame.place(x=780, y=50, width=470, height=420)
 
        scroll_y = Scrollbar(right_lbl_frame, orient=VERTICAL)
        self.textarea = Text(right_lbl_frame, yscrollcommand=scroll_y.set, bg="light pink", fg="blue", font=("times new roman", 12, "bold"))
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)
 
        billc_frame = LabelFrame(main_frame, text="Bill counter", font=("times new roman", 12, "bold"), bg="white", fg="red")
        billc_frame.place(x=0, y=430, width=1270, height=110)
 
        self.lbl_subtotal = Label(billc_frame, text="Subtotal:", font=("times new roman", 12, "bold"), bg="white")
        self.lbl_subtotal.grid(row=0, column=0, sticky=W, padx=5, pady=2)
 
        self.entry_subtotal = ttk.Entry(billc_frame, textvariable=self.sub_total, font=("times new roman", 10, "bold"), width=24, state="readonly")
        self.entry_subtotal.grid(row=0, column=1, padx=5, pady=2)
 
        self.lbl_tax = Label(billc_frame, text="Tax:", font=("times new roman", 12, "bold"), bg="white")
        self.lbl_tax.grid(row=1, column=0, sticky=W, padx=5, pady=2)
 
        self.entry_tax = ttk.Entry(billc_frame, textvariable=self.tax, font=("times new roman", 10, "bold"), width=24, state="readonly")
        self.entry_tax.grid(row=1, column=1, padx=5, pady=2)
 
        self.lbl_total = Label(billc_frame, text="Total:", font=("times new roman", 12, "bold"), bg="white")
        self.lbl_total.grid(row=2, column=0, sticky=W, padx=5, pady=2)
 
        self.entry_total = ttk.Entry(billc_frame, textvariable=self.total, font=("times new roman", 10, "bold"), width=24, state="readonly")
        self.entry_total.grid(row=2, column=1, padx=5, pady=2)
 
        button_frame = Frame(billc_frame, bd=2, bg="white")
        button_frame.place(x=300, y=0)
 
        self.addtocart = Button(button_frame, text="Add to cart", command=self.additem, font=("arial", 15, 'bold'), bg="light blue", fg="black", width=11, cursor="hand2")
        self.addtocart.grid(row=0, column=0)
 
        self.generate_bill = Button(button_frame, text="Generate bill", command=self.gen_bill, font=("arial", 15, 'bold'), bg="light blue", fg="black", width=11, cursor="hand2")
        self.generate_bill.grid(row=0, column=1)
 
        self.save = Button(button_frame, text="Save Bill", command=self.savebill, font=("arial", 15, 'bold'), bg="light blue", fg="black", width=11, cursor="hand2")
        self.save.grid(row=0, column=2)
 
        self.clear = Button(button_frame, text="Clear",command=self.clear, font=("arial", 15, 'bold'), bg="light blue", fg="black", width=11, cursor="hand2")
        self.clear.grid(row=0, column=3)
 
        self.print = Button(button_frame, text="Print",command=self.print_bill, font=("arial", 15, 'bold'), bg="light blue", fg="black", width=11, cursor="hand2")
        self.print.grid(row=0, column=4)
 
        self.exit = Button(button_frame, text="Exit",command=self.exit_app, font=("arial", 15, 'bold'), bg="light blue", fg="black", width=11, cursor="hand2")
        self.exit.grid(row=0, column=5)
 
        self.welcome()
 
    def populate_comboboxes(self):
        categories = []
        products_names = []
        prices = []
        try:
            # Connect to MySQL database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sagarme",
                database="grocery_store"
            )
 
            # Fetch data from the product table
            cursor = conn.cursor()
            cursor.execute("SELECT DISTINCT category FROM products")
            categories = cursor.fetchall()
 
            cursor.execute("SELECT DISTINCT name FROM products")
            product_names = cursor.fetchall()
 
            cursor.execute("SELECT DISTINCT price FROM products")
            prices = cursor.fetchall()
 
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error connecting to MySQL: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        return categories, product_names, prices
 
    def additem(self):
        Tax = 1
        if self.price.get() == "":
            messagebox.showerror("Error", "Please select a product and enter its price")
            return
 
        self.n = float(self.price.get())
        if self.quantity.get() == "":
            messagebox.showerror("Error", "Please enter the quantity")
            return
 
        self.m = int(self.quantity.get()) * self.n
        self.l.append(self.m)
 
        if self.productname.get() == "":
            messagebox.showerror("Error", "Please select a product")
            return
 
        self.textarea.insert(END, f"\n  {self.productname.get()}\t\t{self.quantity.get()}\t\t{self.m}")
        self.sub_total.set(str('Rs.%.2f' % (sum(self.l))))
        self.tax.set(str('Rs.%.2f' % ((((sum(self.l)) - (self.price.get())) * Tax) / 100)))
        self.total.set(str('Rs.%.2f' % (((sum(self.l)) + ((((sum(self.l)) - (self.price.get())) * Tax) / 100)))))
 
    def gen_bill(self):
        if self.productname.get() =="":
            messagebox.showerror("Error", "Please add a product to the cart")
        else:
            text = self.textarea.get(10.0, (10.0 + float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END, "\n ======================================================")
            self.textarea.insert(END, f"\n Subtotal:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END, f"\n Tax:\t\t\t{self.tax.get()}")
            self.textarea.insert(END, f"\n Total:\t\t\t{self.total.get()}")
            self.textarea.insert(END, "\n ======================================================")
 
    def savebill(self):
      try:
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sagarme",
            database="grocery_store"
        )
 
        cursor = conn.cursor()
        if not self.textarea.get("10.0", END).strip():
            messagebox.showerror("Error", "Please generate the bill before saving.")
            return  # Exit the function if bill content is empty
 
 
        # Retrieve bill details
        bill_number = self.bill_no.get()
        customer_name = self.customername.get()
        phone = self.phone.get()
        email = self.email.get()
        subtotal = float(self.sub_total.get().split('Rs.')[1])  # Retrieve subtotal from StringVar and remove 'Rs.' prefix
        tax = float(self.tax.get().split('Rs.')[1])  # Retrieve tax from StringVar and remove 'Rs.' prefix
        total = float(self.total.get().split('Rs.')[1])  # Retrieve total from StringVar and remove 'Rs.' prefix
        bill_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Current date and time
 
        # Construct SQL INSERT statement for bill table
        insert_bill_query = "INSERT INTO bills (bill_no, customer_name, phone, email, subtotal, tax, total, bill_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        bill_data = (bill_number, customer_name, phone, email, subtotal, tax, total, bill_date)
 
        # Execute SQL statement to insert into the bill table
        cursor.execute(insert_bill_query, bill_data)
 
        # Commit changes
        conn.commit()
 
        messagebox.showinfo("Success", "Bill saved successfully!")
 
      except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error saving bill: {e}")
 
      finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
   
 
   
 
    def welcome(self):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END, "\t Welcome to our grocery store")
        self.textarea.insert(END, f"\n Bill no: {self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer name: {self.customername.get()}")
        self.textarea.insert(END, f"\n Phone number: {self.phone.get()}")
        self.textarea.insert(END, f"\n Customer email: {self.email.get()}")
        self.textarea.insert(END, "\n================================================")
        self.textarea.insert(END, f"\n Products\t\t\tQty\t\tPrice")
        self.textarea.insert(END, "\n================================================")
    def clear(self):
        # Clear entry fields
        self.customername.set("")
        self.phone.set("")
        self.email.set("")
        self.productname.set("")
        self.price.set("")
        self.quantity.set("")
        self.category.set("")
        self.sub_total.set("")
        self.tax.set("")
        self.total.set("")
        self.search_bill.set("")
 
        # Clear text area
        self.textarea.delete(1.0, END)
        self.welcome()
 
 
 
        #print func
    def print_bill(self):
        # Create a new window to display the bill content
        bill_window = Toplevel(self.root)
        bill_window.title("Print Bill")
        bill_window.geometry("600x400")
 
        # Create a Text widget to display the bill content
        bill_text = Text(bill_window, wrap=WORD)
        bill_text.pack(expand=True, fill=BOTH)
 
        # Insert the bill content into the Text widget
        bill_text.insert(END, self.textarea.get("1.0", END))
 
       
 
 
    def exit_app(self):
        # Ask for confirmation before exiting
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()        
if __name__ == '__main__':
    root = Tk()
    b = bill_app(root)
    root.mainloop()