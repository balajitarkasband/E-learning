import tkinter as tk
from tkinter import messagebox
import pymysql

class RegistrationPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registration Page")
        self.geometry("400x300")
        self.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        # Add a label with upper padding and styling
        tk.Label(self, text="Registration Page", font=("Arial", 16), pady=20, bg="#f0f0f0").pack()

        # Add labels and entry fields for user details with styling
        user_label = tk.Label(self, text="User ID:", font=("Arial", 12), bg="#f0f0f0")
        user_label.pack()
        self.user_entry = tk.Entry(self, font=("Arial", 12))
        self.user_entry.pack(pady=5)

        username_label = tk.Label(self, text="Username:", font=("Arial", 12), bg="#f0f0f0")
        username_label.pack()
        self.username_entry = tk.Entry(self, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        email_label = tk.Label(self, text="Email:", font=("Arial", 12), bg="#f0f0f0")
        email_label.pack()
        self.email_entry = tk.Entry(self, font=("Arial", 12))
        self.email_entry.pack(pady=5)

        password_label = tk.Label(self, text="Password:", font=("Arial", 12), bg="#f0f0f0")
        password_label.pack()
        self.password_entry = tk.Entry(self, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=5)

        # Add a register button with styling
        register_button = tk.Button(self, text="Register", font=("Arial", 12), command=self.register, bg="#4CAF50", fg="white", relief="raised", width=10)
        register_button.pack(pady=10)

    def register(self):
        # Get the entered user details
        user_id = self.user_entry.get()
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Connect to the MySQL database
        db = pymysql.connect(host='localhost', user='root', passwd='', database='elearning')
        cursor = db.cursor()

        # Insert the user details into the database
        try:
            cursor.execute("INSERT INTO users (UserID, Username, Email, Password) VALUES (%s, %s, %s, %s)", (user_id, username, email, password))
            db.commit()
            messagebox.showinfo("Registration Successful", "You have been successfully registered!")
        except pymysql.Error as e:
            messagebox.showerror("Registration Failed", f"Error: {e}")

        # Close the database connection
        db.close()

if __name__ == "__main__":
    app = RegistrationPage()
    app.mainloop()
