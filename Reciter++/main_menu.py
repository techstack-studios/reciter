

# 主目录
master_menu = Menu(tk)  # 创建主窗口
file_menu = Menu(master_menu)  # 窗口菜单
master_menu.add_cascade(
    label=language_metadata["FILES"][default_language], menu=file_menu)  # 加入“帮助”菜单
tk.config(menu=master_menu)  # 设置菜单

