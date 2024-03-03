from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
 
class grocerycategory:
    def __init__(self,root):
 
        self.root=root
        self.root.geometry("1270x700+0+0")
        self.root.title("Grocery category" )
        self.root.config(bg="lightblue")
        self.root.focus_force()
        Label(root,text="grocery store|develop by xxxx",bg="#c36464",fg='#fff',font='arial 10 bold').pack(side=BOTTOM,fill=X)
 
        #variable
        self.var_category_id=StringVar()
        self.var_name=StringVar()
 
        #category title=========
        lbl_title=Label(self.root,text="Manage category",font=("groudy old style",30),bg="blue",fg="white",bd=3,relief=RIDGE)
        lbl_title.pack(side=TOP,fill=X,padx=10,pady=10)
 
        lbl_title=Label(self.root,text="Enter category name",font=("groudy old style",30),fg="black",bg="lightblue")
        lbl_title.place(x=50,y=80)
 
        lbl_title=Entry(self.root,textvariable=self.var_name,font=("groudy old style",30),bg="light green")
        lbl_title.place(x=55,y=140,width=300,height=40)
 
        btn_add = Button(self.root, text='SAVE',command=self.add_data, font=("arial", 15, 'bold'), width=13, bg='brown',cursor='hand2')
        btn_add.place(x=350,y=140,width=100,height=40)
 
        btn_delete = Button(self.root, text='DELETE',command=self.delete_data, font=("arial", 15, 'bold'), width=13, bg='purple',cursor='hand2')
        btn_delete.place(x=450,y=140,width=100,height=40)
       
        btn_show_categories = Button(root, text="Show Categories", command=self.show_categories,bg='yellow')
        btn_show_categories.place(x=550,y=140,width=100,height=40)
 
 
 
 
 
        img_logo = Image.open('images/img7.jpg')
        img_logo = img_logo.resize((600, 400))
        self.photo_logo = ImageTk.PhotoImage(img_logo)
 
        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=10, y=200, width=600, height=450)
 
        img_logo1 = Image.open('images/img6.jpg')
        img_logo1 = img_logo1.resize((600, 350))
        self.photo_logo1 = ImageTk.PhotoImage(img_logo1)
 
        self.logo1 = Label(self.root, image=self.photo_logo1)
        self.logo1.place(x=630, y=280, width=600, height=350)
 
 
#category treeview
       
        category_frame = Frame(self.root, bd=3, relief=RIDGE, bg='orange')
        category_frame.place(x=700, y=70, width=530, height=200)
 
        scroll_x=ttk.Scrollbar(category_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(category_frame,orient=VERTICAL)
 
        self.category_table=ttk.Treeview(category_frame,column=('category_id','name'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
 
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
 
        scroll_x.config(command=self.category_table.xview)
        scroll_y.config(command=self.category_table.yview)
 
        self.category_table.heading('category_id',text='category_id')
        self.category_table.heading('name',text='NAME')
 
        self.category_table['show']='headings'
        self.category_table.column("category_id",width=30)
        self.category_table.column("name",width=30)
       
 
       
       
 
        self.category_table.pack(fill=BOTH,expand=1)
        #self.category_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
 
    def add_data(self):
        if self.var_name.get() == "":
            messagebox.showerror("Error", "Name is required!")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="sagarme",
                    database="grocery_store"
                )
                my_cursor = conn.cursor()
             
                my_cursor.execute("INSERT INTO category (name) VALUES (%s)", (self.var_name.get(),))
 
                conn.commit()
                self.fetch_data()  
                conn.close()
                messagebox.showinfo("Success", "Category added successfully!")
            except Exception as es:
                messagebox.showerror("Error", f"Error adding category: {str(es)}")
 
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sagarme",
                database="grocery_store"
            )
            cur = conn.cursor()
            cur.execute("SELECT * FROM category")
            data = cur.fetchall()
            if len(data) != 0:
                self.category_table.delete(*self.category_table.get_children())
                for i in data:
                    self.category_table.insert("", END, values=i)
                conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error fetching data: {str(es)}")
 
 
    def delete_data(self):
        selected_item = self.category_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a category to delete.")
        else:
            confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this category?")
            if confirmation:
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="sagarme",
                        database="grocery_store"
                    )
                    my_cursor = conn.cursor()
                   
                    # Retrieve the category ID of the selected item
                    category_id = self.category_table.item(selected_item, 'values')[0]
                   
                    # Execute the delete query
                    my_cursor.execute("DELETE FROM category WHERE category_id = %s", (category_id,))
                   
                    conn.commit()
                    self.fetch_data()  
                    conn.close()
                    messagebox.showinfo("Success", "Category deleted successfully.")
                except Exception as es:
                    messagebox.showerror("Error", f"Error deleting category: {str(es)}")
 
    def show_categories(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sagarme",
                database="grocery_store"
            )
            my_cursor = conn.cursor()
 
        # Execute the SQL query to retrieve categories
            my_cursor.execute("SELECT category_id, name FROM category")
            categories = my_cursor.fetchall()
 
            # Clear existing data in the category table widget
            self.category_table.delete(*self.category_table.get_children())
 
            # Insert retrieved categories into the category table widget
            if categories:
                for category in categories:
                    self.category_table.insert("", "end", values=category)
   
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching categories: {str(e)}")
   
 
 
 
 
 
 
 
if __name__=="__main__":
    root=Tk()
    c=grocerycategory(root)
    root.mainloop()        