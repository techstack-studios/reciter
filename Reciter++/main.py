import json
import os
import tkinter
from tkinter import Frame, Button, Label, Menu, Entry, messagebox, END

# 初始化

directory = os.path.dirname(__file__)  # 程序目录
plan_selected = False  # 计划是否选择
default_language = 0  # 0-zh_cn, 1-en_us
test_started = False  # 测试是否开始
plans_file_exists = False  # 计划文件是否存在
language_filename = os.path.join(directory, "assets", "locale.json")  # 语言文件所在目录
plans_filename = "plans_file.json"  # 计划文件

# 读入语言文件

with open(language_filename, "r", encoding="utf-8") as obj:
    language_metadata = json.loads(obj.read())

# 界面属性设置
tk = tkinter.Tk()
tk.title(language_metadata["TITLE"][default_language])  # 窗口标题
tk.iconbitmap(os.path.join(directory, "assets", "AppIcon.ico"))  # 窗口图标

# 读入计划
current_plan_name = ""  # 当前计划
plans = []  # 计划列表
all_files = []
all_files1 = os.listdir()  # 读取目录下所有文件
for each in all_files1:  # 循环遍历
    if ".json" in each and each != "language_file.json":  # 判断是否不是语言文件
        all_files.append(each.replace(".json", ""))  # 将计划文件加入计划列表
plans = all_files

# 主目录
master_menu = Menu(tk)  # 创建主窗口
file_menu = Menu(master_menu)  # 窗口菜单
master_menu.add_cascade(
    label=language_metadata["FILE_MENU"][default_language], menu=file_menu)  # 加入“帮助”菜单
tk.config(menu=master_menu)  # 设置菜单


# 计划

def new_plan():
    global plans
    plan_name = entry1.get()
    if plan_name == '':  # 没有计划名
        tkinter.messagebox.showwarning(language_metadata["TITLE"][default_language],
                                       language_metadata["CantBeEmpty"][default_language])  # 警告用户计划名不能为空
    else:  # 有计划名
        plans.append(plan_name)  # 添加计划
        refresh_listbox(left_box, plans)  # 刷新计划列表
        entry1.delete(0, END)  # idk


def get_current_plan(event):
    global plan_selected, current_plan_name, word_li, index_of_words
    index_of_words = 0
    plan_selected = True
    try:
        current_plan_name = left_box.get(left_box.curselection()[0])
    except IndexError:
        pass
    try:
        with open(current_plan_name + ".json", "r", encoding="utf-8") as obj:
            word_li = json.loads(obj.read())
    except FileNotFoundError:
        word_li = {}
    set_keys_2_word_li()
    refresh_listbox(LB1, keys)


frame1 = Frame(tk, width=200, height=200)  # 框架1
frame1.grid(row=0, column=0)
left_box = Listbox(frame1)  # 多行文本框 ——计划列表
left_box.grid(row=0, column=0)
left_box.bind("<<ListboxSelect>>", func=get_current_plan)  # 绑定事件 ——当前事件更新
entry1 = Entry(frame1)  # 文本框1
entry1.grid(row=1, column=0)
buttom2 = Button(
    frame1, text=language_metadata["Create New Plan"][default_language], command=new_plan)  # 按钮2 ——创建计划
buttom2.grid(row=2, column=0)

for each in plans:
    left_box.insert(END, each)  # 将计划加入计划列表

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


# 测试结果反馈
def show_result():
    global index_of_words, crosses, ticks
    E.delete(0, END)
    result = tkinter.Tk()
    result.iconbitmap(os.path.join(directory, "assets", "AppIcon.ico"))
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
    global test_started
    if index_of_words == len(keys) - 1:
        test_started = 0
        return True
    else:
        return False


def update_word():
    global test_started

    try:
        L2.configure(text=keys[index_of_words])
        test_started = 1
    except IndexError:
        tkinter.messagebox.showwarning(language_metadata["TITLE"][default_language],
                                       language_metadata["Plz ChooseP"][default_language])
        pass


def confirm():
    global index_of_words, ticks, crosses, test_started
    if test_started == 0:
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
    if test_started == 0:
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
frame3 = Frame(tk, width=200, height=200)
frame3.grid(row=0, column=1)
letf_box2 = Listbox(frame3)
left_box2.grid(row=0, column=0)
E2 = Entry(frame3)
E2.grid(row=1, column=0)
L = Label(frame3, text=language_metadata["Chinese"][default_language])
L.grid(row=2, column=0)
E3 = Entry(frame3)
E3.grid(row=3, column=0)
L1 = Label(frame3, text=language_metadata["English"][default_language])
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
    frame3, text=language_metadata["Add New Word"][default_language], command=add_word)
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
B = Button(F2, text=language_metadata["CONFIRM"] \
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
