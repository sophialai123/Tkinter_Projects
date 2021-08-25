# Tkinter_Projects
from tkinter import  * 


#create a function with button
def button_clink():
    miles = float(miles_input.get())  # to get the value from input which is the entry widget
    miles_to_km = miles * 1.609344
    print(miles_to_km)
    middle_label.config(text=f"{miles_to_km}") # the label will be change actual value



# create a window:
window = Tk()

# create a title:
window.title("Miles to Kilometer Converter")
window.minsize(width =200, height= 200)# screen size

#add pading size x and y, can change location of the layout
window.config(padx=100,pady=100)


#create an entry as an input, and change the size
miles_input = Entry(width=10)

#input.config(padx=50, pady=20)
miles_input.grid(column=2, row=1)


#create 4 labels:
miles_label = Label(text="Miles",font=("Arial", 15, ),padx=10,pady=10)
miles_label.grid(column=3, row=1)


equal_label = Label(text="is equal to", font=("Arial", 15, ))
equal_label.grid(column=1, row=2)


middle_label = Label(text="0", font=("Arial", 15, ))
middle_label.grid(column=2, row=2)


km_label = Label(text="Km", font=("Arial", 15, ))
km_label.grid(column=3, row=2)


#create a button:
button = Button(text="Calculate", font=("Arial", 15, ), command=button_clink) #command is to calling the function
button.grid(column=2, row=3,)



# keep the window open
window.mainloop()
