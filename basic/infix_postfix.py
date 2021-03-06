from pythonds.basic import Stack


def infixToPostFix2(infixexpr):
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    opStack = Stack()
    output = []
    tokens = list(infixexpr)
    for token in tokens:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            output.append(token)
        elif token in "(":
            opStack.push(token)
        elif token in ")":
            top = opStack.pop()
            while top != "(":
                output.append(top)
                top = opStack.pop()
        elif token in "+-*/":
            while not opStack.isEmpty() and \
                    prec[opStack.peek()] >= prec[token]:
                output.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        output.append(opStack.pop())
    return "".join(output)


print(infixToPostFix2("A+B*C+D"))
print(infixToPostFix2("(A+B)*C+D"))
print(infixToPostFix2("( A + B ) * ( C + D )"))
print(infixToPostFix2("( A + B ) * C"))
print(infixToPostFix2("A + B * C"))


def doMath(operator, operand1, operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2


def postfixEval(postfixExpr):
    opStack = Stack()
    tokens = list(postfixExpr)
    for token in tokens:
        if token in "0123456789":
            opStack.push(int(token))
        elif token in "+-*/":
            operand2 = opStack.pop()
            operand1 = opStack.pop()
            result = doMath(token, operand1, operand2)
            opStack.push(result)
    return opStack.pop()


print(postfixEvaluation("12+"))
print(postfixEvaluation("78+32+/"))
