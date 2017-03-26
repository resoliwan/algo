"""Fibonacci numbers module"""


def fin(n):
    # return finbonacci series up to n
    a, b = 0, 1
    result = []
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

if __name__ == '__main__':
    import sys
    print(fin(int(sys.argv[1])))
        
