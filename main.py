from tkinter import *
import pandas as pd
import random

unknown_words = []

BACKGROUND_COLOR = "#B1DDC6"


random_dict = {}


# Read the data from the csv file and convert to a dictionary
try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')
    to_learn = data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

# print(data_dict)


# Create a function to generate french word


def next_card():
    global random_dict, flip_time
    # A random dictionary is picked from the list of dictionaries
    random_dict = random.choice(to_learn)
    front_canvas.itemconfig(front_image, image=first_image)
    front_canvas.itemconfig(french_title, text='French', fill="black")
    front_canvas.itemconfig(french_text, text=random_dict['French'], fill="black")
    # The buttons are disabled while the french words are on the screen
    window.after_cancel(flip_time)
    flip_time = window.after(3000, flip_card)


# If the right button is pressed
def right_button():
    # The random dictionary is deleted from the list of dictionaries
    to_learn.remove(random_dict)
    next_card()
    (pd.DataFrame(to_learn).to_csv('data/words_to_learn.csv', header=True,  index=False))


# A new random dictionary is picked from the updated list of dictionaries


# The English words are shown
def flip_card():
    global random_dict
    front_canvas.itemconfig(front_image, image=back_image)
    front_canvas.itemconfig(french_title, text='English', fill="white")
    front_canvas.itemconfig(french_text, text=random_dict['English'], fill="white")
    # The buttons are set to normal in order to change the card


# -------------------------------------U.I------------------------------------ #
# Create a window
window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_time = window.after(3000, func=flip_card)

# Create two canvases, one for the front and one for the back
# Front canvas
front_canvas = Canvas(height=600, width=850, bg=BACKGROUND_COLOR, highlightthickness=0)
first_image = PhotoImage(file="images/card_front.png")
front_image = front_canvas.create_image(425, 275, image=first_image)
# Add text to the canvas
french_title = front_canvas.create_text(425, 150, text=" ", font=('Arial', 40, 'italic'))
french_text = front_canvas.create_text(425, 275, text=" ", font=('Arial', 60, 'bold'))
front_canvas.grid(column=0, row=1, columnspan=3)

# Back Canvas Image
back_image = PhotoImage(file="images/card_back.png")

# Create buttons
# Create right button
right_button = Button(highlightthickness=0, bd=0, command=right_button)
right_image = PhotoImage(file="images/right.png")
right_button.config(image=right_image)
right_button.grid(row=2, column=2)
# Create wrong button
wrong_button = Button(highlightthickness=0, bd=0, command=next_card)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button.config(image=wrong_image)
wrong_button.grid(row=2, column=0)


# Call the next card function

next_card()

# with open("unknown_words.json", "w") as p:
#     json.dump(unknown_words, p, indent=4)

window.mainloop()
