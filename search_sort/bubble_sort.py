def bubbleSort(alist):
    for k in range(len(alist) - 1):
        for i in range(len(alist) - 1):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i+1] = alist[i + 1], alist[i]

    return alist

# alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
# print(bubbleSort(alist))
# alist = [200, 10, 40, 90, 45, 60, 70, 80, 100, 9]
# print(bubbleSort(alist))
# print(bubbleSort([8, 4, 2]))

def bubbleSort2(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
    return alist


# print(bubbleSort2([8, 4, 2]))

def shortBubbleSort(alist):
    passnum = len(alist) - 1
    exchanges = True
    while passnum >= 0 and exchanges:
        exchages = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                exchanges = True
        passnum -= 1
    return alist
        

print(shortBubbleSort([8, 4, 2]))
