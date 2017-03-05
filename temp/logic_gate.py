"""Logic Gate"""


class LogicGate:
    def __init__(self, label):
        self.label = label

    def getLabel(self):
        return self.label

    def getOutput(self):
        return self.performGateLogic()
    
    def performGateLogic(self):
        return None


class UnaryGate(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pin = None

    def getPin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate:" 
                             + self.getLabel() + "-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError("Error: No Empty pin at gate:" 
                               + self.getLabel())


class BinaryGate(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA is None:
            return int(input("Enter PinA input for gate:"
                             + self.getLabel() + "-->"))
        else:
            return self.pinA.getFrom().getOutput()
    
    def getPinB(self):
        if self.pinB is None:
            return int(input("Enter PinB input for gate:"
                             + self.getLabel() + "-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA is None:
            self.pinA = source
        elif self.pinB is None:
            self.pinB = source
        else:
            raise RuntimeError("Error: No Empty pins at gate:"
                               + self.getLabel())


class AndGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 0 and b == 0:
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


class NorGate(OrGate):
    def __init__(self, label):
        OrGate.__init__(self, label)

    def performGateLogic(self):
        a = super(NorGate, self).performGateLogic()
        if a == 0:
            return 1
        else:
            return 0


class NandGate(AndGate):
    def __init__(self, label):
        AndGate.__init__(self, label)

    def performGateLogic(self):
        a = super(NandGate, self).performGateLogic()
        if a == 0:
            return 1
        else:
            return 0


class Connectoer:
    def __init__(self, fgate, tgate):
        self.fgate = fgate
        self.tgate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fgate

    def getTo(self):
        return self.tgate


def main():
    g1 = AndGate("G1AND")
    g2 = AndGate("G2AND")
    g3 = OrGate("G3OR")
    g4 = NotGate("G4NOT")

    Connectoer(g1, g3)
    Connectoer(g2, g3)
    Connectoer(g3, g4)
    print(g4.getOutput())

    g5 = NorGate("G5NOR")
    g5.getOutput()

    g6 = NandGate("G6NAND")
    print(g6.getOutput())

    g7 = NorGate("G7NOR")
    g8 = NorGate("G8NOR")
    g9 = AndGate("G9AND")
    Connectoer(g7, g9)
    Connectoer(g8, g9)
    print(g9.getOutput())


main()
