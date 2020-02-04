from tkinter import Tk, Label, Button, messagebox, Frame
import tkinter as tk
import pymysql
import login as lg
import admin

class Registration_System:
    def __init__(self,root):
        self.root=root
        root.title("***Registration***")
        root.geometry("458x300")
    
        username = tk.StringVar()
        password = tk.StringVar()
        confirmpassword = tk.StringVar()

        TitleFrame=Frame(self.root, bd=10, width=450, height=50, padx=10,pady=10, bg="Gray",relief=tk.RIDGE)
        TitleFrame.grid(row=0,column=0)

        self.lblTitle=Label(TitleFrame,text="***Registration System***",padx=10,pady=4,bd=1,font=('arial',20,'bold'),bg="red",width=20)
        self.lblTitle.pack()

        MainFrame= Frame(self.root, bd=10, width=450, height=200, padx=11,pady=10, bg="Gray",relief=tk.RIDGE)
        MainFrame.grid(row=1,column=0)

        self.lblUser=Label(MainFrame,font=('arial',12,'bold'),text='User Name',padx=2,pady=10,bd=2,width=19)
        self.lblUser.grid(row=1,column=0)

        self.EntName=tk.Entry(MainFrame,font=('arial',14,'bold'),textvariable=username, bd=2,width=19,justify='center')
        self.EntName.grid(row=1,column=1,pady=10)

        self.lblPassword=Label(MainFrame,font=('arial',12,'bold'),text='Password',padx=2,pady=10,bd=2,width=19)
        self.lblPassword.grid(row=2,column=0)

        self.EntPassword=tk.Entry(MainFrame,font=('arial',14,'bold'),textvariable=password, bd=2,width=19,justify='center')
        self.EntPassword.grid(row=2,column=1,pady=10)
        self.EntPassword.config(show="*")

        self.lblPassword=Label(MainFrame,font=('arial',12,'bold'),text='Confirm Password',padx=2,pady=10,bd=2,width=19)
        self.lblPassword.grid(row=3,column=0)

        self.confirmEntPassword=tk.Entry(MainFrame,font=('arial',14,'bold'),textvariable=confirmpassword, bd=2,width=19,justify='center')
        self.confirmEntPassword.grid(row=3,column=1,pady=10)
        self.confirmEntPassword.config(show="*")


        self.registerbutton = Button(MainFrame, fg="#75131b", text="Register", bg = "#4067a3" , font = ("arial", 12, "bold italic"),  height = 2, width = 19, command= lambda:self.database_connection(self.EntName.get(),self.EntPassword.get(),self.confirmEntPassword.get()))
        self.registerbutton.grid(row = 4, column = 1)

    def database_connection(self, username, password, confirmpassword):
            # Open database connection
            connection = pymysql.connect("localhost","root","","converter")
            # prepare a cursor object using cursor() method
            # cursor = connection.cursor()
            # print(username)

            # sql = "INSERT INTO `registration` (`username`, `pwd`, `confirmpwd`) VALUES (%s,%s,%s)"
            # val = (username,password,confirmpassword)
            # execute SQL query using execute() method.
            '''
            try:
                # cursor.execute(sql, val)
                cursor.execute("SELECT * from login")
                print("Registered successfully")
            db.commit()
            except Exception as error:
                print(error)
            finally:
                db.commit()
            
            # disconnect from server
            db.commit()
            db.close()
            '''

            try:
                with connection.cursor() as cursor:
                    #check for existing user
                    sql = "SELECT `username`,`pwd` FROM `registration` where `username` = %s"
                    cursor.execute(sql, username)
                    data = cursor.fetchone()
                    if data != None:
                        print("Username already exits")
                    else:
                        try:
                            # Create a new record
                            query = "INSERT INTO `registration` (`username`, `pwd`, `confirmpwd`) VALUES (%s,%s,%s)"
                            val = (username,password,confirmpassword)
                            cursor.execute(query, val)
                            connection.commit()
                            messagebox.showinfo("Congrats","User registered successfully")
                            self.go_to_login_page()

                        except Exception as error:
                            print(error)
                                             
                # connection is not autocommit by default. So you must commit to save
                # your changes.
            finally:
                connection.close()

    def register_verification(self, username , password, confirmpassword):
        if (username.get() == "" or password.get() == ""):
            messagebox.showerror("Error","All fields are required!!")
        elif self.database_connection(username, password, confirmpassword) == True:
            print("Welcome", username.get())
            # elif (username.get()=="biswadp" and password.get()=="tamang"):
                # messagebox.showinfo("Successfull",f"Welcome {username.get()}")
                # cv.Converter(root)
                # database_connection()
        else:
            messagebox.showerror("Error","Invalid Username or Password")

    def go_to_login_page(self):
        self.close_window()
        tk_instance = Tk()
        login_system_object = lg.Login_System(tk_instance)
        print("Going to login page")

    def close_window(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    registration_gui = Registration_System(root)
    root.mainloop()