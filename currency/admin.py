from tkinter import Tk, Button, Frame
import tkinter as tk
import csv
import pymysql
from mainScreen import main_GUI

class adminGui(main_GUI):
    def __init__(self, root):
        self.root = root
        root.title("***Admin Page***")
        root.geometry("550x350")
        root.resizable(0,0)

        Button(root, fg = "#75131b", text="Register a user", bg = "#4067a3" , font = ("arial", 12, "bold italic"),  height = 3, width = 50, command = self.hello).grid(padx=20, pady=20)

        Button(root, fg = "#75131b", text="Get registered user", bg = "#4067a3" , font = ("arial", 12, "bold italic"),  height = 3, width = 50, command = self.get_registered_user).grid(padx=20, pady=20)

        Button(root, fg = "#75131b", text = "Get excel file", bg = "#4067a3" , font = ("arial", 12, "bold italic"),  height = 3, width = 50, command = self.write_into_excel).grid(padx=20, pady=20)

    def hello(self):
        print("semethng")

    def get_registered_user(self):
        # Open database connection
        db = pymysql.connect("localhost","root","","converter")
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # execute SQL query using execute() method.
        cursor.execute("SELECT * from registration")

        # Fetch all row using fetchall() method.
        data = cursor.fetchall() # Here data contains a list of tuple 
        print(data)

    def get_data_from_db(self):
        # Open database connection
        db = pymysql.connect("localhost","root","","converter")
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # execute SQL query using execute() method.
        cursor.execute("SELECT * from registration")

        # Fetch all row using fetchall() method.
        data = cursor.fetchall() # Here data contains a list of tuple 
        return list(data)

    def write_into_excel(self):
        with open('file.csv','w') as csv_file:
            csv_out = csv.writer(csv_file, lineterminator='\n')
            # csv_out.writerow(['Username','Password','Confirm Password'])
            for row in self.get_data_from_db():
                csv_out.writerow(row)

if __name__ == "__main__":
    root = Tk()
    admin_gui_object = adminGui(root)
    root.mainloop()
