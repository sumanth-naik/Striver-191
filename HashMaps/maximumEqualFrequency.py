from collections import defaultdict
from typing import List
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        numToCountMap = {}
        countToNumsMap = defaultdict(set)
        maxFreq = 1
        for index, num in enumerate(nums):
            if num in numToCountMap:
                countToNumsMap[numToCountMap[num]].remove(num)
                numToCountMap[num] += 1
            else:
                numToCountMap[num] = 1
            countToNumsMap[numToCountMap[num]].add(num)

            if len(countToNumsMap[numToCountMap[num]-1])==0:
                del countToNumsMap[numToCountMap[num]-1]

            if len(countToNumsMap)==2:
                if 1 in countToNumsMap and len(countToNumsMap[1])==1:
                    maxFreq = max(maxFreq, index+1)
                else:
                    keys = sorted(countToNumsMap.keys())
                    if keys[1]-keys[0]==1 and len(countToNumsMap[keys[1]])==1:
                        maxFreq = max(maxFreq, index + 1)
            if len(countToNumsMap)==1:
                if 1 in countToNumsMap or len(countToNumsMap[numToCountMap[num]])==1:
                    maxFreq = max(maxFreq, index + 1)

        return maxFreq

