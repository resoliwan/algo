def moveTower(height, fromPin, withPin, toPin):
    if height >= 1:
        moveTower(height - 1, fromPin, toPin, withPin)
        moveDisk(height - 1, fromPin, toPin)
        moveTower(height - 1, withPin, toPin, fromPin)

def moveDisk(height, fromPin, toPin):
    print('move pin {}, from {} to {}'.format(height, fromPin, toPin))

moveTower(3, 'A', 'B', 'C')
