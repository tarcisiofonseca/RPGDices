import random
from tkinter import *
import PyPDF2

def roll():
    dice_type = int(en1.get())
    dice_number = int(en2.get())
    lista = []
    for a in range(1, dice_number + 1):
        cont = random.randint(1, dice_type)
        lista.append(cont)
    lb3["text"] = lista

window = Tk()

lb1 = Label(window, text="How many faces have the dice? ")
lb2 = Label(window, text="How many times do you want to roll the dice? ")
en1 = Entry(window)
en2 = Entry(window)
lb3 = Label(window, text="Result")
photo = PhotoImage(file="dice.png")
lbf = Label(window, image=photo)
enc = Label(window, text="Encounter")

lb1.grid(row=1, column=0, pady=10)
en1.grid(row=2, column=0)
lb2.grid(row=3, column=0)
en2.grid(row=4, column=0)
lb3.grid(row=5, column=0, pady=20)
lbf.grid(row=0, column=0)
enc.grid(row=1, column=12)

roll = Button(window, width=20, text="Roll!", command=roll)
roll.grid(row=6, column=0, padx=5, pady=5)

window.geometry("580x300")
window.title("RPG Dices")
window.mainloop()
