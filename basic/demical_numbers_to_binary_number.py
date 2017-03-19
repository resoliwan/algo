

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


def divideBy2(decNumber):
    remStack = Stack()
    while decNumber > 0:
        remain = decNumber % 2
        remStack.push(remain)
        decNumber = decNumber // 2

    binStr = ""
    while not remStack.isEmpty():
        binStr = binStr + str(remStack.pop())

    return binStr


print(divideBy2(233))


def baseConverter(base, decNumber):
    digits = "0123456789ABCDFGHIJKLMNOPQRSTUVWXYZ"
    remStack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remStack.push(rem)
        decNumber = decNumber // base
    
    newString = ""
    while not remStack.isEmpty():
        newString = newString + str(digits[remStack.pop()])

    return newString


print(baseConverter(8, 233))
print(baseConverter(16, 233))

print(baseConverter(8, 25))
print(baseConverter(16, 256))
print(baseConverter(26, 26))
