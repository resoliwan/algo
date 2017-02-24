"""moneky"""


import string
import random


def choice_from_strings():
    """return random string with a-Z and include space"""
    return random.choice(string.ascii_letters + " ")


def choices_from_strings(number_of_string):
    """return random strings"""
    return [choice_from_strings() for x in range(0, number_of_string)]


def score(compare, target):
    """Calculate Score of function"""
    return sum([1 for x, y in zip(target, compare) if x == y])/len(target)*100


choices_from_strings(28)
# target = list("methinks it is like a weasel")
target = list("abcd")
i = 0
bestString = ""
bestScore = 0

while i < 100000:
    generated = choices_from_strings(4)
    if i%1000==0:
        print("score %f" %(bestScore))
        print("compare %s target%s" %(generated, target))
    currentScore = score(generated, target)
    if bestScore < currentScore:
        bestScore = generated
        bestScore = currentScore
    i = i+1


