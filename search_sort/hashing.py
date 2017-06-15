# def hash(aString, tableSize):
#     return sum([ord(x) for x in list(aString)]) % tableSize

# print(hash('hello', 3))
# print(hash('hello1', 3))
# print(hash('hello2', 3))

class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size

    def put(self, key, value):
        hashValue =  self.hash(key)
        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = value
        else:
            if self.slots[hashValue] == key:
                self.data[hashValue] = value #replace
            else:
                nextSlot = self.reHash(hashValue)
                while self.slots[nextSlot] != None and key != self.slots[nextSlot]:
                    nextSlot = self.reHash(nextSlot)

                if self.slots[nextSlot] == None:
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = value
                else:
                    self.data[nextSlot] = value #replace


    def hash(self, key):
        return sum([ord(ch) for ch in list(key)]) % self.size

    def reHash(self, oldHash):
        return (oldHash + 1) % self.size

    def printInfo(self):
        print(self.slots)
        print(self.data)
    
m = HashTable(3)
print(m.put('2', 2))
print(m.printInfo())
print(m.put('4', 4))
print(m.printInfo())
print(m.put('8', 8))
print(m.printInfo())

# print(m.put('10', 10))
# print(m.printInfo())
