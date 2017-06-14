def hash(aString, tableSize):
    return sum([ord(x) for x in list(aString)]) % tableSize

print(hash('hello', 3))
# print(hash('hello1', 3))
# print(hash('hello2', 3))

