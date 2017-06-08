def recMC(coins, value):
    if value in coins: 
        return 1
    minCnt = value
    for i in [c for c in coins if c < value]:
        cnt = 1 + recMC(coins, value - i)
        if cnt < minCnt:
            minCnt = cnt

    return minCnt


# print(recMc([1, 5], 10))

def recDC(coins, value, dic):
    if value in coins:
        return 1
    minCnt = value
    if dic[value] > 0:
        return dic[value]

    for i in [c for c in coins if c < value]:
        cnt = 1 + recDC(coins, value - i, dic)
        if cnt < minCnt:
            minCnt = cnt
            dic[value] = minCnt

    return minCnt


print(recDC([1, 5, 10, 21, 50], 63, [0]* 100))
