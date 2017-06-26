def selectionSort1(alist):
    largestIndex = 0
    for passNum in range(len(alist) - 1, 0, -1):
        for i in range(passNum):
            # print('passNum: {}, i: {}'.format(passNum, i))
            if alist[largestIndex] < alist[i]:
                largestIndex = i

        alist[largestIndex], alist[passNum] = alist[passNum], alist[largestIndex]

    return alist


# alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
# print(selectionSort1(alist))
print(selectionSort1([4, 8, 2]))
