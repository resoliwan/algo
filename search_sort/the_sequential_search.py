def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1

    return found

# print(sequentialSearch([1, 2, 3], 3))
# print(sequentialSearch([1, 2, 3], 4))

def orderedSequentialSearch(alist, item):
    found = False
    stop = False
    pos = 0
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        elif alist[pos] > item:
            stop = True
        else:
            pos += 1

    return found

# print(orderedSequentialSearch([1, 2, 3], 3))
# print(orderedSequentialSearch([1, 2, 5], 4))

def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first < last and not found:
        midpoint = (first + last) // 2
        if item == alist[midpoint]:
            found = True
        else:
            if item > alist[midpoint]:
                first = midpoint + 1
            else:
                last = midpoint - 1

    return found

print(binarySearch([2, 4, 8, 16, 32], 8))
print(binarySearch([2, 4, 8, 16, 32], 17))

# print(binarySearch([5, 6, 7, 8, 9], 9))
# print(binarySearch([1, 2, 5], 4))
