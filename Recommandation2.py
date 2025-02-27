import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class LearningPlatformApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Learning Platform")

        # Set background image
        self.bg_image = Image.open('D:/python3.12/Scripts/elearning/recommemdation.png')
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # Create labels
        self.label1 = tk.Label(root, text="Welcome to the Learning Platform!")
        self.label1.pack(pady=10)

        # Create buttons
        self.button1 = tk.Button(root, text="Start Learning", command=self.start_learning)
        self.button1.pack(pady=5)

        self.button2 = tk.Button(root, text="Recommendations", command=self.show_recommendations)
        self.button2.pack(pady=5)

        self.button3 = tk.Button(root, text="Back to main menu", command=root.quit)
        self.button3.pack(pady=5)

    def start_learning(self):
        messagebox.showinfo("Learning Platform", "Let's start learning!")

    def show_recommendations(self):
        # Create a new window for recommendations
        recommendation_window = tk.Toplevel(self.root)
        recommendation_window.title("Recommendations")

        # Set background image
        self.bg_image = Image.open('D:/python3.12/Scripts/elearning/registration.png')
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(recommendation_window, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # Create a label for recommendations
        recommendation_label = tk.Label(recommendation_window, text="Choose courses to add to your cart:")
        recommendation_label.pack(pady=10)

        # Create buttons for courses
        course1_button = tk.Button(recommendation_window, text="Course 1", command=lambda: self.add_to_cart("Course 1"))
        course1_button.pack(pady=5)

        course2_button = tk.Button(recommendation_window, text="Course 2", command=lambda: self.add_to_cart("Course 2"))
        course2_button.pack(pady=5)

        course3_button = tk.Button(recommendation_window, text="Course 3", command=lambda: self.add_to_cart("Course 3"))
        course3_button.pack(pady=5)

        course3_button = tk.Button(recommendation_window, text="Course 4", command=lambda: self.add_to_cart("Course 4"))
        course3_button.pack(pady=5)

        course3_button = tk.Button(recommendation_window, text="Course 5", command=lambda: self.add_to_cart("Course 5"))
        course3_button.pack(pady=5)

        # Create a button to view the cart
        cart_button = tk.Button(recommendation_window, text="View Cart", command=self.view_cart)
        cart_button.pack(pady=10)

    def add_to_cart(self, course):
        messagebox.showinfo("Added to Cart", f"{course} added to your cart!")

    def view_cart(self):
        # Display a messagebox with the cart contents
        cart_contents = "Your Cart:\n\n"
        # You can customize this with the actual contents of the cart
        messagebox.showinfo("Cart", cart_contents)

def main():
    root = tk.Tk()
    app = LearningPlatformApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
