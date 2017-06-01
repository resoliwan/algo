def findSmallestCoinSet(target, coins):
    result = _findSmallestCoinSet(target, coins)

    if len(coins) <= 1:
        return result
    
    for i in range(len(coins)):
        tempResult = findSmallestCoinSet(target, coins[:i] + coins[i+1:])
        if tempResult['cnt'] < result['cnt']:
            result = tempResult
        elif tempResult['cnt'] == result['cnt']:
            result['solution'] = result['solution'] + tempResult['solution']

    return result


def _findSmallestCoinSet(target, coins):
    resultSet = set()
    remainder = 0 
    for i in range(len(coins)-1, -1, -1):
        divisor = coins[i]
        quotient = target // divisor
        if quotient != 0:
            target = target % divisor
            resultSet.add((divisor, quotient))
    

    if target != 0:
        return {'cnt': 999, 'solution': []}
    else:
        return {'cnt': sum([ x for _, x in resultSet]), 'solution': [resultSet]} 

    



target = 63 
coins = [1, 5, 10, 21, 25]
print('main', findSmallestCoinSet(target, coins))
