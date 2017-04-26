



class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    def getData(self):
        return self.data
    def setData(self, newData):
        self.data = newData
    def getNext(self):
        return self.next
    def setNext(self, newNext):
        self.next = newNext


class UnorderedList():
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head is None
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getNext()
        return count
    def search(self, item):
        current = self.head
        found = False
        while current is not None or not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())



