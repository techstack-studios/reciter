from tkinter import *
import tkinter.messagebox
import json
import sys
import os

"""Init"""
plan_selected = False
default_language = 0
# 0 - Chinese
# 1 - English
plans_file_exists = False
language_filename = "language_file.json"
plans_filename = "plans_file.json"

with open(language_filename, "r", encoding="utf-8") as obj:
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

master_menu = Menu(tk)
file_menu = Menu(master_menu)
master_menu.add_cascade(label=language_metadata["File Menu"][default_language], menu=file_menu)
tk.config(menu=master_menu)
""" --- """


"""Plans View"""


def new_plan():
    global plans
    plans.append(E1.get())
    refresh_listbox(LB, plans)


def get_current_plan(the_list_box):
    print(the_list_box.curselection())


F1 = Frame(tk, width=200, height=200)
F1.grid(row=0, column=0)
LB = Listbox(F1, command=)
LB.grid(row=0, column=0)
E1 = Entry(F1)
E1.grid(row=1, column=0)
B2 = Button(F1, text=language_metadata["Create New Plan"][default_language], command=new_plan)
B2.grid(row=2, column=0)





""" --- """

# For debug
word_li = {}
index_of_words = ticks = crosses = 0
keys = []


def set_keys_2_word_li():
    global keys
    keys = []
    fake_keys = list(word_li.items())
    for each in fake_keys:
        keys.append(each[0])


def show_result():
    global index_of_words, crosses, ticks
    result = Tk()
    result.title(language_metadata["Result"][default_language])
    Tick_L = Label(result, text=language_metadata["Ticks"][default_language] + str(ticks))
    Wrong_L = Label(result, text=language_metadata["Wrongs"][default_language] + str(crosses))
    Tick_L.grid(row=0, column=0)
    Wrong_L.grid(row=1, column=0)
    Tick_percent_L = Label(result, text=language_metadata["Tick Percent"][default_language] + str(ticks / (ticks + crosses) * 100) + "%")
    Wrong_percent_L = Label(result, text=language_metadata["Wrong Percent"][default_language] + str(crosses / (ticks + crosses) * 100) + "%")
    Tick_percent_L.grid(row=2, column=0)
    Wrong_percent_L.grid(row=3, column=0)
    index_of_words = crosses = ticks = 0
    update_word()


def check_if_finished():
    if index_of_words == len(keys) - 1:
        return True


def update_word():
    L2.configure(text=keys[index_of_words])


def confirm():
    global index_of_words, ticks, crosses
    if E.get() == word_li[keys[index_of_words]]:
        ticks += 1
    else:
        crosses += 1
    if check_if_finished():
        show_result()
    index_of_words += 1
    update_word()


def skip():
    global index_of_words, crosses
    if check_if_finished():
        show_result()
    index_of_words += 1
    crosses += 1
    update_word()


# For debug


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


def add_word():
    global word_li
    word_li[E3.get()] = E2.get()
    set_keys_2_word_li()
    refresh_listbox(LB1, keys)



B3 = Button(F3, text=language_metadata["Add New Word"][default_language], command=add_word)
B3.grid(row=5, column=0)

""" --- """

"""Words Exam Window"""

F2 = Frame(tk, width=200, height=200)
F2.grid(row=0, column=2)
B4 = Button(F2, text=language_metadata["Start Exam"][default_language], command=update_word)
B4.grid(row=0, column=0)
L2 = Label(F2, text="")
L2.grid(row=1, column=0)
L2.configure(text="")
E = Entry(F2)
E.grid(row=2, column=0)
B = Button(F2, text=language_metadata["Confirm"][default_language], command=confirm)
B.grid(row=3, column=0)
B1 = Button(F2, text=language_metadata["Skip"][default_language], command=skip)
B1.grid(row=4, column=0)


def clear_listbox(the_list_box):
    the_list_box.delete(0, END)


def refresh_listbox(the_list_box, new_list):
    clear_listbox(the_list_box)
    for each in new_list:
        the_list_box.insert(END, each)


""" --- """

tk.mainloop()
