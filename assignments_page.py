import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar
import pymysql

class AssignmentPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Assignment Page")
        self.master.geometry("400x450")

        # Fetch Course IDs and Names from database
        self.course_info = self.fetch_course_info()

        # Title Label
        title_label = tk.Label(self.master, text="Assignment Title:", font=("Helvetica", 14))
        title_label.pack(pady=10)

        # Title Entry
        self.title_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.title_entry.pack()

        # Description Label
        description_label = tk.Label(self.master, text="Assignment Description:", font=("Helvetica", 14))
        description_label.pack(pady=10)

        # Description Textbox
        self.description_text = tk.Text(self.master, width=40, height=5, font=("Helvetica", 12))
        self.description_text.pack()

        # Course Label
        course_label = tk.Label(self.master, text="Select Course:", font=("Helvetica", 14))
        course_label.pack(pady=10)

        # Course Dropdown Menu
        self.selected_course = tk.StringVar()
        self.course_dropdown = tk.OptionMenu(self.master, self.selected_course, *self.course_info.keys())
        self.course_dropdown.pack()

        # Deadline Label
        deadline_label = tk.Label(self.master, text="Assignment Deadline:", font=("Helvetica", 14))
        deadline_label.pack(pady=10)

        # Calendar Widget for Deadline
        self.cal = Calendar(self.master, selectmode='day', date_pattern='yyyy-mm-dd')
        self.cal.pack()

        # Submit Button
        submit_button = tk.Button(self.master, text="Submit", command=self.submit_assignment, font=("Helvetica", 14))
        submit_button.pack(pady=20)

    def fetch_course_info(self):
        try:
            db = pymysql.connect(host='localhost', user='root', passwd='', database='elearning1')
            cursor = db.cursor()
            cursor.execute("SELECT CourseID, Title FROM courses")
            course_info = {row[1]: row[0] for row in cursor.fetchall()}
            db.close()
            return course_info
        except pymysql.Error as e:
            messagebox.showerror('Error', f'Error: {e}')
            return {}

    def submit_assignment(self):
        title = self.title_entry.get()
        description = self.description_text.get("1.0", tk.END)
        selected_course_name = self.selected_course.get()
        deadline_str = self.cal.get_date()

        try:
            course_id = self.course_info[selected_course_name]
            self.insert_assignment(title, description, course_id, deadline_str)
            messagebox.showinfo("Assignment Submitted", "Assignment Details:\nTitle: {}\nDescription: {}\nCourse: {}\nDeadline: {}".format(title.strip(), description.strip(), selected_course_name, deadline_str))
        except ValueError:
            messagebox.showerror("Error", "An error occurred while submitting the assignment.")

    def insert_assignment(self, title, description, course_id, deadline):
        try:
            db = pymysql.connect(host='localhost', user='root', passwd='', database='elearning1')
            cursor = db.cursor()
            
            query = "INSERT INTO assignments (CourseID, Title, Description, Deadline) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (course_id, title, description, deadline))
            db.commit()

            db.close()

        except pymysql.Error as e:
            messagebox.showerror('Error', f'Error: {e}')

def main():
    root = tk.Tk()
    app = AssignmentPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
