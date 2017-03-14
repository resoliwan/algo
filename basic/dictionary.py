import timeit
import random


for i in range(10000, 100001, 20000):
    t = timeit.Timer("random.randrange(%d) in x" % i,
                     setup="from __main__ import x, random")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("size: %d, list: %5.2f, dic: %5.2f" % (i, lst_time, d_time))
