def startQuickSort(alist):
    if len(alist) < 1:
        return alist
    quickSort(alist, 0, 1, len(alist) - 1)
    return alist


def quickSort(alist, p, l, r):
    pivot = p
    leftmark = l
    rightmark = r
    print('pivot: {}, leftmark: {}, rightmark: {}'.format(pivot, leftmark, rightmark))
    if leftmark == pivot:
        return
    if leftmark >= rightmark:
        if alist[leftmark] > alist[rightmark]:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
        return

    while leftmark < rightmark:
        print(leftmark, rightmark)
        while alist[pivot] > alist[leftmark] and leftmark < rightmark:
            leftmark += 1
        while alist[pivot] < alist[rightmark] and  leftmark < rightmark:
            rightmark -= 1 
        print(leftmark, rightmark)
        alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    print(alist)
    print('after pivot: {}, leftmark: {}, rightmark: {}'.format(pivot, leftmark, rightmark))
    alist[pivot], alist[rightmark] = alist[rightmark], alist[pivot]
    print(alist)
    quickSort(alist, p, (p + 1), (rightmark - 1))
    quickSort(alist, (rightmark + 1), (rightmark + 2), r)

print(startQuickSort([8, 4, 5, 9, 10]))
