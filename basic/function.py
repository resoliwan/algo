def square(n):
    return n**2

print(square(2))

def squareroot(n):
    root = n/2;
    for i in range(0, 100):
        root = 1/2 * (root + n/root)
    return root 

squareroot(4)
        
