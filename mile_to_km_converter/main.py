from tkinter import *


def button_clicked():
    miles = int(input_mile.get())
    kms = miles * 1.609
    converted_km.config(text=kms)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100) #여백

# Entry
input_mile = Entry(width=10)
input_mile.grid(column=1, row=0)

# Label
mile = Label(text="Miles", font=("Arial", 24, "bold"))
mile.grid(column=2, row=0)

is_equal_to = Label(text="is equal to", font=("Arial", 24, "bold"))
is_equal_to.grid(column=0, row=1)

converted_km = Label(text="0", font=("Arial", 24, "bold"))
converted_km.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 24, "bold"))
km.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()
