"""stack"""
"""
install pythond
down http://www.pythonworks.org/pythonds
extarct to file

tar file extarct 
tar -cf pythonds.tar pythonds

conda install
conda install --offline pythonds.tar

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
