class Solution:
    def shipWithinDays(self, weights, days):
        left, right = max(weights), len(weights)
        minWeightCapacity = right
        while left<=right:
            mid = (left+right)//2
            dayCount, currWeightSum = 1, 0
            for weight in weights:
                if weight + currWeightSum > mid:
                    dayCount += 1
                    if dayCount==days+1:
                        break
                    currWeightSum = 0
                currWeightSum += weight
            if dayCount<=days:   
                minWeightCapacity = min(minWeightCapacity, mid)
                right = mid - 1
            else:
                left = mid + 1
        return minWeightCapacity