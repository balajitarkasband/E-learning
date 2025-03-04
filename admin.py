from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox
from datetime import date, datetime  
import pymysql
import PIL.Image
from PIL import ImageTk
import os

background = "#06283D"
framefg = "white"

root = Tk()
root.title("Elearning System")
root.geometry("1250x700+210+10")
root.config(bg=background)

# Connect to MySQL database
db = pymysql.connect(host='localhost', user='root', passwd='', db='elearning1')
cursor = db.cursor()

# Create the farmer_data table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Courses (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        gender VARCHAR(10),
        dob DATE,
        Category VARCHAR(10),
        date DATE,
        religion VARCHAR(50),
        Ages VARCHAR(255)
    )
''')
db.commit()

# Close the cursor and database connection
cursor.close()
db.close()

# Exit
def Exit():
    root.destroy()

 
# Save
def Save():
    global gender
    name = Name.get()
    dob_str = DOB.get()
    religion = Religion.get()
    Ages = Age.get()
    farmer_Category = Category.get()
    
    if name == "" or farmer_Category == "Select Category" or dob_str == "" or religion == "" or Ages == "":
        messagebox.showerror("Error", "Incomplete data! Please fill in all the fields.")
        return

    try:
        # Convert the date string to a datetime object
        dob = datetime.strptime(dob_str, "%d/%m/%Y").date()
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please enter the date in the format DD/MM/YYYY.")
        return

    # Connect to MySQL database
    db = pymysql.connect(host='localhost', user='root', passwd='', db='elearning1')
    cursor = db.cursor()

    try:
        cursor.execute('''
            INSERT INTO farmer (name, gender, dob, Category, date, religion, Ages)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', (name, gender, dob, farmer_Category, date.today(), religion, Ages))
        
        # Get the last inserted ID (registration number)
        registration_number = cursor.lastrowid

        # Save the image with a filename based on the registration number
        image_filename = f"C:\\python312\\Scripts\\Images\\Profile_Img_{registration_number}.png"
        img.save(image_filename)

        db.commit()

        messagebox.showinfo("Success", "Data entered successfully")
        Clear()
    except Exception as e:
        messagebox.showerror("Error", f"Error saving data to database: {e}")

        
    # Close the cursor and database connection
    cursor.close()
    db.close()

        
# Search
def search():
    text = Search.get()
    Clear()

    # Connect to MySQL database
    db = pymysql.connect(host='localhost', user='root', passwd='', db='elearning1')
    cursor = db.cursor()

    cursor.execute('SELECT * FROM farmer WHERE id=%s', (text,))
    data = cursor.fetchone()

    # Close the cursor and database connection
    cursor.close()
    db.close()

    if data:
        Registration.set(data[0])
        Name.set(data[1])
        gender = 1 if data[2] == 'Male' else 2
        DOB.set(data[3])
        Category.set(data[4])
        Religion.set(data[6])
        Age.set(data[7])

        if gender == 1:
            R1.select()
        else:
            R2.select()

        # Load and display image
        try:
            img_path = f"C:\\python312\\Scripts\\Images\\Profile_Img_{text}.png"  
            print("Image path:", img_path)  # Debugging statement
            img = PIL.Image.open(img_path)
            resized_image = img.resize((199, 190))  # Resize the image
            photo = ImageTk.PhotoImage(resized_image)
            lbl.config(image=photo)
            lbl.image = photo
            print("Image loaded and resized successfully")  # Debugging statement
        except Exception as e:
            print("Error loading image:", e)
    else:
        messagebox.showerror("Invalid", "Invalid registration number!!!")




# Clear
def Clear():
    Name.set('')
    DOB.set('')
    Religion.set('')
    Age.set('')
    Category.set('Select Category')
    
    registration_no()
    
    saveButton.config(state='normal')
    
    img1 = PhotoImage(file='C:\\python312\\Scripts\\Images\\Profile_Img.png')
    lbl.config(image=img1)
    lbl.image = img1
    
    img = ""

# Registration number
# Registration number
def registration_no():
    # Connect to MySQL database
    db = pymysql.connect(host='localhost', user='root', passwd='', db='elearning1')
    cursor = db.cursor()

    cursor.execute('SELECT MAX(id) FROM farmer')
    max_row_value = cursor.fetchone()[0]

    try:
        Registration.set(max_row_value + 1)
    except:
        Registration.set("1")

    # Close the cursor and database connection
    cursor.close()
    db.close()


# Gender
def selection():
    global gender
    value = radio.get()
    gender = "Male" if value == 1 else "Female"

# Show image
def showImage():
    global filename
    global img
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file",
                                          filetype=(("JPG File", ".jpg"), ("PNG File", ".png"), ("All files", "*.txt")))
    img = (PIL.Image.open(filename))
    resized_image = img.resize((199, 190))
    photo2 = ImageTk.PhotoImage(resized_image)
    lbl.config(image=photo2)
    lbl.image = photo2

# Top frames
Label(root, text="Email: elearning1system @gmail.com", width=10, height=3, bg="#f0687c", anchor='e').pack(side=TOP, fill=X)
Label(root, text="Elearning System", width=15, height=2, bg="orange", fg='black', font='arial 20 bold').pack(side=TOP, fill=X)

"""# Search box to update
Search = StringVar()
Entry(root, textvariable=Search, width=15, bd=2, font="arial 20").place(x=820, y=70)

try:
    original_image_search = PIL.Image.open('C:\\python312\\Scripts\\Images\\Search Icon.png')
    resized_image_search = original_image_search.resize((40, 40), PIL.Image.BICUBIC)
    imageicon_search = ImageTk.PhotoImage(resized_image_search)
except Exception as e:
    print("Error loading search icon image:", e)
    imageicon_search = None

if imageicon_search:
    srch = Button(root, text="Search", compound=LEFT, image=imageicon_search, width=100, height=30, bg='#7b68ee',
                  font="arial 13 bold", command=search)
    srch.place(x=1060, y=66)
else:
    srch = Button(root, text="Search", width=20, bg='#7b68ee', font="arial 13 bold", command=search)
    srch.place(x=1060, y=66)"""

# Registration and Date
Label(root, text="Registration No:", font="arial 13", fg='white', bg=background).place(x=30, y=150)
Label(root, text="Date:", font="arial 13", fg='white', bg=background).place(x=500, y=150)

Registration = IntVar()
Date = StringVar()

reg_entry = Entry(root, textvariable=Registration, width=15, font="arial 10")
reg_entry.place(x=160, y=150)

registration_no()

# registration_no()
today = date.today()
d1 = today.strftime("%d/%m/%Y")
date_entry = Entry(root, textvariable=Date, width=15, font="arial 10")
date_entry.place(x=550, y=150)

Date.set(d1)

# Clear
def Clear():
    Name.set('')
    DOB.set('')
    Religion.set('')
    Age.set('')
    Category.set('Select Category')
    
    registration_no()
    
    saveButton.config(state='normal')
    
    img1 = PhotoImage(file='C:\\python312\\Scripts\\Images\\Profile_Img.png')
    lbl.config(image=img1)
    lbl.image = img1
    
    img = ""

# FARMER Details
obj = LabelFrame(root, text="Farmer Details", font=20, bd=2, width=900, bg=background, fg=framefg, height=230,relief=GROOVE)
obj.place(x=30, y=200)

Label(obj, text="Full Name:", font="aerial 13", bg=background, fg=framefg).place(x=30, y=30)
Label(obj, text="Date of Birth:", font="aerial 13", bg=background, fg=framefg).place(x=30, y=70)
Label(obj, text="Gender:", font="aerial 13", bg=background, fg=framefg).place(x=30, y=110)

Label(obj, text="Courses:", font="aerial 13", bg=background, fg=framefg).place(x=500, y=30)
Label(obj, text="Collage:", font="aerial 13", bg=background, fg=framefg).place(x=500, y=70)
Label(obj, text="Age:", font="aerial 13", bg=background, fg=framefg).place(x=500, y=110)

Name = StringVar()
name_entry = Entry(obj, textvariable=Name, width=40, font="arial 10")
name_entry.place(x=160, y=30)

DOB = StringVar()
name_entry = Entry(obj, textvariable=DOB, width=40, font="arial 10")
name_entry.place(x=160, y=70)

radio = IntVar()
R1 = Radiobutton(obj, text='Male', variable=radio, value=1, bg=background, fg=framefg, command=selection)
R1.place(x=150, y=110)

R2 = Radiobutton(obj, text='Female', variable=radio, value=2, bg=background, fg=framefg, command=selection)
R2.place(x=250, y=110)

Courses = Combobox(obj, values=['IT', 'Management'], font="Roboto 10", width=20,
                 state="r")
Courses.place(x=590, y=30)
Courses.set("Select Category")

Religion = StringVar()
religion_entry = Entry(obj, textvariable=Religion, width=30, font="arial 10")
religion_entry.place(x=590, y=70)

Age = StringVar()
Age_entry = Entry(obj, textvariable=Age, width=30, font="arial 10")
Age_entry.place(x=590, y=110)

# Image
f = Frame(root, bd=3, bg="black", width=200, height=200, relief=GROOVE)
f.place(x=1000, y=210)

try:
    original_image_profile = PIL.Image.open('C:\\python312\\Scripts\\Images\\Profile_Img.png')
    resized_image_profile = original_image_profile.resize((200, 200), PIL.Image.BICUBIC)
    img_profile = ImageTk.PhotoImage(resized_image_profile)
except Exception as e:
    print("Error loading profile image:", e)
    img_profile = None

if img_profile:
    lbl = Label(f, bg="black", image=img_profile)
    lbl.place(x=0, y=0)
else:
    print("Profile image not loaded.")

# Buttons
Button(root, text="Upload", width=19, height=2, font="aerial 12 bold", bg="lightblue", command=showImage).place(
    x=1000, y=450)
saveButton = Button(root, text="Save", width=19, height=2, font="aerial 12 bold", bg="lightgreen", command=Save)
saveButton.place(x=200, y=500)
Button(root, text="Reset", width=19, height=2, font="aerial 12 bold", bg="lightpink", command=Clear).place(x=425, y=500)
Button(root, text="Exit", width=19, height=2, font="Arial 12 bold", bg="Black", fg="white", command=Exit).place(x=650, y=500)

root.mainloop()