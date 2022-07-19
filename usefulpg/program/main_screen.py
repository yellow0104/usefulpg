import tkinter as tk
from tkinter import Button, Menu, ttk
import os

import webview

import requests
from bs4 import BeautifulSoup

win = tk.Tk()
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
text_3 = ['뉴스', 'news']

def bt1_news():
    window = webview.create_window(f'{one}', link_list[one])
    webview.start()
def bt2_news():
    window = webview.create_window(f'{two}', link_list[two])
    webview.start()

res = requests.get('https://m.news.naver.com/main?mode=LSD&sid1=100')
soup = BeautifulSoup(res.text, 'lxml')
text = soup.find_all('strong', attrs={'class':"sh_text_headline"})
links = soup.find_all('a', attrs={'class':'sh_thumb_link'})

link_list = {}
one = ''
two = ''
one2 = ''
two2 = ''
for link in links:
        l = link['href']
        if one2 == '':
            one2 += l
        else:
            two2 += l

for title in text:
    
        
    t = title.get_text()
    
    if one == '':
        one += t
        
    else:
        two += t
    link_list[one] = one2
    link_list[two] = two2
    
print(link_list) 
one_bt = tk.Button(text=one, command=bt1_news, padx=10, pady=2)
two_bt = tk.Button(text=two, command=bt2_news, padx=10, pady=2)
label_title = tk.Label(text=text_3[language])
label_title.grid(column=0, row=1)
label_main_title = tk.Label(text=f"{user_name} hello!")
label_main_title.grid(column=0, row=0)

one_bt.grid(column=0, row=2)
two_bt.grid(column=0, row=3)





menubar = tk.Menu(win)
menu1 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(menu=menu1, label=text_1[language])
menu2 = tk.Menu(menu1, tearoff=0)
menu2.add_radiobutton(label='한국어', command=kor)
menu2.add_radiobutton(label='english', command=eng)
menu1.add_cascade(menu=menu2, label=text_2[language])

win.config(menu=menubar)

win.mainloop()
