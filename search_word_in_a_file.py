# This project is for a text file with multiple lines

import tkinter as tk
from tkinter.filedialog import askopenfilename
import os
from tkinter import messagebox

root = tk.Tk()
root.title("I wil find u")
root.geometry('400x100')

file_name = ""
success = False

def openfile():
    global file_name
    # global keyword is used to reference to the variable outisde this method
    # only after using global the variable value can be changed from inside this function and is changed every where.
    file_path = askopenfilename(initialdir=os.getcwd(),
                                # os.getcwd() gives us the present working directory
                                filetypes=(("Text Files", "*.txt*"), ("Python Files", "*.py*")),
                                # only allows the file dialog to select file with .py and .txt extension
                                title='Choose a file.')
    # sets a title for the file dialog window
    file_name = (os.path.basename(file_path))
    filenameentry.delete(0, 'end')
    # delete the values inside the entry
    filenameentry.insert(0, file_path)
    # returns the base name i.e file name of the path selected
    # os.path.dirname returns the head whereas os.path.basename returns the tail of the path selected


def findit(searchword, name):
    if searchword == "":
        messagebox.showerror("Error", "Please enter a search word first")
    elif name == "":
        messagebox.showerror("Error", "Please select a file first")
    else:
        mylines = []  # creating a list
        filehandle = open(name, 'r')
        print(type(filehandle))
        for lines in filehandle:
            mylines.append(lines.split())
            # split statement without any parameter splits the lines on the basis of whitespace
            # here every line in the text file is splitted on the basis of whitespace
            # the splitted lines are again being appended(added) to a list and the list can be seen below
        '''
        [['Keep', 'your', 'paragraph', 'centered', 'on', 'one', 'idea.'],
         ['There', 'is', 'nothing', 'more', 'frustrating', 'for', 'readers', 'when', 'they', 'read', 'a', 'paragraph',
          'that', 'talks', 'about', 'one', 'thing,', 'only', 'to', 'find', 'that', 'it', 'runs', 'off', 'track', 'and',
          'discusses', 'something', 'else.'],
         ['For', 'instance,', 'if', 'you', 'are', 'discussing', 'your', 'protagonist,', 'keep', 'the', 'paragraph',
          'on', 'that', 'character', 'and', 'nothing', 'else.', 'If', 'you', 'were', 'to', 'continue', 'talking',
          'about', 'the', 'car', 'waiting', 'outside,', 'and', 'then', 'cats,', 'dogs', 'and', 'pineapples', 'in',
          'the', 'same', 'paragraph,', 'the', 'reader', 'will', 'get', 'confused.'], ['Keep', 'it', 'simple.'],
         ['One', 'paragraph,', 'one', 'central', 'idea.']]
        '''
        for line in mylines:
            for i in range(len(line)):
                global success
                if line[i] == searchword:
                    success = True
                    messagebox.showinfo("Found in this line", line)
        if not success:
            messagebox.showinfo("Not Found", "Probably not in the file")
        filehandle.close()


tk.Label(root, text="Simple Search GUI", fg="red", font=('Helvetica', 16)).grid(row=0, column=2)
tk.Label(root, text="File name: ").grid(row=1, column=1)
tk.Label(root, text="Search Word: ").grid(row=2, column=1)

searchentry = tk.Entry(root)  # this line is required to get value
filenameentry = tk.Entry(root)  # this line is required to get value

filenameentry.grid(row=1, column=2, ipadx=50)
searchentry.grid(row=2, column=2, ipadx=50)

SelectFile = tk.Button(root, text="Select a File", bg="orange", command=openfile).grid(column=3, row=1)
Search = tk.Button(root, text="Search", bg="orange", command=lambda: findit(searchentry.get(), file_name)) \
    .grid(column=3, row=2)

root.mainloop()
