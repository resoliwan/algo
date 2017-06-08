def dpMakeChange(coins, change, minCoins):
    for cent in range(change+1):
        coinCounts = cent
        for j in [c for c in coins if c <= cents]:
            if minCoins[cent-j] + 1 < coinConut:
                coinCount = minCoins[cent-j] + 1

        minCoins[cent] = coinCount
    return minCoins[cent]
