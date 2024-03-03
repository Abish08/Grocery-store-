import tkinter as tk
from tkinter import messagebox
 
def authenticate():
    username = username_entry.get()
    password = password_entry.get()
 
    # For demonstration, hardcoding username and password
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
 
# Create main window
root = tk.Tk()
root.title("Login Page")
 
# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
 
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)
 
# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
 
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)
 
# Login button
login_button = tk.Button(root, text="Login", command=authenticate)
login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
 
root.mainloop()