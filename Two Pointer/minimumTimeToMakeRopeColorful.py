   
class Solution:
    def minCost(self, colors: str, neededTime):
        i, j, n, totalTime = 0, 0, len(colors), 0
    
        while i<n:
            maxInRange = sumInRange = neededTime[i]
            while j+1<n and colors[i]==colors[j+1]: 
                j+=1
                maxInRange = max(maxInRange, neededTime[j])
                sumInRange += neededTime[j]
            totalTime += (sumInRange - maxInRange)
            i = j = j+1

        return totalTime
