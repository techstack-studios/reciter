import numpy as np

from collections import defaultdict

poems_queue = np.load('poems_queue.npy', allow_pickle='TRUE').item()


def print_poem_queue(num):
        print(poems_queue['title'])
        print(poems_queue['dynasty'])
        print(poems_queue['author'])
        print(poems_queue['content'].replace('。', '。\n'))

    else:
        print(poems_queue[num]['title'])
        print(poems_queue[num]['dynasty'])
        print(poems_queue[num]['author'])
        print(poems_queue[num]['content'].replace('。', '。\n'))


print(type(poems_queue))

#for i in range(0, len(poems_queue)):
#    print('This is a poem waiting for vertification:\n')
#    print_poem_queue(i)


print(poems_queue)