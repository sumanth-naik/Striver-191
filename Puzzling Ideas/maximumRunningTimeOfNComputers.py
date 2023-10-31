from bisect import bisect_right
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        batteries.sort(key=lambda x:-x)
        totalExtraBatteryLeft = sum(batteries[n:])

        prefixSumArr = [0]
        for battery in batteries[:n]:
            prefixSumArr.append(prefixSumArr[-1] + battery)

        def isPossible(target):
            numBatteriesGreaterOrEqualToTarget = bisect_right(batteries, -target, 0, n, key=lambda x:-x)
            totalExtraBatteryRequired = (n-numBatteriesGreaterOrEqualToTarget)*target - (prefixSumArr[n] - prefixSumArr[numBatteriesGreaterOrEqualToTarget])
            return totalExtraBatteryRequired<=totalExtraBatteryLeft

        low, high = 1, sum(batteries)//n 
        while low<high:
            mid = (low+high+1)//2
            if isPossible(mid): low = mid
            else: high = mid - 1
        return low
    
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:

        batteries.sort()
        sumOfConsideredBatteries = sum(batteries)
        # Any battery more than avg(wrt n and not len(batteries)) will be wasting battery in the end
        # Keep removing such batteries
        while batteries[-1]>sumOfConsideredBatteries/n:
            # n will never get to 0 as avg in worst case will be batteries[0]
            n -= 1
            sumOfConsideredBatteries -= batteries.pop()
        # None of the battery juice will get wasted from this point
        return sumOfConsideredBatteries//n