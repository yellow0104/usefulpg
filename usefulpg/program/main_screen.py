import tkinter as tk
from tkinter import Menu, ttk
import os

win = tk.Tk()
win.geometry("700x500+500+300")
win.resizable(False, False)

with open('usefulpg\\txt_zip\\language_setting.txt', 'r', encoding='utf-8') as f:
    language = int(f.read())
with open('usefulpg\\txt_zip\\user_information.txt', 'r', encoding='utf-8') as f:
    user_name = f.read()


def kor():
    if language == 0:
        print('이미 한국어입니다')
    else:
        with open('usefulpg\\txt_zip\\language_setting.txt', 'w', encoding='utf-8') as f:
            f.write('0')
            print(language)
        win.destroy()
        os.system('py usefulpg\program\main_screen.py')

    
def eng():
    if language == 1:
        print('already in english setting')
    else:
        with open('usefulpg\\txt_zip\\language_setting.txt', 'w', encoding='utf-8') as f:
            f.write('1')
            print(language)
        win.destroy()
        os.system('py usefulpg\program\main_screen.py')





text_1 = ['설정', 'setting']
text_2 = ['언어', 'language']


menubar = tk.Menu(win)
menu1 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(menu=menu1, label=text_1[language])
menu2 = tk.Menu(menu1, tearoff=0)
menu2.add_radiobutton(label='한국어', command=kor)
menu2.add_radiobutton(label='english', command=eng)
menu1.add_cascade(menu=menu2, label=text_2[language])

win.config(menu=menubar)

win.mainloop()