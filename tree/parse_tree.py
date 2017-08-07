from pythonds.trees.binaryTree import BinaryTree
from pythonds.basic.stack import Stack


def parseTree(expression):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    operators = ['+', '-', '*', '/']
    stack = 
    root = BinaryTree(None)
    stack 

    for char in list(expression):
        if char == '(':
            cur.insertLeft(None)
            return cur.getLeftChild()
        if char in operators:
            cur.setRootVal(char)
            cur.rightChild(None)
            return cur.getRightChild()
        if char in numbers:
            cur.setRootVal(char)
            return cur
        if char == ')':
            return

expression = '(3+(4*5))'

parseTree(root, expression)



