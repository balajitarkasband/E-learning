from tkinter import *
from tkinter import messagebox
import pymysql

def newregistration_page():
    app.destroy()
    import newregistration

def recommendation_page():
    app.destroy()
    import recommandation

    
class LoginPage(Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.geometry('925x500+300+200')  
        self.configure(bg="#fff")
        self.resizable(False, False)
        
        img = PhotoImage(file='D:/python3.12/Scripts/elearning/login.png')
        image_label = Label(self, image=img, bg='white')
        image_label.image = img  
        image_label.place(x=50, y=50)

        self.frame = Frame(self, width=350, height=350, bg="white")
        self.frame.place(x=480, y=70)

        heading = Label(self.frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=100, y=5)

        def on_enter(e):
            self.user.delete(0, 'end')

        def on_leave(e):
            name = self.user.get()
            if name == '':
                self.user.insert(0, 'Username')

        self.user = Entry(self.frame, width=25, fg='black', bd=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Username')
        self.user.bind('<FocusIn>', on_enter)
        self.user.bind('<FocusOut>', on_leave)

        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=107)

        def on_enter_password(e):
            self.password_entry.delete(0, 'end')

        def on_leave_password(e):
            name = self.password_entry.get()
            if name == '':
                self.password_entry.insert(0, 'Password')

        self.password_entry = Entry(self.frame, width=25, fg='black', bd=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.password_entry.place(x=30, y=150)
        self.password_entry.insert(0, 'Password')
        self.password_entry.bind('<FocusIn>', on_enter_password)
        self.password_entry.bind('<FocusOut>', on_leave_password)

        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=177)

        Button(self.frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', bd=0, border=0, command=self.signin).place(x=35, y=204)

        label = Label(self.frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
        label.place(x=75, y=270)
        
        sign_up = Button(self.frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=newregistration_page)
        sign_up.place(x=215, y=270)

    def signin(self):
        username = self.user.get()
        password = self.password_entry.get()

        try:
            db = pymysql.connect(host='localhost', user='root', passwd='', database='elearning1')
            cursor = db.cursor()

            cursor.execute("SELECT * FROM users WHERE Username = %s AND Password = %s", (username, password))
            user_data = cursor.fetchone()

            if user_data:
                 messagebox.showinfo('Signin', 'Successfully signed in')
            else:
                messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

            db.close()

        except pymysql.Error as e:
            print("Error:", e)
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()
