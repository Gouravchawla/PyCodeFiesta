from tkinter import *

def doNothing():
    print("I'm not doing anything! :D")

root = Tk()

#****Menu****

menu1 = Menu(root)
root.config(menu = menu1)
subMenu= Menu(menu1)
menu1.add_cascade(label = "File", menu=subMenu)
subMenu.add_command(label="New project...",command=doNothing)
subMenu.add_command(label="New...", command= doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu=Menu(menu1)
menu1.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

#****Toolbar****
toolbar = Frame(root, bg="#999")

insertButt = Button(toolbar, text="Insert Image", command= doNothing)
insertButt.pack(side = LEFT, padx=2, pady=2)

printButton1 = Button(toolbar, text = "Print!", command=doNothing)
printButton1.pack(side = LEFT, padx=2, pady=2)

printButton2 = Button(toolbar, text = "Print!", command=doNothing)
printButton2.pack(side = LEFT, padx=2, pady=2)

printButton3 = Button(toolbar, text = "Print!", command=doNothing)
printButton3.pack(side = LEFT, padx=2, pady=2)

printButton4 = Button(toolbar, text = "Print!", command=doNothing)
printButton4.pack(side = LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill = X)


#****Status bar****
status = Label(root, text="Trying to process something...", bd=1, relief=SUNKEN, anchor = W)
status.pack(side = BOTTOM, fill = X)

root.mainloop()

