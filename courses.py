import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

     # Background Color
background = "#f2f2f2"
framefg = "black"

class InstructorPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Instructor Page")
        self.master.geometry("600x500")


        # ID Label
        id_label = tk.Label(self.master, text="ID:", font=("Helvetica", 14), bg="#f2f2f2", fg="#333333")
        id_label.pack(pady=10)

        # ID Entry
        self.id_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.id_entry.pack()

        # Name Label
        name_label = tk.Label(self.master, text="Name:", font=("Helvetica", 14), bg="#f2f2f2", fg="#333333")
        name_label.pack(pady=10)

        # Name Entry 
        self.name_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.name_entry.pack()

        # Bio Label
        bio_label = tk.Label(self.master, text="Bio:", font=("Helvetica", 14), bg="#f2f2f2", fg="#333333")
        bio_label.pack(pady=10)

        # Bio Textbox
        self.bio_text = tk.Text(self.master, width=40, height=5, font=("Helvetica", 12))
        self.bio_text.pack()

        # Profile Picture Label
        profile_picture_label = tk.Label(self.master, text="Profile Picture:", font=("Helvetica", 14), bg="#f2f2f2", fg="#333333")
        profile_picture_label.pack(pady=10)

        # Profile Picture Button
        self.profile_picture_button = tk.Button(self.master, text="Choose Profile Picture", command=self.choose_profile_picture, font=("Helvetica", 12))
        self.profile_picture_button.pack()

        # Submit Button
        submit_button = tk.Button(self.master, text="Submit", command=self.submit_instructor, font=("Helvetica", 14), bg="lightpink2", fg="white")
        submit_button.pack(pady=20)

        # Profile Picture Image
        self.profile_picture = None

    def choose_profile_picture(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((100, 100), Image.ANTIALIAS)
            self.profile_picture = ImageTk.PhotoImage(image)
            self.profile_picture_button.config(text="Change Profile Picture")

    def submit_instructor(self):
        instructor_id = self.id_entry.get()
        name = self.name_entry.get()
        bio = self.bio_text.get("1.0", tk.END)

        # You can process the instructor details here
        messagebox.showinfo("Instructor Submitted", "Instructor Details:\nID: {}\nName: {}\nBio: {}\nProfile Picture: {}".format(instructor_id.strip(), name.strip(), bio.strip(), "Uploaded" if self.profile_picture else "Not Uploaded"))

def main():
    root = tk.Tk()
    app = InstructorPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
