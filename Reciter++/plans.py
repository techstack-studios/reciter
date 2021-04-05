
# 计划

def new_plan():
    global plans
    plan_name = entry1.get()
    if plan_name == '':  # 没有计划名
        tkinter.messagebox.showwarning(language_metadata["TITLE"][default_language],
                                       language_metadata["WARNING_EMPTY"][default_language])  # 警告用户计划名不能为空
    else:  # 有计划名
        plans.append(plan_name)  # 添加计划
        refresh_listbox(LB1, plans)  # 刷新计划列表
        entry1.delete(0, END)  # idk


def get_current_plan(event):
    global plan_selected, current_plan_name, word_li, index_of_words
    index_of_words = 0
    plan_selected = True
    try:
        current_plan_name = LB1.get(LB1.curselection()[0])
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
LB1 = Listbox(frame1)  # 多行文本框 ——计划列表
LB1.grid(row=0, column=0)
LB1.bind("<<ListboxSelect>>", func=get_current_plan)  # 绑定事件 ——当前事件更新
entry1 = Entry(frame1)  # 文本框1
entry1.grid(row=1, column=0)
bottom2 = Button(
    frame1, text=language_metadata["BUTTON_NEW_WL"][default_language], command=new_plan)  # 按钮2 ——创建计划
bottom2.grid(row=2, column=0)

for each in plans:
    LB1.insert(END, each)  # 将计划加入计划列表
