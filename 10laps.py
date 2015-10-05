import random

__author__ = 'daniel'


def get_start_index(lst):
    smallest_index = 0
    smallest_sum = sum(lst[0: 10])
    for start in range(1, len(lst)-10):
        print lst[start: start+10]
        if sum(lst[start: start+10]) < smallest_sum:
            smallest_index = start
    print smallest_index


def gen_test():
    test = [random.randint(0, 100) for x in range(1, 21)]
    print test
    return test

test = gen_test()
get_start_index(test)