import tkinter as tk

window = tk.Tk()
window.title('PyStart')

label = tk.Label(window, text="Jak masz na imie?")
label.pack()

first_name = tk.Entry()
first_name.pack()

window.mainloop()
