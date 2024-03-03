import tkinter as tk
from tkinter import messagebox

def register():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    email = email_entry.get()
    address = address_entry.get("1.0", tk.END).strip()  # Get text from Text widget
    
    # Check if passwords match
    if password != confirm_password:
        messagebox.showerror("Registration Failed", "Passwords do not match")
    else:
        # Here you can implement your registration logic
        # For simplicity, just display the registered username, email, and address
        messagebox.showinfo("Registration Successful", f"Registered username: {username}\nEmail: {email}\nAddress: {address}")

# Create main window
root = tk.Tk()
root.title("Registration Page")

# Top label
registration_label = tk.Label(root, text="REGISTER HERE", font=("Akronim", 36))
registration_label.pack(pady=10)

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Confirm Password label and entry
confirm_password_label = tk.Label(root, text="Confirm Password:")
confirm_password_label.pack()
confirm_password_entry = tk.Entry(root, show="*")
confirm_password_entry.pack()

# Email label and entry
email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

# Address label and entry
address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Text(root, height=4, width=30)
address_entry.pack()

# Register button
register_button = tk.Button(root, text="Register", command=register)
register_button.pack(pady=10)

root.mainloop()
