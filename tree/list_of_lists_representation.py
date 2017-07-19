t1 = ['a',
        ['b', 
            ['d', [], []],
            ['e', [], []]
        ],
        ['c', 
            ['f', [], []],
            []
        ]
    ]
print(t1)
print('root: ', t1[0])
print('left subtree: ', t1[1])
print('right subtree: ', t1[2])

def BinaryTree(r):
    return [r, [], []]

def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root

def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, t, []])
    else:
        root.insert(2, [newBranch, [], []])

def getRoot(root):
    return root[0]

def setRootVal(root, value):
    root[0] = value

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
print(r)
print(l)
