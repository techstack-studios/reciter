from tkinter import *
import tkinter.messagebox
import json
import sys
import os

"""Init"""
default_language = 0
# 0 - Chinese
# 1 - English
plans_file_exists = False
language_filename = "language_file.json"
plans_filename = "plans_file.json"

with open(language_filename, "r") as obj:
    language_metadata = json.loads(obj.read())
try:
    with open(plans_filename) as obj:
        plans_file = json.loads(obj.read())
        plans_file_exists = True
except FileNotFoundError:
    pass

tk = Tk()
tk.title(language_metadata["Title"][default_language])

current_plan_name = ""
plans = []
all_files = []
for each in all_files:
    if ".json" not in each or language_filename == each:
        all_files.remove(each)
plans = all_files

""" --- """

"""Master Menu"""


def clear_listbox(the_list_box):
    the_list_box.delete(0, END)


def refresh_listbox(the_list_box, new_list):
    clear_listbox()
    for each in new_list:
        the_list_box.insert(END, each)


def new_words():
    pass


def new_plan():
    pass


master_menu = Menu(tk)
file_menu = Menu(master_menu)
master_menu.add_cascade(label=language_metadata["File Menu"][default_language], menu=file_menu)
tk.config(menu=master_menu)
""" --- """

"""Plans View"""
F1 = Frame(tk, width=200, height=200)
F1.grid(row=0, column=0)
LB = Listbox(F1)
LB.grid(row=0, column=0)
E1 = Entry(F1)
E1.grid(row=1, column=0)
B2 = Button(F1, text=language_metadata["Create New Plan"][default_language], command=new_plan())
B2.grid(row=2, column=0)

for each in plans:
    LB.insert(END, each)

""" --- """

"""Words List View"""
F3 = Frame(tk, width=200, height=200)
F3.grid(row=0, column=1)
LB1 = Listbox(F3)
LB1.grid(row=0, column=0)
E2 = Entry(F3)
E2.grid(row=1, column=0)
L = Label(F3, text=language_metadata["Chinese"][default_language])
L.grid(row=2, column=0)
E3 = Entry(F3)
E3.grid(row=3, column=0)
L1 = Label(F3, text=language_metadata["English"][default_language])
L1.grid(row=4, column=0)
""" --- """

"""Words Exam Window"""
F2 = Frame(tk, width=200, height=200)
F2.grid(row=0, column=2)
E = Entry(F2)
E.grid(row=1, column=0)
B = Button(F2, text=language_metadata["Confirm"][default_language])
B.grid(row=2, column=0)
B1 = Button(F2, text=language_metadata["Skip"][default_language])
B1.grid(row=3, column=0)

""" --- """

tk.mainloop()
