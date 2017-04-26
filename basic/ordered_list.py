"""

"""


class Node():
    def __init__(self, data):
        self.next = None
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, node):
        self.next = node

    def getNext(self):
        return self.next


class OrderedList():
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current is not None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self, item):
        temp = Node(item)
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
