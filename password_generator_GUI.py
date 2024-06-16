import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
   try:
       length = int(length_entry.get())
       if length <= 0:
           raise ValueError("Length must be greater than 0")
       characters = string.ascii_letters + string.digits + string.punctuation
       password = ''.join(random.choice(characters) for i in range(length))
       password_entry.delete(0, tk.END)
       password_entry.insert(0, password)
   except ValueError as e:
       messagebox.showerror("Error", str(e))


# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")  # Set window size
root.configure(bg='gray')  # Set window background color


# Create a label and entry for password length
length_label = tk.Label(root, text="Length:", bg='gray', fg='white')  # Set label background color
length_label.pack(pady=5)  # Add vertical padding


length_entry = tk.Entry(root, width=20)  # Set width of entry widget
length_entry.pack(pady=5)  # Add vertical padding


# Create a button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg='lightgreen',fg='white')  # Set button background color
generate_button.pack(pady=5)  # Add vertical padding


# Create a label and entry to display the generated password
password_label = tk.Label(root, text="Generated Password:", bg='gray',fg='white')  # Set label background color
password_label.pack(pady=5)  # Add vertical padding


password_entry = tk.Entry(root, width=20)  # Set width of entry widget
password_entry.pack(pady=5)  # Add vertical padding


# Start the GUI event loop
root.mainloop()