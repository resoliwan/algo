def insertionSort1(alist):
    for next in range(1, len(alist)):
        for i in range(next):
            # print('next: {}, i:{}'.format(next, i))
            if alist[next] < alist[i]:
                alist[next], alist[i] = alist[i], alist[next]
    return alist


print(insertionSort1([8, 4, 2, 5]))
