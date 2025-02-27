import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class ReviewPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Review Page")
        self.master.geometry("600x400")

       

        review_label = tk.Label(self.master, text="Write your review:", font=("Helvetica", 18), bg="white")
        review_label.pack(pady=10)

        self.review_text = tk.Text(self.master, width=40, height=5, font=("Helvetica", 12))
        self.review_text.pack()

        ratings_label = tk.Label(self.master, text="Rate from 1 to 5:", font=("Helvetica", 14), bg="white")
        ratings_label.pack(pady=10)

        self.ratings_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.ratings_entry.pack()

        submit_button = tk.Button(self.master, text="Submit", command=self.submit_review, font=("Helvetica", 14), bg="lightblue")
        submit_button.pack(pady=20)

    def submit_review(self):
        review = self.review_text.get("1.0", tk.END)
        ratings = self.ratings_entry.get()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        messagebox.showinfo("Review Submitted", "Thank you for your review:\nReview: {}\nRatings: {}\nTimestamp: {}".format(review.strip(), ratings.strip(), timestamp))

def main():
    root = tk.Tk()
    app = ReviewPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
