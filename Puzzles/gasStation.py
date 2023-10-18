class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas, currGas, startIndex, n = 0, 0, 0, len(gas)
        for index in range(n):
            totalGas += (gas[index]-cost[index])
            currGas += (gas[index]-cost[index])
            if currGas<0:
                currGas, startIndex = 0, index+1
        return startIndex if totalGas>=0 else -1
