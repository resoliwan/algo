class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, key, value):
        if self.root is None:
            self.root = TreeNode(value, value)
        else:
            _put(self, key, value, self.root)
    
    def _put(self, key, value, currentNode):
        if currentNode.key < key:
            if currentNode.hasLeftChild():
                self._put(key, value, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, value, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, value, parent=currentNode)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root.key == key:
            return None
        else:
            return self._get(self, key, self.root)

    def _get(self, key, currentNode):
        if currentNode is None:
            return None
        elif currentNode.key == key:
            return currentNode
        elif currentNode.key < key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)
    
    def __contain__(self, key):
        return self.get(key) is not None





class TreeNode:
    def __init__(self, key, value, leftChild, rightChild, parent):
        self.key = key
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent



