import tkinter as tk
from tkinter import ttk


def login():
    self.root.destroy()
    import newlogin
    
def signup():
    self.root.destroy()
    import newregistration

class LearningPlatformHomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Learning Platform")
        self.root.geometry("800x600")

        # Header
        self.header_frame = tk.Frame(root, bg="blue", height=100)
        self.header_frame.pack(fill="x")

        self.header_label = tk.Label(self.header_frame, text="Welcome to Our Learning Platform", fg="white", bg="blue", font=("Arial", 20))
        self.header_label.pack(pady=30)

        # Navigation Bar
        self.nav_frame = tk.Frame(root, bg="black", height=50)
        self.nav_frame.pack(fill="x")

        self.signup_button = tk.Button(self.nav_frame, text="Signup",command=signup)
        self.signup_button.pack(side="right", padx=10)

        self.login_button = tk.Button(self.nav_frame, text="Login", command=login)
        self.login_button.pack(side="right", padx=10)

        # About Us Section
        self.about_us_frame = tk.Frame(root, bg="white")
        self.about_us_frame.pack(pady=20)

        self.about_us_label = tk.Label(self.about_us_frame, text="About Us", font=("Arial", 16))
        self.about_us_label.pack(pady=10)

        self.about_us_text = tk.Text(self.about_us_frame, height=5, width=70)
        self.about_us_text.insert(tk.END, "Our learning platform aims to provide high-quality courses to learners around the globe.")
        self.about_us_text.config(state="disabled")
        self.about_us_text.pack(pady=10)

        # Contact Us Section
        self.contact_us_frame = tk.Frame(root, bg="white")
        self.contact_us_frame.pack(pady=20)

        self.contact_us_label = tk.Label(self.contact_us_frame, text="Contact Us", font=("Arial", 16))
        self.contact_us_label.pack(pady=10)

        self.contact_us_text = tk.Text(self.contact_us_frame, height=5, width=70)
        self.contact_us_text.insert(tk.END, "Email: contact@learningplatform.com\nPhone: +1234567890\nAddress: 123 Main Street, City, Country")
        self.contact_us_text.config(state="disabled")
        self.contact_us_text.pack(pady=10)

        # Courses Section
        self.courses_frame = tk.Frame(root, bg="white")
        self.courses_frame.pack(pady=20)

        self.courses_label = tk.Label(self.courses_frame, text="Courses", font=("Arial", 16))
        self.courses_label.pack(pady=10)

        self.course1_button = tk.Button(self.courses_frame, text="Course 1: Introduction to Programming")
        self.course1_button.pack(pady=5)
        self.course2_button = tk.Button(self.courses_frame, text="Course 2: Data Science Fundamentals")
        self.course2_button.pack(pady=5)
        self.course3_button = tk.Button(self.courses_frame, text="Course 3: Web Development Basics")
        self.course3_button.pack(pady=5)

        # Cart Section
        self.cart_frame = tk.Frame(root, bg="white")
        self.cart_frame.pack(pady=20)

        self.cart_label = tk.Label(self.cart_frame, text="Cart", font=("Arial", 16))
        self.cart_label.pack(pady=10)

        self.cart_contents_label = tk.Label(self.cart_frame, text="No items in cart")
        self.cart_contents_label.pack()

    def open_login_page(self):
        # This function would open your login page
        print("Opening login page...")

if __name__ == "__main__":
    root = tk.Tk()
    app = LearningPlatformHomePage(root)
    root.mainloop()
