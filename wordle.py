import random
import tkinter as tk
from english_words import get_english_words_set

words = get_english_words_set(["web2"], lower=True)

good_words = []

for word in words:
    if len(word) == 5 and word.isalpha():
        good_words.append(word)

words = good_words

secret = random.choice(words)

turn = 0
used = []

window = tk.Tk()
window.title("Wordle")
window.geometry("400x550")

title = tk.Label(window, text="Wordle", font=("Arial", 24))
title.pack()

message = tk.Label(window, text="", font=("Arial", 14))
message.pack()

boxes = []

for x in range(6):
    row = []

    for y in range(5):
        box = tk.Label(
            window,
            text="",
            width=4,
            height=2,
            font=("Arial", 20),
            relief="solid"
        )

        box.grid(row=x, column=y, padx=5, pady=5)

        row.append(box)

    boxes.append(row)


def guess_word():
    global turn

    guess = entry.get().lower()
    entry.delete(0, tk.END)

    if len(guess) != 5:
        message.config(text="Enter 5 letters")
        return

    if guess not in words:
        message.config(text="Not a real word")
        return

    if guess in used:
        message.config(text="Already guessed")
        return

    used.append(guess)

    for x in range(5):
        boxes[turn][x]["text"] = guess[x]

        if guess[x] == secret[x]:
            boxes[turn][x]["bg"] = "green"
            boxes[turn][x]["fg"] = "white"

        elif guess[x] in secret:
            boxes[turn][x]["bg"] = "yellow"

        else:
            boxes[turn][x]["bg"] = "gray"
            boxes[turn][x]["fg"] = "white"

    turn += 1

    if guess == secret:
        message.config(text="You won in " + str(turn) + " turns!")
        entry.config(state="disabled")

    elif turn == 6:
        message.config(text="The word was " + secret)
        entry.config(state="disabled")


entry = tk.Entry(window, font=("Arial", 18))
entry.pack(pady=20)

button = tk.Button(window, text="Guess", command=guess_word)
button.pack()

window.bind("<Return>", lambda x: guess_word())

window.mainloop()
