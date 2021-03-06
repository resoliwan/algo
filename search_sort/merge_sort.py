def mergeSort(alist):
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    leftHalf = alist[:mid]
    rightHalf = alist[mid:]

    mergeSort(leftHalf)
    mergeSort(rightHalf)
    
    i = 0   
    j = 0
    k = 0

    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] < rightHalf[j]:
            alist[k] = leftHalf[i]
            i += 1
        else:
            alist[k] = rightHalf[j]
            j += 1
        k += 1

    while i < len(leftHalf):
        alist[k] = leftHalf[i]
        i += 1
        k += 1

    while j < len(rightHalf):
        alist[k] = rightHalf[j]
        j += 1
        k += 1

    return alist

print(mergeSort([8, 4, 2, 5, 9, 10, 24]))

def mergeSort2(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

# alist = [54,26,93,17,77,31,44,55,20]
# mergeSort(alist)
# print(alist)
