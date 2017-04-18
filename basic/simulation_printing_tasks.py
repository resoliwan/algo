"""
# Simulation printing tasks.
## Main simulation step.

Input:
    Tasks ranges from 1 to 20 pages.
Limit:
    Student have to get printed task before they go to class.
Ouput:
    What page rate shold be used?
        1. 5 page per minutes
        2. 10 page per minutes

Scenario:
    On any average day about 10 students are woking in the lab at any given hour.
    These students typically print up to twice during that time.

    Students make task and put it in the queue.
    Printer check the queue and take it from the queue if it is not busy.
    Printer print the task.
    Of interest us is the average amount of time students will wait for their paper to be printed.

Algorithmn:
    - Create a queue of print tasks. Each task will be given a timestamp upon its arrival. The queue is empty to start.
    - For each second(currentSecond):
        Students make a task by generating a random number between 1 to 180 inclusive. If a number is 180, we say a task has been created.
        Dose a new print task get created? If so, add it to the queue with the currentSecond as the timestamp.
        If the task is not busy and if a task is waiting.
            Remove the next task from the print queue and assign it to the printer.
            Substract the timestamp from the currentSecond to compute the waiting time for that task.
            Append the waiting time to the list for later processing.
            Based on the number of pages in the print task. Figure out how much time will be required.
        The printer dose one second of printing if necessory. It also substracts one second from the time required for that task.
        If the task has been completed, in other words the time required has reached zero. the printer is no longer busy.
    - After the simulation is complete, compute the avereage time from the list of the waiting times generated.
"""

from pythonds.basic.queue import Queue
import time
import random
from statistics import mean


class Printer:
    def __init__(self, rateOfPrintPerMinute):
        self.rateOfPrintPerMinute = rateOfPrintPerMinute
        self.tasks = []
        self.task = None
        self.remainSecond = 0
    def assign(self, task, currentSecond):
        task.printStart(currentSecond)
        self.task = task
        self.remainSecond = task.getRemainPageCount() * 60/self.rateOfPrintPerMinute
    def printForOneSecond(self):
        self.remainSecond = self.remainSecond - 1
        if self.remainSecond <= 0:
            self.tasks.append(self.task)
            self.task = None
    def isBusy(self):
        return self.task is not None
    def getTasks(self):
        return self.tasks


class Task:
    def __init__(self, currentSecond):
        self.startSecond = currentSecond
        self.remainPageCount = self.pageCount = random.randint(1, 20)
        # self.remainPageCount = 20
        self.waitingSecond = 0
    def getWaitingSecond(self):
        return self.waitingSecond
    def printStart(self, currentSecond):
        self.waitingSecond = currentSecond - self.startSecond
    def getRemainPageCount(self):
        return self.remainPageCount


class PrinterSimulation:
    def newTaskCreated(self):
        return random.randint(1, 180) == 180
    def simulate(self, rateOfPrintPerMinute):
        printer = Printer(rateOfPrintPerMinute)
        printQueue = Queue()
        totalSimulateHour = 24 
        totalSimulateSecond = totalSimulateHour * 60 * 60
        for currentSecond in range(0, totalSimulateSecond):
            if self.newTaskCreated():
                printQueue.enqueue(Task(currentSecond))
            if not printQueue.isEmpty() and not printer.isBusy():
                printer.assign(printQueue.dequeue(), currentSecond)
            if printer.isBusy():
                printer.printForOneSecond()
        while not printQueue.isEmpty() and not printer.isBusy():
            currentSecond = currentSecond + 1
            if not printQueue.isEmpty() and not printer.isBusy():
                printer.assign(printQueue.dequeue(), currentSecond)
            if printer.isBusy():
                printer.printForOneSecond()
        tasks = printer.getTasks()
        # print([tasks.getWaitingSecond() for tasks in tasks])
        # print(len(tasks))
        # print(mean([tasks.getWaitingSecond() for tasks in tasks]))
        return mean([tasks.getWaitingSecond() for tasks in tasks])/60

p = PrinterSimulation()
print('print 5 page per one sencod, average waiting time is %f' % p.simulate(5))
print('print 10 page per one sencod, average waiting time is %f5.2' % p.simulate(10))
