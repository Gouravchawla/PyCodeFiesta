"""This is a string length calculator program with GUI support"""
# Version : 0.1
# Author  : Gourav Chawla

from tkinter import *


# Function to calculate string length
def calculateLength():
    """Function to calculate the length of string without using the len() function. It appends the null character '\0' to the string and counts from 0 to that null
       character. When that null character is encountered, function stops and sets the IntVar variable for displayLabel. The IntVar is displayed on the screen"""
    
    counter = 0     #Counter variable
    i = 0           #iterator
    tempString = inputString.get() + "\0" #appending '\0' to find out end of string

    # while loop which goes from 0 to end of the string
    while tempString[i] != "\0":
        i += 1
        counter += 1

    lengthOfString.set(counter)
    displayLabel.pack()


## end of calculateLength function


## Start of GUI programming
    
root = Tk()
inputString = StringVar()
lengthOfString = IntVar()
root.title("String Calculator")

# Frame 1 for input area
inputFrame = Frame(root).pack()

#Label for String text box
labelInput = Label(inputFrame, text = "Enter String").pack()

# Entry box for String input
inputEntry = Entry(inputFrame, width = 70, textvariable = inputString, relief = SUNKEN, bd=10).pack()


#Frame for button
buttonFrame = Frame(root).pack()


# Button for Calculation command
calculateButton = Button(buttonFrame, text= "Calculate", command = calculateLength).pack()

# Label for displaying length of string
displayLabel = Label(buttonFrame, textvariable = lengthOfString)

root.mainloop()


## End of GUI programming
