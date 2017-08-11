from pythonds.trees.binaryTree import BinaryTree

t = BinaryTree('Book')
t.insertLeft('ch1')
ch1 = t.getLeftChild()
ch1.insertLeft('se1.1')
ch1.insertRight('se1.2')
se1_2 = ch1.getRightChild()
se1_2.insertLeft('se1.2.1')
se1_2.insertRight('se1.2.2')
 
t.insertRight('ch2')
ch2 = t.getRightChild()
ch2.insertLeft('se2.1')
ch2.insertRight('se2.2')
se2_2 = ch2.getRightChild()
se2_2.insertLeft('se2.2.1')
se2_2.insertRight('se2.2.2')

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

print('preorder')
preorder(t)

def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

print('inorder')
inorder(t)

def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

print('postorder')
postorder(t)
