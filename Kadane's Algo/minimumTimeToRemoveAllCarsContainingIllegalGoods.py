'''
ref: https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/solutions/1748424/python-maximum-sum-on-subarray-explained/
len(left) + 2* count(middle, 1) + len(right) = len(left) + len(middle) + len(right) + 2*count(middle, 1) - len(middle) = n + count(middle, 1) - count(middle, 0).

So, in fact what we need to found is the subarray with the smallest count(middle, 1) - count(middle, 0) value. If we now replace all 0 with -1, it is the same as found the subarray with the smallest sum! 
'''

class Solution:
    def minimumTime(self, s: str) -> int:
        runningSum, minSum = 0, 0 #init minSum to 0, as in a case with all ones, we dont have middle
        for num in s:
            runningSum += 2*int(num)-1
            minSum = min(runningSum, minSum)
            runningSum = min(runningSum, 0)
        return len(s) + minSum

# ref: https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/solutions/1748704/java-c-python-short-one-pass-o-1-space/ 
class Solution:
    def minimumTime(self, s: str) -> int:
        left, res = 0, len(s)
        for index, num in enumerate(s):
            left = min(left + (num=='1')*2, index+1) # min(pop left ones and greedily pop middle ones, pop everything)
            res = min(res, left + (len(s)-1-index)) # left stores best way to pop till index, hypthetical right will be min at (n-1-index).
            # And it is guranteed that at some index this case will happen
        return res