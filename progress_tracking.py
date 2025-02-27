import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pymysql

class ProgressTrackingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Progress Tracking")
        self.root.geometry("400x400")

        self.label = tk.Label(root, text="Progress Tracking", font=("Arial", 16))
        self.label.pack(pady=10)

        self.user_id_label = tk.Label(root, text="User ID:")
        self.user_id_label.pack()
        self.user_id_entry = tk.Entry(root)
        self.user_id_entry.pack()

        self.course_id_label = tk.Label(root, text="Course ID:")
        self.course_id_label.pack()
        self.course_id_var = tk.StringVar()
        self.course_id_dropdown = tk.OptionMenu(root, self.course_id_var, *self.fetch_course_ids(), command=self.update_course_info)
        self.course_id_dropdown.config(width=25)
        self.course_id_dropdown.pack()

        self.category_label = tk.Label(root, text="Category:")
        self.category_label.pack()
        self.category_var = tk.StringVar()
        self.category_var.set("Select Category")
        self.category_dropdown = tk.OptionMenu(root, self.category_var, *self.fetch_categories(), command=self.update_module_id)
        self.category_dropdown.config(width=25)
        self.category_dropdown.pack()

        self.course_name_label = tk.Label(root, text="Course Name:")
        self.course_name_label.pack()
        self.course_name_var = tk.StringVar()
        self.course_name_entry = tk.Entry(root, textvariable=self.course_name_var, state="readonly")
        self.course_name_entry.pack()

        self.instructor_label = tk.Label(root, text="Instructor:")
        self.instructor_label.pack()
        self.instructor_var = tk.StringVar()
        self.instructor_entry = tk.Entry(root, textvariable=self.instructor_var, state="readonly")
        self.instructor_entry.pack()

        self.completion_status_label = tk.Label(root, text="Completion Status:")
        self.completion_status_label.pack()
        self.completion_status_var = tk.StringVar()
        self.completion_status_var.set("Incomplete")
        self.completion_status_dropdown = tk.OptionMenu(root, self.completion_status_var, "Incomplete", "Complete")
        self.completion_status_dropdown.config(width=25)
        self.completion_status_dropdown.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_progress, bg="#008000", fg="white")
        self.submit_button.pack(pady=10)

        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def fetch_course_ids(self):
        try:
            db = pymysql.connect(host='localhost', user='root', passwd='', database='elearning1')
            cursor = db.cursor()
            cursor.execute("SELECT CourseID FROM courses")
            course_ids = [row[0] for row in cursor.fetchall()]
            db.close()
            return course_ids
        except pymysql.Error as e:
            messagebox.showerror('Error', f'Error: {e}')
            return []

    def fetch_categories(self):
        try:
            db = pymysql.connect(host='localhost', user='root', passwd='', database='elearning1')
            cursor = db.cursor()
            cursor.execute("SELECT DISTINCT Category FROM courses")
            categories = [row[0] for row in cursor.fetchall()]
            db.close()
            return categories
        except pymysql.Error as e:
            messagebox.showerror('Error', f'Error: {e}')
            return []

    def update_course_info(self, selected_course_id):
        try:
            db = pymysql.connect(host='localhost', user='root', passwd='', database='elearning1')
            cursor = db.cursor()
            cursor.execute("SELECT Title, Instructor FROM courses WHERE CourseID=%s", (selected_course_id,))
            course_info = cursor.fetchone()
            self.course_name_var.set(course_info[0])
            self.instructor_var.set(course_info[1])
            db.close()
        except pymysql.Error as e:
            messagebox.showerror('Error', f'Error: {e}')

    def update_module_id(self, selected_category):
        try:
            db = pymysql.connect(host='localhost', user='root', passwd='', database='elearning1')
            cursor = db.cursor()
            cursor.execute("SELECT ModuleID FROM courses WHERE Category=%s", (selected_category,))
            module_id = cursor.fetchone()[0]
            db.close()
            self.course_id_var.set(module_id)
        except pymysql.Error as e:
            messagebox.showerror('Error', f'Error: {e}')

    def submit_progress(self):
        user_id = self.user_id_entry.get()
        course_id = self.course_id_var.get()
        completion_status = self.completion_status_var.get()

        try:
            db = pymysql.connect(host='localhost', user='root', passwd='', database='elearning1')
            cursor = db.cursor()
            
            query = "INSERT INTO progresstracking (UserID, CourseID, CompletionStatus, Timestamp) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (user_id, course_id, completion_status, self.timestamp))
            db.commit()

            db.close()

            messagebox.showinfo('Success', 'Progress tracked successfully')
        
        except pymysql.Error as e:
            messagebox.showerror('Error', f'Error: {e}')

if __name__ == "__main__":
    root = tk.Tk()
    app = ProgressTrackingApp(root)
    root.mainloop()
