import tkinter as tk
from tkinter import messagebox
import pymysql

class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.geometry("400x300")
        self.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        # Add a label with upper padding and styling
        tk.Label(self, text="Welcome to the Online Learning Platform", font=("Arial", 16), pady=50, bg="#f0f0f0").pack()

        # Add labels and entry fields for user ID and password with styling
        user_label = tk.Label(self, text="User ID:", font=("Arial", 12), bg="#f0f0f0")
        user_label.pack()
        self.user_entry = tk.Entry(self, font=("Arial", 12))
        self.user_entry.pack(pady=5)

        password_label = tk.Label(self, text="Password:", font=("Arial", 12), bg="#f0f0f0")
        password_label.pack()
        self.password_entry = tk.Entry(self, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=5)

        # Add a login button with styling
        login_button = tk.Button(self, text="Login", font=("Arial", 12), command=self.login, bg="#4CAF50", fg="white", relief="raised", width=10)
        login_button.pack(pady=10)

    def login(self):
        # Get the entered user ID and password
        user_id = self.user_entry.get()
        password = self.password_entry.get()

        # Connect to the MySQL database
        db = pymysql.connect(host='localhost', user='root', passwd='', database='elearning')
        cursor = db.cursor()

        # Check if the user ID and password match the records in the database
        cursor.execute("SELECT * FROM users WHERE UserID = %s AND Password = %s", (user_id, password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Login Successful", f"Welcome, {user[1]}!")  # Assuming user[1] contains the username
            # Add code here to navigate to the main page or perform further actions after successful login
        else:
            messagebox.showerror("Login Failed", "Invalid user ID or password. Please try again.")

        # Close the database connection
        db.close()

if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()
