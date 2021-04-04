
"""Words List View"""
frame3 = Frame(tk, width=200, height=200)
frame3.grid(row=0, column=1)
left_box2 = Listbox(frame3)
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
