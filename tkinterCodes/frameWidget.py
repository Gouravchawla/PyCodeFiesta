# This is program to test frameWidget of Tkinter library

from tkinter import *

root = Tk()

frame1 = Frame(root, relief=RAISED)
frame1.pack()

label1 = Label(frame1, text="This is a label in the first frame", relief=SUNKEN)
label1.pack()


mainloop()
