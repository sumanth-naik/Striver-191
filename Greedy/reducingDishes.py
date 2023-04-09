class Solution:
    def maxSatisfaction(self, satisfaction):
        satisfaction.sort()
        cumulativeSum, i = 0, len(satisfaction)
        while i>0:
            if cumulativeSum+satisfaction[i-1]>=0: 
                i-=1
                cumulativeSum+=satisfaction[i]
            else: break
        return sum(mult*satisfaction[i+mult-1] for mult in range(1, len(satisfaction)-i+1))
        
    def maxSatisfaction(self, satisfaction):
        res = total = 0
        satisfaction.sort()
        while satisfaction and satisfaction[-1] + total > 0:
            total += satisfaction.pop()
            res += total
        return res