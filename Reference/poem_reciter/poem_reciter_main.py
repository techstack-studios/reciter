import numpy as np
import json
import random
from enum import Enum

from collections import defaultdict

poems = np.load('poems.npy', allow_pickle='TRUE').item()

# with open('poems.json', 'r') as f_read:
#    poems = json.dump(data, f_read)

poems_queue = []


class Mode(Enum):
    START = 'start'
    RECITE = 'recite'
    ADD = 'add'
    SAVE = 'save'
    END = 'end'


cur_mode = Mode.START


def sleep(continue_input):
    while (not continue_input == input('type go to continue...\n')):
        pass


def change_mode():
    global cur_mode
    cur_mode = Mode(input(
        'type start to start, recite to practice reciting poems, add to add poems to our poem_lib, and end to quit.\n'))


def print_poem(title, random_cnt):
    if (len(poems[title]) == 0):
        print('No poems found!')

    for i in range(len(poems[title])):
        print(poems[title][i]['title'])
        print(poems[title][i]['dynasty'])
        print(poems[title][i]['author'])
        content_clone = poems[title][i]['content']
        for i in range(0, int(random_cnt) + 1):
            content_clone = content_clone.replace(random.choice(
                content_clone.replace('。', '').replace('，', '')), '*')
        print(content_clone)


def add_poem():
    print('all inputs must be in one line!\n')

    title = input('input title: ')
    dynasty = input('input dynasty: ')
    author = input('input author: ')
    content = input('input content: ')

    double_check = input("are you sure you want to add this poem? (y/n)")

    if (double_check == 'n'):
        return

    poem = {
            'title': title,
            'dynasty': dynasty,
            'author': author,
            'content': content
        }

    poems[title].append(poem)

    print('poem successfuly added to queue!')


def save_poem():
    np.save('poems_queue.npy', poems_queue)

    with open('poems_queue.json', 'w') as f_write:
        json.dump(poems_queue, f_write, indent = 4)

    print('sent to vertification queue, waiting for vertification!')


def recite_poem(title):

    poem_len = len(poems[title][0]['content'])

    print('Lets start by reading it a few times:\n')
    print_poem(title, 0)
    sleep('go')
    print('Now lets take out some characters, see if you can recite it now!\n')
    print_poem(title, poem_len / 20)
    sleep('go')
    print('Now lets take out some characters, see if you can recite it now!\n')
    print_poem(title, poem_len / 10)
    sleep('go')
    print('Now lets take out some characters, see if you can recite it now!\n')
    print_poem(title, poem_len / 7.5)
    sleep('go')
    print('Now lets take out some characters, see if you can recite it now!\n')
    print_poem(title, poem_len / 5)
    sleep('go')
    print('Now lets take out some characters, see if you can recite it now!\n')
    print_poem(title, poem_len / 2.5)
    sleep('go')
    print('Now lets take out some characters, see if you can recite it now!\n')
    print_poem(title, poem_len / 2)
    sleep('go')
    print('Now lets take out some characters, see if you can recite it now!\n')
    print_poem(title, poem_len)
    sleep('go')


while(1):

    if (cur_mode == Mode.START):
        print('Welcome to poem reciter v1.0!')
    elif (cur_mode == Mode.RECITE):
        input_poem = input('search: ')
        recite_poem(input_poem)

    elif (cur_mode == Mode.ADD):
        add_poem()

    elif (cur_mode == Mode.SAVE):
        save_poem()

    elif (cur_mode == Mode.END):
        break

    change_mode()
