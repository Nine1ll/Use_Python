import random
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_to_database():
    if len(website_input.get()) == 0 or len(password_input.get()) == 0 or len(e_user_input.get()) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave a ny fields empty!")
    else :
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {e_user_input.get()}\nPassword: {password_input.get()} \n"
                                               f"Is it ok to save?")
        if is_ok:
            with open("password_database.txt", mode="a") as database:
                database.write(f"{website_input.get()} | {e_user_input.get()} | {password_input.get()}\n")
                website_input.delete(0, END)
                e_user_input.delete(0, END)
                password_input.delete(0, END)
                e_user_input.insert(END, "@gmail.com")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas

canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(120, 120, image=mypass_img)
canvas.grid(column=1, row=0)

# Label

website = Label(text="Website: ")
website.grid(column=0, row=1)
e_user = Label(text="Email/Username: ")
e_user.grid(column=0, row=2)
passwords = Label(text="Password: ")
passwords.grid(column=0, row=3)

# Entry

website_input = Entry(width=40)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
e_user_input = Entry(width=40)
e_user_input.grid(column=1, row=2, columnspan=2)
e_user_input.insert(END, "@gmail.com")
password_input = Entry(width=18)
password_input.grid(column=1, row=3)

# Button

g_password = Button(text="Generate Password", width=18, command=generate_password)
g_password.grid(column=2, row=3)
add = Button(text="Add", width=40, command=add_to_database)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()
