def shellSort0(alist, nOfSublists):
    for n in range(nOfSublists, 0, -1):
        gap = int(len(alist) / n)
        if gap == len(alist):
            gap = 1
            
        for subId in range(n):
            for i in range(subId, len(alist), gap):
                # i = subId + gap
                newItem = alist[i]
                print('n {}, gap {}, subId {} i {} newItem {} preItem {}'.format(n, gap, subId, i, alist[i], alist[i - gap]))
                while i > 0 and alist[i - gap] > newItem:
                    alist[i] = alist[i - gap]
                    i -= gap
                alist[i] = newItem

def shellSort(alist):
    sublistCount = len(alist) // 2
    while sublistCount > 0:

        for startPoistion in range(sublistCount):
            insertionSort(alist, startPoistion, sublistCount)

        sublistCount = sublistCount // 2
    return alist

def insertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        position = i
        currentValue = alist[position]

        while position >= gap and alist[position - gap] > currentValue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentValue

    return alist



def shellSort2(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

# alist = [54,26,93,17,77,31,44,55,20]
# shellSort(alist)
# print(alist)

print(shellSort([8, 4, 2, 5, 6, 7]))
# print(shellSort2([8, 4, 2, 5, 6, 7]))
