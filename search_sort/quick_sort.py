def startQuickSort(alist):
   sortHelper(alist, 0, 1, len(alist) - 1)
   return alist

def sortHelper(alist, p, l, r):
    if (r - p) < 2:
        return 
    split = sort(alist, p, l, r)
    sortHelper(alist, p, p + 1, split - 1)
    sortHelper(alist, split + 1, split + 2, r)

def sort(alist, p, l, r):
    # print('p: {}, l: {}, r: {}, alist: {}'.format(p, l, r, alist))
    done = False
    while not done:
        while alist[l] < alist[p] and l < r:
            l += 1
        while alist[r] > alist[p] and r >= l:
            r -= 1
        # print('  while l , r increasem p: {}, l: {}, r: {}, alist: {}'.format(p, l, r, alist))
        if l < r:
            alist[l], alist[r] = alist[r], alist[l]
        else:
            done = True

    # print('  before change pivot p: {}, l: {}, r: {}, alist: {}'.format(p, l, r, alist))
    alist[p], alist[r] = alist[r], alist[p]
    return r
    # print('  end p: {}, l: {}, r: {}, alist: {}'.format(p, l, r, alist))




print(startQuickSort([5, 1, 9, 8, 3, 4, 7]))

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
