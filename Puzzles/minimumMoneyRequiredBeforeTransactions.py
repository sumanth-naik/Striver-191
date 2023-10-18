class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
       
        def compare(x, y):
            cost1, cashback1 = x
            cost2, cashback2 = y
            oneTwo = max(cost1, cost1+cost2-cashback1)
            twoOne = max(cost2, cost2+cost1-cashback2)
            if oneTwo>twoOne: return -1
            elif oneTwo<twoOne: return 1
            else: return -1 if cost1>cost2 else 1
        
        transactions.sort(key=cmp_to_key(compare))
        
        minMoneySeen, currMoney = 1e9, 0
        for cost, cashback in transactions:
            currMoney -= cost
            minMoneySeen = min(minMoneySeen, currMoney)
            currMoney += cashback
        return -minMoneySeen


class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        moneySpent, maxCashbackDuringLoss, maxCostDuringGain = 0, 0, 0
        for cost, cashback in transactions:
            if cost>cashback:
               moneySpent += (cost - cashback)
               maxCashbackDuringLoss = max(maxCashbackDuringLoss, cashback)
            else:
                maxCostDuringGain = max(maxCostDuringGain, cost)
        # Worst case will be like, 
        # [loss, loss, lossWithMostCashback, mostProfit, profit] or 
        # [loss, loss, mostProfit, profit, lossWithMostCashback]
        # in other words
        # [t1, t2, t of maxCashbackDuringLoss, t of maxCostDuringGain, t3] or 
        # [t1, t2, t of maxCostDuringGain, t3, t of maxCashbackDuringLoss]
        return moneySpent + max(maxCashbackDuringLoss, maxCostDuringGain)


class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        return sum(max(0, cost-cashback) for cost, cashback in transactions) + max(map(min, transactions))