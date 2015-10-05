import random

__author__ = 'daniel'


def max_heapify(a, index, end):
    left = 2*index + 1  # find children based on 0 index
    right = left + 1
    largest = left      # assume that left side is largest until proven wrong
    if left > end:      # "easy" way to store heap size in computation, rather than some other variable.
        return

    if right <= end and a[right] > a[left]:  # check if right side is larger than left
        largest = right
    if a[largest] > a[index]:  # check if index is larger than children.
        print ":".join([str(left), str(right), str(index), str(largest)])
        print ":".join([str(a[left]), str(a[right]), str(a[index]), str(a[largest])])
        swap(a, index, largest)
        print a
        print
        max_heapify(a, largest, end)


def build_max_heap(a):
    for i in range((len(a)-2)/2, -1, -1):  # original pseudocode calls for len(a), but this saves time.
        max_heapify(a, i, len(a)-1)


def heapsort(a):
    build_max_heap(a)
    for end in range(len(a)-1, 0, -1):
        print end
        swap(a, 0, end)
        max_heapify(a, 0, end-1)


def swap(source, index1, index2):
    source[index1], source[index2] = source[index2], source[index1]


def gen_test():
    test = [random.randint(0, 100) for x in range(1, 10)]
    print test
    return test

test01 = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 10]
test02 = [5, 3, 17, 10, 84, 19, 6, 22, 9]

print test01
max_heapify(test01, 2, len(test01))
print test01

print test02
build_max_heap(test02)
print test02

# A1 = gen_test()
# heapsort(A1)
# print A1



