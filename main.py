import tkinter
from tkinter import *

# create a window
window = Tk()


#change the size of the window:
window.minsize(width=500, height=600)

#add pading size x and y
window.config(padx=100,pady=200)

#create a label
my_label = Label()
my_label.config(text="Label",font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


#creat a new button
new_button = Button()
new_button.config(text="New button")
new_button.grid(column=3,row=0)


#create a button
button = Button()
button.config(text="button")
button.grid(column=2, row=2)


#create a entry as input
input = Entry()
input.grid(column=3, row=4)



#keep the screen open
window.mainloop()