def maxIceCream(costs, coins):
    costs.sort()
    numIceCreams = 0
    for cost in costs:
        if cost<=coins:
            coins-=cost
            numIceCreams += 1
        else:
            break
    return numIceCreams