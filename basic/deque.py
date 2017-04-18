"""
Deque() creates a new dequeu that is empty. it needs no parameter and return an empty deque.
addFront(item) add a new item to the front of the deque. It needs item and returns nothing.
addRear(item) add a new item to the rear of the deque. It needs item and returns nothing.
removeFront() removes front item from the deque. It needs no parameters and return the items. The deque is modified.
removeRear() removes rear item from the deque. It needs no parameter and return the item. The deque is modified.
isEmpty() tests to see whether the deque is empty. It needs no paramter and returns a boolean value.
size() returns the number of item in the deque. It needs no parameter and returns an integers.
"""

class Deque():
    def __init__(self):
        self.items = []
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item):
        self.items.insert(0, item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def isEmpty(self):
        return self.iemes == []
    def size(self):
        return len(self.items)

from pythonds.basic import Stack

class PalindromeChecker():
    def check(self, string):
        l = list(string)
        l.reverse()
        return string == "".join(l)
p = PalindromeChecker()
print(p.check("madam"))
print(p.check("madama"))


class PalindromeChecker2():
    def check(self, string):
        stillEqual = True
        charDeque = Deque()
        for s in list(string):
            charDeque.addRear(s)
        while charDeque.size() > 1 and stillEqual:
            if charDeque.removeRear() == charDeque.removeFront():
                stillEqual = False
        return stillEqual
p = PalindromeChecker2()
print(p.check("madam"))
print(p.check("madama"))
