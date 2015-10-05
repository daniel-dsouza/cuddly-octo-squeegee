__author__ = 'daniel'

charArray = ['1', '2', '3', 'a']

i = 0

def rev():
    global i
    local = i
   # print i
    if i != 3:
        i += 1
        rev()
    print charArray[local]


rev()
