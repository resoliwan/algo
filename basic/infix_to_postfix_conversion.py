from pythonds.basic.stack import Stack


# A + (B * C) -> ABC*+
# (A * B) + C -> AB*C+
def infixToPostfixConversion(formula):
    operatorMap = {"*": 1, "/": 1, "+": 0, "-": 0}
    result = ""
    opertorStack = Stack()

    for current in formula:
        if current in "+-*/":
            if opertorStack.isEmpty():
                opertorStack.push(current)
            else:
                if operatorMap[current] >= operatorMap[opertorStack.peek()]:
                    result = result + current 
                else:
                    opertorStack.push(current)
        else:
            result = result + current 

    while not opertorStack.isEmpty():
        result = result + opertorStack.pop()
    return result


print(infixToPostfixConversion("A+B*C"))         

