""" This is a basic calculator with GUI built using Tkinter """
# Author: Gourav Chawla
# Ver: 0.0
#Status: Not yed completed


# ****Imports****
from tkinter import *


# ****Business Logic****
class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2


# ****GUI Code****

root = Tk()

#To fix the size of window
root.minsize(width=300, height=500)
root.maxsize(width=300, height=500)

displayFrame = Frame(root, background="#ccc")
displayFrame.pack(side=TOP)

buttonFrame = Frame(root, bg="blue")
buttonFrame.pack(side=BOTTOM)



#****Trying to dynamically create buttons****
# for i in range(17,27):
#   (button + str(i)) = Button(root, text = str(i))
#  (button + str(i)).pack()


root.mainloop()