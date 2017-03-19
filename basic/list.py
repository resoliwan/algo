import timeit


def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


print("concat %5.5f seconds" % timeit.timeit("test1()", setup="from __main__ import test1", number=1000))
print("append %5.5f seconds" % timeit.timeit("test2()", setup="from __main__ import test2", number=1000))
print("comprehension %5.5f secondes" % timeit.timeit("test3()", setup="from __main__ import test3", number=1000))
print("range %5.5f seconds" % timeit.timeit("test4()", setup="from __main__ import test4", number=1000))


def empty1():
  l = 1


print("empty %5.5f seconds" % timeit.timeit("empty1()", setup="from __main__ import empty1", number=1000))


