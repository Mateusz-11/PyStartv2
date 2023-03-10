import tkinter as tk
from random import randint
from tkinter import messagebox


def on_submit():
    global prevoius_difference, steps

    steps += 1
    value = int(field.get())
    difference = abs(target - value)
    print(value)
    print(target)

    if difference == 0:
        messagebox.showinfo('Stan', f'Gratulacje, zgadles! Zgadles w krokach: {steps}')
    elif prevoius_difference is None or difference < prevoius_difference:
        messagebox.showinfo('Stan', 'Cieplej!')
    else:
        messagebox.showinfo('Stan', 'Zimniej!')

    prevoius_difference = difference

steps = 0
prevoius_difference = None
target = randint(1, 100)

window = tk.Tk()
window.title('Zgadnij liczbe')

label = tk.Label(window, text='Wprowadz liczbe')
label.pack()

field = tk.Entry()
field.pack()

button = tk.Button(text='Zgaduje!', command=on_submit)
button.pack()

window.mainloop()
