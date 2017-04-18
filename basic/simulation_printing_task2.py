from pythonds.basic.queue import Queue
import time
import random
from statistics import mean


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask is not None:    
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        return self.currentTask is not None

    def startNext(self, newTask):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages() * 60/self.pagerate


class Task:
    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.pages = random.randint(1, 20)

    def getTimestamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currentTime):
        return currentTime - self.timestamp

def newPrintTask():
    return random.randint(0, 180) == 180

def simulation(numSeconds, pagePerMinute):
    printer = Printer(pagePerMinute)
    queue = Queue()
    waitingTimes = []
    
    for currentSecond in range(numSeconds):
        if newPrintTask():
            queue.enqueue(Task(currentSecond))

        if (not queue.isEmpty()) and (not printer.busy()):
            nextTask = queue.dequeue()
            waitingTimes.append(nextTask.waitTime(currentSecond))
            printer.startNext(nextTask)

        printer.tick()
    
    averageMinutes = sum(waitingTimes)/len(waitingTimes)/60
    print(averageMinutes) 

for i in range(0, 10):
    simulation(3600, 5)

for i in range(0, 10):
    simulation(3600, 10)



