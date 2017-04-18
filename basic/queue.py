# Queue
# Queue Create a new queue that is empty 
#    it needs no parameter and returns an empty queue.
# enqueue(item) Add a new item at the rear of the queue. It need the item and
#  returns nothing
# dequeue() Remove the front item from the queue. It need no parameters and
#  return the item.
# isEmpty() Tests to see whether queue is empty. It need no parmeters  
#  and return boolean values
# size() Return the number of items in the queue. It need no parameters 
#  and return Integer.


class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
q.dequeue()
