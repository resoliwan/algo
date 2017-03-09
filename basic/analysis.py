import time


def sumOfN(num):
    start = time.time()
    theSum = 0
    for i in range(1, num+1):
        theSum = theSum + i

    end = time.time()
    return theSum, end-start


for i in range(5):
    print("Sum is %d required %10.7f seconds" % sumOfN(10000))


def sumOfN3(num):
    start = time.time()
    theSum = (num*(num+1))/2
    end = time.time()
    return theSum, end-start


for i in range(5):
    print("Sum is %d requiered %10.7f seconds" % sumOfN3(10000))


def minmum2(source):
    result = source[0]
    for i in source:
        for k in source:
            # print(i, k)
            if i >= k and result >= k:
                result = k
            elif result >= i:
                result = i
    return result


minmum2([1, 2, 3, 4])


def minmum1(source):
    result = source[0]
    for i in source:
        if result > i:
            result = i
    return result


minmum1([1, 2, 3, 4, -1, 9])
 
