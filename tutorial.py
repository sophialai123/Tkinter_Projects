"""
documentation:
https://docs.python.org/3/library/tkinter.html#the-packer



How to use advanced python arguments
Keyword Arguments with default values

def my_function(a=1, b=2, c=3):
    #do this with a
    #then do this with b
    #finally do this with c
my_function () # no need to provide any values here
my_function(b=5) # if ONLY change the value of b, the rest will be the same


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)

#out_put= 4 (7,3,0) {"x": 10 , "y":64}



# Unlimited Arguments also called: Unlimited positional arguments

def add(* args): # *args can accept any number of arguments, args format will be tuple ()
    for n in args:  # also can loop through args
        print(n)


add(4,6, 7, 9) # can pass any numbers inside, unlimited

# get the sum of *args
def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)

add(4, 7, 3, 10)

# **Kwargs : Many Keywored Arguments:
def calculate(**kwargs):  # create unlimited keyword arguments
    print(kwargs)  # a dictionary will be print it out
    for key,value in kwargs.items(): # can loop through the kwargs
        print(key)
        print(value)
        print(kwargs["add"])  # access the value by pass the key


calculate(add=3, multiply=5)   # output = {'add': 3, 'multiply': 5}

import turtle
t = turtle.Turtle()
t.write("Hello this is the text value, other wants will  be default value")
"""




## Demo from udemy:

import tkinter

#create a new window:
window = tkinter.Tk()

# change the title:
window.title("My first GUI program")

#change the size of the window:
window.minsize(width=500, height=600)
#add pading size x and y
window.config(padx=100,pady=200)


#create a function with button

def button_clink():
    print("I got clicked")
    #my_label.config(text="Button got clicked") # the label will be change
    new_text = input.get() # get() will get the input value
    my_label.config(text= new_text) # the text will change as input


#create a Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold")) # font will be tuple: 字体，大小，粗细
#my_label.pack()  #pack() will be show on the screen in the centre by defualt, side will change the value


my_label["text"] = "New text" # change or Update the text, same as below:
my_label.config(text="New text")
#my_label.place(x=100, y=110) # place in an exactly position
my_label.grid(column=0, row=0) # when use the grid, the pack cannot be used.
# adding pading x and y in my_label
my_label.config(padx=50,pady=50)




#create a button class
# change the text, command can use the name of  function, but to calling the function
button = tkinter.Button(text= "Click me", command=button_clink) # will print output everytime, clink the button
button.grid(column=1, row=1)
#button.pack() # keep the screen open


# Entry class input
#http://tcl.tk/man/tcl8.6/TkCmd/entry.htm
input= tkinter.Entry(width=10)
#input.pack()
print(input.get()) # to return the entry's string
input.grid(column=2, row=2)



## Tkinter Layout Managers :: **** Pack and Grid cannot be used at the same time
# Pack: start from top and the buttom, can change the side
# Place: exactly the position: my_label.place(x= 0, y= 0)
# Grid: Row, Column




#keep the window running:
window.mainloop()


