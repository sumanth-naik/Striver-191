# Key Idea: This is an optimization on top of DP. Think LIS when DP qn needs length of ordered output

import bisect
class Solution:
    def lengthOfLIS(self, nums) -> int:
        lisArr = []
        for num in nums:
            index = bisect.bisect_left(lisArr, num)
            if index==len(lisArr): lisArr.append(num)
            else: lisArr[index] = num
        return len(lisArr)
