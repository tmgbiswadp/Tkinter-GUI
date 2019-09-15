import tkinter as tk
import webbrowser as wb
from tkinter import messagebox as mb


window = tk.Tk()
window.title("My first GUI")
window.geometry("300x200")
window.resizable(0,0)

def linkedin():
    #wb.open_new_tab("www.google.com")
    # opens the tab in webbrowser
    mb.showinfo("Hello Python")
    mb.showerror("Something went wrong")
    mb.showwarning("Hello python")
    # pops up a message box

def facebook():
    wb.open_new_tab("www.facebook.com")


# Creating twoo text labels and input labels
tk.Label(window, text = "Linked In").grid(row = 0, column = 1)

# Entry is used to display the input_field
tk.Entry(window).grid(row = 0, column = 2, columnspan = 5)

tk.Label(window, text = "Facebook").grid(row = 2, column = 1)
# Entry is used to display the input_field
tk.Entry(window).grid(row = 2, column = 2)

tk.Checkbutton(window, text ="Keep me logged in").grid(column = 1, columnspan = 2)
# column span takes to take the width of 2 columnspan
# you can also use row span
button1 = tk.Button(window, text = "Linked In", bg = "orange", command = linkedin).grid(column= 1, row= 5)

button2 = tk.Button(window, text = "Facebook", bg = "pink", command = facebook).grid(column= 2, row= 5)
#button2.bind("<Button-1>", facebook)

#def say_hi():
    #tk.Label(window, text = "Hi").pack()

#tk.Button(window, text = "Click Me", command =say_hi).pack()
# Command is executed when you click the Button
# In this above case we are calling the function say_hi





window.mainloop()
