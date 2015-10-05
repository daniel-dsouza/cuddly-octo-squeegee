import random

__author__ = 'daniel'

colors = ['R', 'W', 'B']
test = [random.choice(colors) for x in range(1, 10)]
print test


def dutch_flag(seq):
    bottom = 0
    center = 0
    top = len(seq)-1
    for element in seq:
        if seq[center] == 'R':
            swap(seq, bottom, center)
            bottom += 1
            center += 1
        elif seq[center] == 'W':
            center += 1
        elif seq[center] == 'B':
            swap(seq, center, top)
            top -= 1
    print seq


def swap(list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]

dutch_flag(test)
