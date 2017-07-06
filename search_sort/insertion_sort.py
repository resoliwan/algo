def insertionSort1(alist):
    for next in range(1, len(alist)):
        for i in range(next):
            # print('next: {}, i:{}'.format(next, i))
            if alist[next] < alist[i]:
                alist[next], alist[i] = alist[i], alist[next]
    return alist


# print(insertionSort1([8, 4, 2, 5]))

def insertionSort2(alist):
    for i in range(1, len(alist)):
        newItem = alist[i]
        # print('next: {}, i: {}, newItem: {}'.format(next, i, newItem))
        while i > 0 and newItem < alist[i - 1]:
            alist[i] = alist[i - 1]
            i -= 1

        alist[i] = newItem

    return alist

print(insertionSort2([8, 4, 2, 5, 10 , 9]))
