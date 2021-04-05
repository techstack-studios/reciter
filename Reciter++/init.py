import os
import json
import tkinter

# 初始化

directory = os.path.dirname(__file__)  # 程序目录
plan_selected = False  # 计划是否被选择
default_language = 0  # 0-zh_cn, 1-en_us
test_started = False  # 测试是否开始
plans_file_exists = False  # 计划文件是否存在
language_filename = os.path.join(directory, "assets", "locale.json")  # 语言文件所在目录
plans_filename = "plans_file.json"  # 计划文件

# 读入语言文件
with open(language_filename, "r", encoding="utf-8") as obj:
    locale = json.loads(obj.read())

# 界面属性设置
tk = tkinter.Tk()
tk.title(locale["TITLE"][default_language])  # 窗口标题
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
