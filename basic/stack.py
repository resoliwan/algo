"""stack"""
"""
install pythond
down http://www.pythonworks.org/pythonds
extarct to file

tar file extarct 
tar -cf pythonds.tar pythonds

conda install
conda install --offline pythonds.tar

from pythonds.basic.stack import Stack
"""


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)


class StackFromTop:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.insert(0, item)

    def peek(self):
        return self.items[0]

    def pop(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def main():
    s = StackFromTop()
    print(s.isEmpty())
    s.push(4)
    s.push("dog")
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())


main()


def main2():
    m = Stack()
    m.push('x')
    m.push('y')
    m.push('z')
    while not m.isEmpty():
        m.pop()
        m.pop()


main2()


# Balanced Parentheses
class ParenthesesChecker:
    def check(self, string):
        parentheses = list(string)
        s = Stack()

        for i in range(len(parentheses)):
            character = parentheses[i]
            if character == "(":
                s.push(character)
                parentheses[i] = None
            elif character == ")" and not s.isEmpty():
                s.pop()
                parentheses[i] = None
       
        print(parentheses)
        if not s.isEmpty():
            return False

        for i in parentheses:
            print("i is not None: {}".format(i))
            if i is not None:
                return False

        return True


def main3():
    checker = ParenthesesChecker()
    print(checker.check("(()()(())())()("))


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        
        index = index+1

    if balanced and s.isEmpty():
        return True
    else:
        return False


parChecker("(()(())())")
parChecker("(()(())()))")


def parGeneralChecker(symbolString):
    parPairs = {"(": ")", "[": "]", "{": "}"}
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in parPairs.keys():
            s.push(symbol)
        else:
            if s.isEmpty() or not parPairs[s.pop()] == symbol:
                balanced = False

        index = index+1

    if balanced and s.isEmpty():
        return True
    else:
        return False


parGeneralChecker("{}([]()(())())")
parGeneralChecker("{(()(())()))}")


def parGeneralChecker2(symbolString):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "({[":
            s.push(symbol)
        else:
            if s.isEmpty() or not matches(s.pop(), symbol):
                balanced = False

        index = index+1

    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    opens = "({[{"
    closes = "]})"
    return opens.index(open) == closes.index(close)


parGeneralChecker2("{}([]()(())())")
parGeneralChecker2("{(()(())()))}")
