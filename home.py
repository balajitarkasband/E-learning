import tkinter as tk
from tkinter import ttk

class HomePage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Home Page")
        self.root.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        # Create main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # Add course card
        course_card = self.create_card(main_frame, "Courses", "Browse through our available courses and start learning.", 0, 0)

        # Add resources card
        resources_card = self.create_card(main_frame, "Resources", "Access additional resources to enhance your learning experience.", 0, 1)

    def create_card(self, parent, title, description, row, column):
        # Create card frame
        card_frame = ttk.Frame(parent)
        card_frame.grid(row=row, column=column, padx=10, pady=10)

        # Add title to card
        title_label = ttk.Label(card_frame, text=title, font=("Arial", 16))
        title_label.grid(row=0, column=0, padx=10, pady=(0, 5))

        # Add description to card
        description_label = ttk.Label(card_frame, text=description, wraplength=200, font=("Arial", 12))
        description_label.grid(row=1, column=0, padx=10, pady=(0, 10))

        return card_frame

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = HomePage()
    app.run()
