"""logic Gate"""


class LogicGate:
    """LogicGate"""
    def __init__(self, label):
        self.label = label
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

    def performGateLogic(self):
        return


class BinaryGate(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)

        self.pinA = None
        self.pinB = None
    
    def setPins(self, pinA, pinB):
        self.pinA = pinA
        self.pinB = pinB

    def getPinA(self):
        # return input("Enter PinA input for gate " + self.getLabel() + "--->")
        return self.pinA

    def getPinB(self):
        # return input("Enter PinB input for gate " + self.getLabel() + "--->")
        return self.pinB


class UnaryGate(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pin = None

    def setPin(self, pin):
        self.pin = pin

    def getPin(self):
        # self.pin =
        # int(input("Enter Pin input for gate " + self.getLabel() + "--->"))
        return self.pin
