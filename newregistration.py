from tkinter import *
from tkinter import messagebox
import pymysql

def newlogin_page():
    window.destroy()
    import newlogin

def signup():
    username_val = username.get()
    email_val = email.get()
    password_val = password.get()
    confirm_password_val = confirm_password.get()
    
    if password_val == confirm_password_val:
        try:
            db = pymysql.connect(host='localhost', user='root', passwd='', database='elearning1')
            cursor = db.cursor()
            
            query = "INSERT INTO users (Username, Email, Password) VALUES (%s, %s, %s)"
            cursor.execute(query, (username_val, email_val, password_val))
            db.commit()

            db.close()

            messagebox.showinfo('Signup', 'Successfully signed up')
        
        except pymysql.Error as e:
            messagebox.showerror('Error', f'Error: {e}')
    else:
        messagebox.showerror('Invalid', "Passwords do not match")

def on_enter(e):
    if e.widget == username:
        if username.get() == 'Username':
            username.delete(0, END)
    elif e.widget == email:
        if email.get() == 'Email':
            email.delete(0, END)
    elif e.widget == password:
        if password.get() == 'Password':
            password.delete(0, END)
    elif e.widget == confirm_password:
        if confirm_password.get() == 'Confirm Password':
            confirm_password.delete(0, END)

def on_leave(e):
    if e.widget == username:
        if username.get() == '':
            username.insert(0, 'Username')
    elif e.widget == email:
        if email.get() == '':
            email.insert(0, 'Email')
    elif e.widget == password:
        if password.get() == '':
            password.insert(0, 'Password')
    elif e.widget == confirm_password:
        if confirm_password.get() == '':
            confirm_password.insert(0, 'Confirm Password')

window = Tk()
window.title("SignUP")
window.geometry('925x500+300+200')
window.configure(bg="#fff")
window.resizable(False, False)

img = PhotoImage(file='D:/python3.12/Scripts/elearning/registration.png')
Label(window, image=img, border=0, bg='white').place(x=50, y=90)

frame = Frame(window, width=350, height=420, bg='#fff')
frame.place(x=480, y=50)

heading = Label(frame, text='Sign up', fg="#57a1f8", bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=50, y=5)

username = Entry(frame, width=25, fg='black', bd=0, bg='white', font=('Microsoft YaHei UI Light', 11))
username.place(x=30, y=50)
username.insert(0, 'Username')
username.bind("<FocusIn>", on_enter)
username.bind("<FocusOut>", on_leave)

email = Entry(frame, width=25, fg='black', bd=0, bg='white', font=('Microsoft YaHei UI Light', 11))
email.place(x=30, y=100)
email.insert(0, 'Email')
email.bind("<FocusIn>", on_enter)
email.bind("<FocusOut>", on_leave)

password = Entry(frame, width=25, fg='black', bd=0, bg='white', font=('Microsoft YaHei UI Light', 11), show='*')
password.place(x=30, y=150)
password.insert(0, 'Password')
password.bind("<FocusIn>", on_enter)
password.bind("<FocusOut>", on_leave)

confirm_password = Entry(frame, width=25, fg='black', bd=0, bg='white', font=('Microsoft YaHei UI Light', 11), show='*')
confirm_password.place(x=30, y=200)
confirm_password.insert(0, 'Confirm Password')
confirm_password.bind("<FocusIn>", on_enter)
confirm_password.bind("<FocusOut>", on_leave)

Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=newlogin_page).place(x=35, y=250)

Label(frame, text='I have an account? ', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9)).place(x=90, y=300)

Button(frame, width=6, text='Sign in', bd=0, bg='white', cursor='hand2', fg='#57a1f8', command=lambda: newlogin_page()).place(x=200, y=300)
window.mainloop()
