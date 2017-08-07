class BinaryHeap():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, item):
        self.heapList.append(item)
        self.currentSize += 1
        self.percolateUp(self.currentSize)

    def percolateUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2] :
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2],  self.heapList[i]
            i = i // 2

    def __str__(self):
        print(self.heapList)
        return ''

b = BinaryHeap()
b.insert(5)
b.insert(1)
b.insert(9)
b.insert(3)
b.insert(10)

print(b)


        

