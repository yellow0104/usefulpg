
from tkinter import END, Button, ttk
import tkinter as tk


win = tk.Tk()

scroll_bar = tk.Text(width=30, height=15)
scroll_bar.pack()

def lencommand():
    scroll_len = len(scroll_bar.get(1.0, END))-1
    len_lable.config(text=scroll_len)

button_len = Button(text='cofirm', command=lencommand)
button_len.pack()

len_lable = tk.Label(text='0')
len_lable.pack()

win.mainloop()