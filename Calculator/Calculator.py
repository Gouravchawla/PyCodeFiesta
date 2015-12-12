""" This is a basic calculator with GUI built using Tkinter """
#Author: Gourav Chawla
#Ver: 0.0
#Status: Not yet completed


# ****Imports****
from tkinter import *

# ****Bussiness Logic****
class Calculator:
    def add(self, num1, num2):
        return num1+num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2



ob = Calculator()

# ****GUI Code****

root = Tk()

#To fix the size of window
root.minsize(width = 300, height = 500)
root.maxsize(width = 300, height = 500)


# Frame : labelFrame
labelFrame = Frame(root)
labelFrame.pack(side = LEFT)


# Frame : inputFrame
inputFrame = Frame(root)
inputFrame.pack(side = RIGHT)


number1 = Label(labelFrame, text="Number 1:")
number1.pack()

number2 = Label(labelFrame,text = "Number 2:")
number2.pack()

resultButton = Button(labelFrame,text="Result:", command = lambda:ob.add(int(number1)+int(number2)))
resultButton.pack(side = LEFT)



number1_entry = Entry(inputFrame)
number1_entry.pack()

number2_entry = Entry(inputFrame)
number2_entry.pack()


resultLabel = Label(inputFrame, text=resultButton.cget("command"))
resultLabel.pack()




#****Trying to dynamically create buttons****
#for i in range(17,27):
#   (button + str(i)) = Button(root, text = str(i))
#  (button + str(i)).pack()


root.mainloop()
