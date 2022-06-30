from tkinter import *
import pandas as pd
import os.path

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

# ------------------------------------ load Data Frame----------------------------------------- #
try:
    words_data = pd.read_csv("./data/french_words.csv", index_col="French")

except FileNotFoundError:
    words_data = pd.read_csv("words_to_learn.csv", index_col="French")

current_card_set = pd.DataFrame()
french_word = str()


# -------------------------------------- CARD SHUFFLE------------------------------------------- #
def next_card():
    global current_card_set, flip_timer, french_word
    window.after_cancel(flip_timer)
    current_card_set = words_data.sample()
    french_word = current_card_set.index[0]

    card.itemconfig(card_set, image=card_front_img)

    card.itemconfig(text_title, text="French", fill="#000000")
    card.itemconfig(text_word, text=french_word, fill="#000000")
    flip_timer = window.after(3000, card_flipped)  # Upon seeing the next card, the card would be flipped in 5s


def card_flipped():
    english_word = current_card_set.iloc[0]["English"]

    card.itemconfig(card_set, image=card_back_img)

    card.itemconfig(text_title, text="English", fill="#FFFFFF")
    card.itemconfig(text_word, text=english_word, fill="#FFFFFF")


def cards_update_by_remove():
    global current_card_set, french_word
    words_data.drop(french_word, inplace=True)
    words_data.to_csv("words_to_learn.csv")


# ---------------------------------------- UI SETUP--------------------------------------------- #
# window
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, card_flipped)

# canvas widget
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

card = Canvas(width=800, height=526)
card_set = card.create_image(400, 263, image=card_front_img)
text_title = card.create_text(400, 150, text="", font=TITLE_FONT)
text_word = card.create_text(400, 263, text="", font=WORD_FONT)

card.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card.grid(row=0, column=0, columnspan=2)

# button widget
x_button_img = PhotoImage(file="./images/wrong.png")
x_button = Button(image=x_button_img, highlightthickness=0, command=next_card)
x_button.grid(row=1, column=0)

check_button_img = PhotoImage(file="./images/right.png")
check_button = Button(image=check_button_img, highlightthickness=0, command=lambda: [cards_update_by_remove(), next_card()])
check_button.grid(row=1, column=1)

next_card()

window.mainloop()
