from pythonds.basic.queue import Queue

# Our program will input a list of names and a constant, call it 'num' , to be used for counting
# It will return the name of the last person remain after repetitive counting by num.
# What happen at this point is up to you
# Queue act like a circle and counting continue back at the begining until the value is reached


def hotPotato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    return queue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
