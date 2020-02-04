from tkinter import Tk, Label, Button, messagebox, Frame
import tkinter as tk
import pymysql
# import admin as ad
import Currency as cv
import registration as rg

class Login_System:
    def __init__(self,root):
        self.root=root
        root.title("***Login***")
        root.geometry("460x260")
    
        username = tk.StringVar()
        password = tk.StringVar()

        TitleFrame=Frame(self.root, bd=10, width=450, height=50, padx=10,pady=10, bg="Gray",relief=tk.RIDGE)
        TitleFrame.grid(row=0,column=0)

        self.lblTitle=Label(TitleFrame,text="***Login System***",padx=10,pady=4,bd=1,font=('arial',20,'bold'),bg="red",width=20)
        self.lblTitle.pack()

        MainFrame= Frame(self.root, bd=10, width=450, height=200, padx=11,pady=10, bg="Gray",relief=tk.RIDGE)
        MainFrame.grid(row=1,column=0)

        self.lblUser=Label(MainFrame,font=('arial',12,'bold'),text='User Name',padx=2,pady=10,bd=2,width=19)
        self.lblUser.grid(row=1,column=0)

        self.EntName=tk.Entry(MainFrame,font=('arial',14,'bold'),textvariable=username, bd=2,width=19,justify='center')
        self.EntName.grid(row=1,column=1,pady=10)

        self.lblPassword=Label(MainFrame,font=('arial',12,'bold'),text='Password',padx=2,pady=10,bd=2,width=19)
        self.lblPassword.grid(row=2,column=0)

        self.EntPassword=tk.Entry(MainFrame,font=('arial',14,'bold'),textvariable=password, bd=2,width=19,justify='center', show ="*")
        self.EntPassword.grid(row=2,column=1,pady=10)

        self.loginbutton = Button(MainFrame, fg="#75131b", text="Login", bg = "#4067a3" , font = ("arial", 12, "bold italic"),  height = 2, width = 19, command= lambda:self.login_verification(self.EntName.get(),self.EntPassword.get()))
        self.loginbutton.grid(row = 3, column = 1)

        
    def database_connection(self, username, password):
            # Open database connection
            db = pymysql.connect("localhost","root","","converter")
            # prepare a cursor object using cursor() method
            cursor = db.cursor()

            # execute SQL query using execute() method.
            cursor.execute("SELECT * from registration")

            # Fetch all row using fetchall() method.
            data = cursor.fetchall() # Here data contains a list of tuple 
            for rows in data:
                try:
                    # print(username)
                    if username == rows[0]:
                        if password == rows[1] and password == rows[2]:
                            messagebox.showinfo("Congrats","Welcome :-"+ username)
                            return True
                except:
                    return False
            else:   
                return False
            
            # disconnect from server
            db.close()

    def login_verification(self, username , password):
        if (username == "" or password == ""):
            messagebox.showerror("Error","All fields are required!!")
        elif (username == "admin" and password == "admin"):
            messagebox.showinfo("Welcome", "Welcome my lord")
            self.go_to_admin_page()
        # elif self.database_connection(username, password) == True:
          #  print("Welcome", username.get())
            # elif (username.get()=="biswadp" and password.get()=="tamang"):
                # messagebox.showinfo("Successfull",f"Welcome {username.get()}")
                # cv.Converter(root)
                # database_connection()
        elif self.database_connection(username, password) == True:
            self.close_window()
            cv.run()
            
        else:
            messagebox.showwarning("Error","Username or password not found")
            
            #  messagebox.showerror("Error","Invalid Username or Password")

    def go_to_admin_page(self):
        self.close_window()
        tk_instance = Tk()
        admin_page_object = rg.admin.adminGui(tk_instance)
        print("Going to login page")

    def close_window(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    login_gui = Login_System(root)
    root.mainloop()