from tkinter import * # type: ignore
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    words_dataframe = pandas.read_csv("Flash Card\\data\\words_to_learn.csv")
except FileNotFoundError:
    words_dataframe = pandas.read_csv("Flash Card\\data\\french_words.csv")

words_dictionary = words_dataframe.to_dict(orient="records")
current_card = {}
def generate_random():
    global current_card, flip_after_timer
    window.after_cancel(flip_after_timer)
    current_card = random.choice(words_dictionary)
    canvas.itemconfig(current_language, text="French", fill="black")
    canvas.itemconfig(current_word, text=current_card["French"], fill="black")
    canvas.itemconfig(current_image, image=front_card_image)
    flip_after_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(current_language, text="English", fill="white")
    canvas.itemconfig(current_word, text=current_card["English"], fill="white")
    canvas.itemconfig(current_image, image=back_card_image)

def is_known_card():
    words_dictionary.remove(current_card)

    data = pandas.DataFrame(words_dictionary)
    data.to_csv("Flash Card\\data\\words_to_learn.csv")
    generate_random()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_after_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_card_image = PhotoImage(file="Flash Card\\images\\card_front.png")
back_card_image = PhotoImage(file="Flash Card\\images\\card_back.png")
current_image = canvas.create_image(400, 236, image=front_card_image)
current_language = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
current_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="Flash Card\\images\\wrong.png")
not_correct_button = Button(image=cross_image, highlightthickness=0, command=generate_random)
not_correct_button.grid(row=1, column=0)

tick_image = PhotoImage(file="Flash Card\\images\\right.png")
correct_button = Button(image=tick_image, highlightthickness=0, command=is_known_card)
correct_button.grid(row=1, column=1)

generate_random();

window.mainloop()
