from random import randint
import time

__author__ = 'daniel'

A = [0]*10000000
for i in range(0, len(A)):
    A[i] = randint(1, 1000000)

# print A


# more correct
def counting_sort(a):
    start = time.clock()
    r = max(a) - min(a)
    small = min(a)
    b = [0]*(r+1)
    c = [0]*(len(a))

    for i in a:
        b[i-1-small] += 1

    for i in range(1, len(b)):
        b[i] += b[i-1]

    for i in range(0, len(a)):
        c[b[a[i]-1-small]-1] = a[i]
        b[a[i]-1-small] -= 1

    end = time.clock()
    return end-start


# few subtractions, but an additional index in b.
def faster_counting_sort(a):
    start = time.clock()
    r = max(a) - min(a)
    small = min(a)
    b = [0]*(r+2)
    c = [0]*(len(a))

    for i in a:
        b[i-small] += 1

    for i in range(1, len(b)):
        b[i] += b[i-1]

    for i in range(0, len(a)):
        c[b[a[i]-small]-1] = a[i]
        b[a[i]-small] -= 1

    end = time.clock()
    return end-start

print counting_sort(A)
print faster_counting_sort(A)

