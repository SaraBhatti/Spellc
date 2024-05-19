import sys
print(sys.path)
import tkinter as tk
from tkinter import ttk
from textblob import TextBlob

root = tk.Tk()
root.title("Spelling Checker")
root.geometry("650x400")
root.config(background="#F38DAA")

heading = tk.Label(root, text="Spelling Checker", font=("Comic Sans MS", 20, "bold"), bg="#AAB1DB", fg="#2760D8")
heading.pack(pady=(50, 0))

def round_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

# Create a canvas for the entry box
entry_canvas = tk.Canvas(root, width=400, height=60, bg="#F38DAA", highlightthickness=0)
entry_canvas.pack(pady=10)
round_rectangle(entry_canvas, 10, 10, 390, 50, radius=20, fill="white")

enter_text = tk.Entry(root, justify="center", width=25, font=("Comic Sans MS", 20, "bold"), bg="white", border=0)
entry_canvas.create_window(200, 30, window=enter_text)

enter_text.focus()

def check_spelling():
    word = enter_text.get()
    a = TextBlob(word)
    right = str(a.correct())

    cs = tk.Label(root, text="Correct text is :", font=("Comic Sans MS", 20), bg="#F6A673", fg="#976EDA")
    cs.place(x=100, y=250)
    spell.config(text=right)

# Create a canvas for the button
button_canvas = tk.Canvas(root, width=150, height=60, bg="#F38DAA", highlightthickness=0)
button_canvas.pack(pady=10)
round_rectangle(button_canvas, 10, 10, 140, 50, radius=20, fill="#976FDB")

check_button = tk.Button(root, text="Check", font=("Comic Sans MS", 20, "bold"), fg="white", bg="#976FDB", border=0, command=check_spelling)
button_canvas.create_window(75, 30, window=check_button)

spell = tk.Label(root, font=("Comic Sans MS", 20), bg="#F6A673", fg="#976EDA")
spell.place(x=350, y=250)

root.mainloop()
