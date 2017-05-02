

def listSum(numbers):
    theSum = 0
    for number in numbers:
        theSum = theSum + number
    return theSum


print(listSum([1, 3, 5, 7, 9]))


def listSum2(numbers):
    if len(numbers) < 2:
        return numbers[0]
    else:
        return numbers[0] + listSum2(numbers[1:])


print(listSum2([1, 3, 5, 7, 9]))


def convertToStr(dividend, divisor):
    if dividend < divisor:
        return str(dividend)
    else:
        return convertToStr(dividend//divisor, divisor) + '' + str(dividend % divisor)


print(convertToStr(10, 2))


def toStr(n, base):
    if n < base:
        return str(n)
    else:
        return toStr(n//base, base) + str(n % base)


print(toStr(10, 2))



