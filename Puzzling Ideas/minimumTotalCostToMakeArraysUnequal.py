from collections import Counter

class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        counter1, counter2 = Counter(nums1), Counter(nums2)
        if len(counter1)==1 or len(counter2)==1 or max(counter2.values())>len(nums2)//2:
            return -1
        costSoFar, index1, n = 0, 0, len(nums1)
        index2List = [i for i in range(n) if nums1[i]==nums2[i]]
        while index1<n:
            if nums1[index1]==nums2[index1]:
                for index2 in index2List:
                    if index1==index2 or nums1[index1]==nums1[index2] or nums2[index2]==nums1[index1]: 
                        index2 += 1
                        continue
                    nums1[index1], nums1[index2] = nums1[index2], nums1[index1]
                    costSoFar += (index1 + index2)
                    break
            index1 += 1
        return costSoFar
        


class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:

        valToFreqMap, totalCount, totalCost, n = defaultdict(int), 0, 0, len(nums1)
        for index in range(n):
            if nums1[index]==nums2[index]:
                valToFreqMap[nums1[index]] += 1
                totalCount += 1
                totalCost += index
        
        # maxFreqVal, maxFreqCount = -1, -1
        # for val, freq in valToFreqMap.items():
        #     if freq>maxFreqVal:
        #         maxFreqVal, maxFreqCount = val, freq
        
        maxFreqVal, maxFreqCount = max(valToFreqMap.items(), key=lambda x:x[1], default=(0,0))

        extraNeeded = 2*maxFreqCount - totalCount
        if extraNeeded<=0: return totalCost

        for index in range(n):
            if nums1[index]!=nums2[index] and nums1[index]!=maxFreqVal and nums2[index]!=maxFreqVal:
                extraNeeded-=1
                totalCost += index
            if extraNeeded==0: return totalCost

        return -1
        
