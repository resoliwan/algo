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
        if self.pinA is None:
            return int(input("Enter PinA input for gate"
                             + self.getLabel() + "-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB is None:
            return int(input("Enter PinB input for gate" 
                             + self.getLabel() + "-->"))
        else: 
            return self.pinB.getFrom().getOutput()
    
    def setNextPin(self, source):
        if self.pinA is None:
            self.pinA = source
        elif self.pinB is None:
            self.pinB = source
        else:
            raise RuntimeError("All pins is already seted")


class UnaryGate(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pin = None

    def setPin(self, pin):
        self.pin = pin

    def getPin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate" 
                             + self.getLabel() + "-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError("All pin is already seted")


class AndGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def performGateLogic(self):
        if self.getPinA() == 1 and self.getPinB() == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def performGateLogic(self):
        if self.getPinA() == 0 and self.getPinB() == 0:
            return 0
        else: 
            return 1


class NotGate(UnaryGate):
    def __init__(self, label):
        UnaryGate.__init__(self, label)

    def performGateLogic(self):
        if self.getPin() == 0:
            return 1
        else:
            return 0


class Connector:
    def __init__(self, fromGate, toGate):
        self.fromGate = fromGate
        self.toGate = toGate
        
        toGate.setNextPin(self)

    def getFrom(self):
        return self.fromGate

    def getTo(self):
        return self.toGate


g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G2")
g4 = NotGate("G3")

c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)
