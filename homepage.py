import tkinter as tk
from tkinter import ttk

#functions


    

class LearningPlatformHomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Learning Platform")
        self.root.geometry("800x600")

        # Header
        self.header_frame = tk.Frame(root, bg="blue", height=100)
        self.header_frame.pack(fill="x")

        self.header_label = tk.Label(self.header_frame, text="Welcome to Online Learning Platform", fg="white", bg="blue", font=("Arial", 20))
        self.header_label.pack(pady=30)

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
        self.contact_us_text.insert(tk.END, "Email: contact@onlinelearningplatform.com\nPhone: +1234567890\nAddress: 123 , Pune, India")
        self.contact_us_text.config(state="disabled")
        self.contact_us_text.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = LearningPlatformHomePage(root)
    root.mainloop()
