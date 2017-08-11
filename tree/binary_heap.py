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
            if self.heapList[i] < self.heapList[i // 2] :
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2],  self.heapList[i]
            i = i // 2

    def getMin(self):
        minEle = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percolateDown(1)

    def percolateDown(self, i):
        while (i * 2) + 1 < self.currentSize:
            mc = self.minChild(i)
            self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[(i * 2) + 1]:
                return i * 2
            else: 
                return (i * 2) + 1

    def __str__(self):
        print(self.heapList)
        return ''

b = BinaryHeap()
b.insert(5)
b.insert(1)
b.insert(9)
b.insert(3)
b.insert(10)
b.insert(7)
b.insert(4)

print(b)

print(b.getMin())
print(b)
print(b.getMin())
print(b)
print(b.getMin())
print(b)

        

