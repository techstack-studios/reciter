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


# For debug


tk.mainloop()
