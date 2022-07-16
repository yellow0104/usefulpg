
from tkinter import messagebox, ttk
import tkinter as tk
import os


    


def singup_fuc():
    user_join_win = tk.Tk()
    with open('usefulpg\\txt_zip\\language_setting.txt', 'r', encoding='utf-8') as f:
        language = int(f.read())
        print(language)




    def kor():
        if language == 0:
            print('이미 한국어입니다')
        else:
            with open('usefulpg\\txt_zip\\language_setting.txt', 'w', encoding='utf-8') as f:
                f.write('0')
                print(language)
            user_join_win.destroy()
            os.system('py usefulpg\program\singup.py')

        
    def eng():
        if language == 1:
            print('already in english setting')
        else:
            with open('usefulpg\\txt_zip\\language_setting.txt', 'w', encoding='utf-8') as f:
                f.write('1')
                print(language)
            user_join_win.destroy()
            os.system('py usefulpg\program\singup.py')


        


    text_1 = ['안녕하세요!\n이곳은 처음이신가보군요!\n당신의 이름은 무엇입니까?', 'hello!\nare you first time here?\nwhat are you name?']
    text_2 = ['확인', 'ok']
    text_3 = ['설정', 'setting']
    text_4 = ['언어', 'language']
    text_5 = ['이름을 입력하세요', 'it is blank.']
    text_6 = ['닉네임을 이것으로 하시겠습니까?', 'your final decision']

    def confirm():
        if username_entry.get() == '':
            messagebox.showerror('usefulpg', text_5[language])
        else:
            ask = messagebox.askquestion('usefulpg', text_6[language])
            if ask == 'yes':
                with open('usefulpg\\txt_zip\\user_information.txt', "w", encoding="utf-8") as f:
                    f.write(username_entry.get())
                user_join_win.destroy()
                os.system('py usefulpg\main.py')
            elif ask == 'no':
                pass
            


    menubar = tk.Menu(user_join_win)

    menu_setting = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label=text_3[language], menu=menu_setting)
    user_join_win.config(menu=menubar)

    menu2 = tk.Menu(menu_setting, tearoff=0)
    menu_setting.add_cascade(label=f'{text_4[language]}', menu=menu2)
    menu2.add_radiobutton(label='한국어', command=kor)
    menu2.add_radiobutton(label='english', command=eng)

    user_join_win.geometry("300x200+750+400")
    user_join_win.resizable(False, False)

    label_hi = tk.Label(text=text_1[language], font=("맑은고딕",10))
    label_hi.pack()

    username_entry = tk.Entry()
    username_bt = tk.Button(text=text_2[language],command=confirm)



    username_entry.pack()
    username_bt.pack()

    user_join_win.mainloop()


if __name__ == "__main__":
    singup_fuc()
    print('singup.py run singup.py')
else:
    print('modul')