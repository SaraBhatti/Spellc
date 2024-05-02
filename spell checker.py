import tkinter
from tkinter import *
from textblob import TextBlob

root = Tk()
root.title("Spelling Checker")
root.geometry("650x400")
root.config(background="#27b8d8")

heading = Label(root, text="Spelling Checker", font=("Comic Sans MS", 20, "bold"), bg="#27b8d8", fg="#2760D8")
heading.pack(pady=(50, 0))

enter_text = Entry(root, justify="center", width=30, font=("Comic Sans MS", 20, "bold"), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

def check_spelling():
    word = enter_text.get()
    a = TextBlob(word)
    right = str(a.correct())

    cs = Label(root, text="Correct text is :", font=("Comic Sans MS", 20), bg="#27b8d8", fg="#2760D8")
    cs.place(x=100, y=250)
    spell.config(text=right)

Button = Button(root, text="Check", font=("Comic Sans MS", 20, "bold"), fg="white", bg="#2760D8", command=check_spelling)
Button.pack()

spell = Label(root, font=("Comic Sans MS", 20), bg="#27b8d8", fg="#2760D8")
spell.place(x=350, y=250)

root.mainloop()
