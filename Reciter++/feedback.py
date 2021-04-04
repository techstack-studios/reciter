import tkinter

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


