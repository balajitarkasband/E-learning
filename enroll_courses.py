import tkinter as tk
from tkinter import messagebox
import pymysql

class CoursesPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Courses")
        self.attributes('-fullscreen', True)  # Set fullscreen mode
        self.configure(bg="#fff")

        # Database connection parameters
        self.db_host = 'localhost'
        self.db_user = 'root'
        self.db_passwd = ''  
        self.db_name = 'elearning1'  

        # Add heading
        self.heading_label = tk.Label(self, text="Courses", font=("Helvetica", 20, "bold"), bg="#fff")
        self.heading_label.pack(pady=(20, 10))

        # Load courses from the database
        self.load_courses()

        # Add exit button at the top right
        self.exit_button = tk.Button(self, text="Exit", command=self.exit_application, bg="#57a1f8", fg="white")
        self.exit_button.pack(side=tk.TOP, anchor=tk.NE, padx=20, pady=20)

        # Add footer
        self.footer_label = tk.Label(self, text="Online Learning Platform", font=("Helvetica", 14), bg="#333", fg="white")
        self.footer_label.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    def load_courses(self):
        try:
            db = pymysql.connect(host=self.db_host, user=self.db_user, passwd=self.db_passwd, database=self.db_name)
            cursor = db.cursor()

            # Execute the SQL query to fetch courses
            cursor.execute("SELECT CourseID, Title, Description, Instructor, Category, Price FROM courses")
            courses = cursor.fetchall()

            db.close()

            # Display course cards
            self.display_course_cards(courses)

        except pymysql.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    def enroll_course(self, course_id):
        # Simulate enrollment process (can be replaced with actual enrollment logic)
        messagebox.showinfo("Enrollment", f"Enrolled in Course {course_id}")

    def display_course_cards(self, courses):
        it_courses = []
        other_courses = []

        for course in courses:
            if "IT" in course[4]:
                it_courses.append(course)
            else:
                other_courses.append(course)

        # Display IT courses
        self.display_course_section("IT Courses", it_courses)

        # Display other courses after IT courses
        self.display_course_section("Other Courses", other_courses)

    def display_course_section(self, section_title, courses):
        # Add section title
        section_label = tk.Label(self, text=section_title, font=("Helvetica", 16, "bold"), bg="#fff")
        section_label.pack(pady=(20, 10))

        # Create frame for course cards
        course_frame = tk.Frame(self, bg="#fff")
        course_frame.pack()

        # Display course cards
        for course in courses:
            self.display_course_card(course_frame, course)

    def display_course_card(self, frame, course):
        course_id, title, description, instructor, category, price = course

        # Create card frame
        card_frame = tk.Frame(frame, bg="white", bd=1, relief=tk.SOLID)
        card_frame.pack(side=tk.LEFT, padx=20, pady=10)

        # Course Title
        title_label = tk.Label(card_frame, text=title, font=("Helvetica", 16, "bold"), bg="white")
        title_label.pack(anchor=tk.CENTER, padx=10, pady=(10, 0))

        # Course Description
        description_label = tk.Label(card_frame, text=description, font=("Helvetica", 12), bg="white", wraplength=300, justify=tk.LEFT)
        description_label.pack(anchor=tk.CENTER, padx=10, pady=(5, 0))

        # Course Instructor
        instructor_label = tk.Label(card_frame, text=f"Instructor: {instructor}", font=("Helvetica", 10), bg="white")
        instructor_label.pack(anchor=tk.CENTER, padx=10, pady=(5, 0))

        # Course Category
        category_label = tk.Label(card_frame, text=f"Category: {category}", font=("Helvetica", 10), bg="white")
        category_label.pack(anchor=tk.CENTER, padx=10, pady=(5, 0))

        # Course Price
        price_label = tk.Label(card_frame, text=f"Price: {price}", font=("Helvetica", 10), bg="white")
        price_label.pack(anchor=tk.CENTER, padx=10, pady=(5, 10))

        # Enroll Button
        enroll_button = tk.Button(card_frame, text="Enroll", command=lambda cid=course_id: self.enroll_course(cid), bg="#57a1f8", fg="white")
        enroll_button.pack(anchor=tk.CENTER, padx=10, pady=(0, 10))

    def exit_application(self):
        self.destroy()

if __name__ == "__main__":
    app = CoursesPage()
    app.mainloop()
