counter = 1
while counter <= 5:
    print("Hello world")
    counter = counter + 1

for item in [1, 2, 3, 4, 5]:
    print(item)

for item in range(5):
    print(item)

wordlist = ['cat', 'dog', 'rabbit']
letterlist = []
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)
print(letterlist)

import math
n = 4
if n < 0:
    print("Sorry, n %+10d is nagative" %n)
else:
    print(math.sqrt(n))

score = 89
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")

sqlist = [x * x for x in range(1, 11)] 
sqlist

sqlist = [x * x for x in range(1, 11) if x%2 != 0]
sqlist
