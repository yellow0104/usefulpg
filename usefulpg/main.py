from tkinter import ttk
import tkinter as tk
from program import singup
import os



with open("usefulpg\\txt_zip\\user_information.txt", 'r', encoding='utf-8') as f:
    user_name = f.read()
    print(user_name)
if user_name == "":
    singup.singup_fuc()
else:
    os.system('py usefulpg\\program\\main_screen.py')