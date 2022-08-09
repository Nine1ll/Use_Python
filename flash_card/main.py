from tkinter import *
from tkinter import messagebox
import pandas
import random
# --- Datas ---

current_card = {}
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"


try:
    words_data = pandas.read_csv("words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    words_data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")

# --- functions ---


def flip_card():
    global current_card
    new_b_word = current_card["English"]
    word_canvas.itemconfig(card_background, image=card_back_image)
    word_canvas.itemconfig(country_text, text="English", fill="white")
    word_canvas.itemconfig(word_text, text=new_b_word, fill="white")


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_data)
    new_f_word = current_card["French"]
    word_canvas.itemconfig(country_text, text="French", fill="black")
    word_canvas.itemconfig(word_text, text=new_f_word, fill="black")
    word_canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, flip_card)


def check_button_command():
    words_data.remove(current_card)
    pandas.DataFrame(words_data).to_csv("data/words_to_learn.csv", index=False)
    next_word()

# ---User Interface---

# Window
window = Tk()
window.title("Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Main
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

word_canvas = Canvas(width=800, height=528, highlightthickness=0, bg=BACKGROUND_COLOR)
card_background = word_canvas.create_image(400, 264, image=card_front_image)
country_text = word_canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
word_text = word_canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
word_canvas.grid(row=0, column=0, columnspan=2)

# Button
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_word)
right_button = Button(image=right_image, highlightthickness=0, command=check_button_command)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

next_word()

window.mainloop()
