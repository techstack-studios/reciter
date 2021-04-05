from tkinter import *
import tkinter.messagebox
import json
import sys
import os

"""Init"""
tk = Tk()

plan_selected = False
language_filename_txt = "current_language.txt"
try:
    with open(language_filename_txt, "r") as obj:
        default_language = int(obj.read())
except FileNotFoundError:
    default_language = 0
tk_ui_language_var = IntVar()
tk_ui_language_var.set(default_language)
# 0-chn, 1-eng
is_test_start = 0  # 0-not start   1-start
plans_file_exists = False
language_filename = "language_file.json"
plans_filename = "plans_file.json"

with open(language_filename, "r", encoding="utf-8") as obj:
    language_metadata = json.loads(obj.read())

tk.title(language_metadata["Title"][default_language])

current_plan_name = ""
plans = []
all_files = []
all_files1 = os.listdir()
for each in all_files1:
    if ".json" in each and each != "language_file.json":
        all_files.append(each.replace(".json", ""))
plans = all_files

""" --- """

"""Master Menu"""


def write_2_language_file():
    with open(language_filename_txt, "w+") as obj:
        obj.write(str(tk_ui_language_var.get()))
    tkinter.messagebox.showwarning(language_metadata["Title"][default_language],
                                   language_metadata["Restart 2 Apply"][default_language])


master_menu = Menu(tk)
file_menu = Menu(master_menu)
file_menu.add_radiobutton(label="中文 Chinese", variable=tk_ui_language_var, value=0, command=write_2_language_file)
file_menu.add_radiobutton(label="英语 English", variable=tk_ui_language_var, value=1, command=write_2_language_file)
master_menu.add_cascade(
    label=language_metadata["Language Menu"][default_language], menu=file_menu)
tk.config(menu=master_menu)
""" --- """

"""Plans View"""


def new_plan():
    global plans
    plan_name = E1.get()
    if plan_name == '':
        tkinter.messagebox.showwarning(language_metadata["Title"][default_language],
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


def del_selected_plan():
    global plans, word_li
    try:
        plans.remove(current_plan_name)
    except ValueError:
        pass
    refresh_listbox(LB, plans)
    try:
        os.remove(current_plan_name + ".json")
    except FileNotFoundError:
        pass
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
B5 = Button(
    F1, text=language_metadata["Del Selected Plan"][default_language], command=del_selected_plan
)
B5.grid(row=3, column=0)


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
    result = Tk()
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
        if keys != []:
            tkinter.messagebox.showwarning(language_metadata["Title"][default_language],
                                           language_metadata["Plz ChooseP"][default_language])
        else:
            tkinter.messagebox.showwarning(language_metadata["Title"][default_language],
                                           language_metadata["Plz AddWord"][default_language])


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

current_select_word = ""


def get_current_selected_word(event):  # 绑定被选中事件
    global current_select_word
    try:
        current_select_word = LB1.get(LB1.curselection()[0])  # 被选中后自动更新当前被选中词
    except IndexError:  # 如无词 防报错
        pass


def del_selected_word():  # 删除选中词汇
    global word_li, keys, index_of_words, current_plan_name
    """
    1. 从word_li字典中移除
    2. 更新keys
    3. index_of_words -= 1
    4. 使用current_plan_name存盘
    5. 更新UI
    """
    # current_selected_word为英文 是键
    try:
        del word_li[current_select_word]
    except KeyError:
        pass
    set_keys_2_word_li()
    index_of_words -= 1
    with open(current_plan_name + ".json", "w+") as obj:
        obj.write(json.dumps(word_li))
    refresh_listbox(LB1, keys)


def add_word():
    if not plan_selected:
        tkinter.messagebox.showwarning(
            language_metadata["Title"][default_language], language_metadata["Plz CP"][default_language])
    else:
        global word_li
        cur_word_chn = E2.get()
        cur_word_eng = E3.get()
        if cur_word_chn == '' or cur_word_eng == '':
            tkinter.messagebox.showwarning(language_metadata["Title"][default_language],
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
B4 = Button(
    F3, text=language_metadata["Del Selected Word"][default_language], command=del_selected_word)
B4.grid(row=6, column=0)
LB1.bind("<<ListboxSelect>>", func=get_current_selected_word)

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
B = Button(F2, text=language_metadata["Confirm"]
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
