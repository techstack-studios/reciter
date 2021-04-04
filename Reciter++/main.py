import json
import os
import tkinter
from tkinter import Frame, Button, Listbox, Label, Menu, Entry, messagebox, END

# Init

cwd = os.path.dirname(__file__)
plan_selected = False
default_language = 0  # 0-chn, 1-eng
is_test_start = 0  # 0-not start   1-start
plans_file_exists = False
language_filename = os.path.join(cwd, "assets", "locale.json")
plans_filename = "plans_file.json"

with open(language_filename, "r", encoding="utf-8") as obj:
    language_metadata = json.loads(obj.read())

tk = tkinter.Tk()
tk.title(language_metadata["TITLE"][default_language])
tk.iconbitmap(os.path.join(cwd, "assets", "AppIcon.ico"))

current_plan_name = ""
plans = []
all_files = []
all_files1 = os.listdir()
for each in all_files1:
    if ".json" in each and each != "language_file.json":
        all_files.append(each.replace(".json", ""))
plans = all_files




"""Master Menu"""

master_menu = Menu(tk)
file_menu = Menu(master_menu)
master_menu.add_cascade(
    label=language_metadata["FILE_MENU"][default_language], menu=file_menu)
tk.config(menu=master_menu)
""" --- """

"""Plans View"""


def new_plan():
    global plans
    plan_name = E1.get()
    if plan_name == '':
        tkinter.messagebox.showwarning(language_metadata["TITLE"][default_language],
                                       language_metadata["CantBeEmpty"][default_language])
    else:
        plans.append(plan_name)
        refresh_listbox(LB, plans)
        E1.delete(0, END)


def get_current_plan(event):
    global plan_selected, current_plan_name, word_li, index_of_words
    index_of_words = 0
    plan_selected = True
    try:
        current_plan_name = LB.get(LB.curselection()[0])
    except IndexError:
        pass
    try:
        with open(current_plan_name + ".json", "r", encoding="utf-8") as obj:
            word_li = json.loads(obj.read())
    except FileNotFoundError:
        word_li = {}
    set_keys_2_word_li()
    refresh_listbox(LB1, keys)


F1 = Frame(tk, width=200, height=200)
F1.grid(row=0, column=0)
LB = Listbox(F1)
LB.grid(row=0, column=0)
LB.bind("<<ListboxSelect>>", func=get_current_plan)
E1 = Entry(F1)
E1.grid(row=1, column=0)
B2 = Button(
    F1, text=language_metadata["Create New Plan"][default_language], command=new_plan)
B2.grid(row=2, column=0)

for each in plans:
    LB.insert(END, each)

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
    E.delete(0, END)
    result = tkinter.Tk()
    result.iconbitmap(os.path.join(cwd, "assets", "AppIcon.ico"))
    result.title(language_metadata["Result"][default_language])
    tick_l = Label(
        result, text=language_metadata["Ticks"][default_language] + str(ticks))
    wrong_l = Label(
        result, text=language_metadata["Wrongs"][default_language] + str(crosses))
    tick_l.grid(row=0, column=0)
    wrong_l.grid(row=1, column=0)
    tick_percent_l = Label(result, text=language_metadata["Tick Percent"][default_language] + str(
        round((ticks / (ticks + crosses) * 100), 2)) + "%")
    wrong_percent_l = Label(result, text=language_metadata["Wrong Percent"][default_language] + str(
        round((crosses / (ticks + crosses) * 100), 2)) + "%")
    tick_percent_l.grid(row=2, column=0)
    wrong_percent_l.grid(row=3, column=0)
    index_of_words = crosses = ticks = 0
    L2.configure(text='')


def check_if_finished():
    global is_test_start
    if index_of_words == len(keys) - 1:
        is_test_start = 0
        return True


def update_word():
    global is_test_start

    try:
        L2.configure(text=keys[index_of_words])
        is_test_start = 1
    except IndexError:
        tkinter.messagebox.showwarning(language_metadata["TITLE"][default_language],
                                       language_metadata["Plz ChooseP"][default_language])
        pass


def confirm():

    global index_of_words, ticks, crosses, is_test_start
    if is_test_start == 0:
        tkinter.messagebox.showwarning(language_metadata["Title"][default_language],
                                       language_metadata["PlzStartTest"][default_language])
    else:
        if E.get() == word_li[keys[index_of_words]]:
            ticks += 1
        else:
            crosses += 1
        if check_if_finished():
            show_result()
            return
        index_of_words += 1
        update_word()
        E.delete(0, END)


def skip():
    global index_of_words, crosses
    if is_test_start == 0:
        tkinter.messagebox.showwarning(language_metadata["Title"][default_language],
                                       language_metadata["PlzStartTest"][default_language])
    else:
        crosses += 1
        if check_if_finished():
            show_result()
            return
        index_of_words += 1
        update_word()
        E.delete(0, END)


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
    if not plan_selected:
        tkinter.messagebox.showwarning(
            language_metadata["TITLE"][default_language], language_metadata["Plz CP"][default_language])
    else:
        global word_li
        cur_word_chn = E2.get()
        cur_word_eng = E3.get()
        if cur_word_chn == '' or cur_word_eng == '':
            tkinter.messagebox.showwarning(language_metadata["TITLE"][default_language],
                                           language_metadata["CantBeEmpty"][default_language])
        else:
            word_li[cur_word_eng] = cur_word_chn
            set_keys_2_word_li()
            refresh_listbox(LB1, keys)
            E2.delete(0, END)
            E3.delete(0, END)
            try:
                with open(current_plan_name + ".json", "w+", encoding="utf-8") as obj:
                    obj.write(json.dumps(word_li))
            except FileNotFoundError:
                pass


B3 = Button(
    F3, text=language_metadata["Add New Word"][default_language], command=add_word)
B3.grid(row=5, column=0)

""" --- """

"""Words Exam Window"""

F2 = Frame(tk, width=200, height=200)
F2.grid(row=0, column=2)
B4 = Button(F2, text=language_metadata["Start Exam"]
[default_language], command=update_word)
B4.grid(row=0, column=0)
L2 = Label(F2, text="")
L2.grid(row=1, column=0)
L2.configure(text="")
E = Entry(F2)
E.grid(row=2, column=0)
B = Button(F2, text=language_metadata["CONFIRM"]
[default_language], command=confirm)
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
