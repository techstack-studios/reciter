
# Words Exam Window

F2 = Frame(tk, width=200, height=200)
F2.grid(row=0, column=2)
B4 = Button(F2, text=language_metadata["Start Exam"][default_language], command=update_word)
B4.grid(row=0, column=0)
L2 = Label(F2, text="")
L2.grid(row=1, column=0)
L2.configure(text="")
E = Entry(F2)
E.grid(row=2, column=0)
B = Button(F2, text=language_metadata["CONFIRM"][default_language], command=confirm)
B.grid(row=3, column=0)
B1 = Button(F2, text=language_metadata["Skip"][default_language], command=skip)
B1.grid(row=4, column=0)


def clear_listbox(the_list_box):
    the_list_box.delete(0, END)


def refresh_listbox(the_list_box, new_list):
    clear_listbox(the_list_box)
    for each in new_list:
        the_list_box.insert(END, each)

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

""" --- """
