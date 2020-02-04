from tkinter import Tk, Label, Button
import tkinter as tk
import registration as rg

class main_GUI:
    def __init__(self, master):
        self.master = master
        master.title("Selection")
        master.geometry("600x400")
        master.resizable(0,0)
        
        Label(master, text="Select One", font =("Times",26, "bold") , width = 25).grid(row=0, column=0)

        Button(master, fg="#75131b", text = "Login" , bg ="#4067a3", font = ("Helvetica",20, "bold italic"), height = 3, width = 32, command=self.login_page).grid(padx=20, pady=20)

        Button(master, fg="#75131b", text="Register", bg = "#4067a3" , font = ("Helvetica",20, "bold italic"),  height = 3, width = 32, command=self.register_page).grid(pady=20, padx=20)

    def register_page(self):
        self.close_window()
        registration_instance = Tk()
        registration_system_object = rg.Registration_System(registration_instance)
        print("Going to register page")

    def login_page(self):
        self.close_window()
        login_instance = Tk()
        login_system_object = rg.lg.Login_System(login_instance)
        print("Going to register page")

    def close_window(self):
        self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    my_gui = main_GUI(root)
    root.mainloop()