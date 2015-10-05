import random

__author__ = 'daniel'

use_hoare = False

def lomuto_partition(a, p, r):
    pivot = a[r]  #added -1
    i = p
    for j in range(p, r):
        if a[j] <= pivot:
            swap(a, i, j)
            i += 1
    swap(a, i, r)
    return i


def hoare_partition(a, p, r):
    pivot = a[p]
    i = p - 1
    j = r + 1
    while True:
        while True:  # crappy do-while loop
            j -= 1
            if a[j] <= pivot:
                break
        while True:
            i += 1
            if a[i] >= pivot:
                break
        if i < j:
            swap(a, i, j)
        else:
            return j


def tail_recursive_quicksort(a, p, r):
    while p < r:
        if use_hoare is True:
            q = hoare_partition(a, p, r)
            tail_recursive_quicksort(a, p, q)
            p = q+1
        else:
            q = lomuto_partition(a, p, r)
            tail_recursive_quicksort(a, p, q-1)
            p = q+1


def quicksort(a, p, r):
    if p < r:
        if use_hoare is True:
            q = hoare_partition(a, p, r)
            quicksort(a, p, q)
            quicksort(a, q+1, r)
        else:
            q = lomuto_partition(a, p, r)
            quicksort(a, p, q-1)
            quicksort(a, q+1, r)


def swap(source, index1, index2):
    source[index1], source[index2] = source[index2], source[index1]


def gen_test():
    global test
    test = [random.randint(0, 100) for x in range(1, 10)]
    print test

test = []

gen_test()
tail_recursive_quicksort(test, 0, len(test)-1)
print test
print "\n"

gen_test()
quicksort(test, 0, len(test)-1)
print test
