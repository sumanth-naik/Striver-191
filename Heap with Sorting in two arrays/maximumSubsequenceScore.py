class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        maxScoreSeen, sumOfKNums, minHeap = 0, 0, []
        for num1, num2 in sorted(list(zip(nums1, nums2)), key=lambda x:-x[1]):
            sumOfKNums += num1
            heappush(minHeap, num1)
            if len(minHeap)==k:
                maxScoreSeen = max(maxScoreSeen, sumOfKNums*num2)
                sumOfKNums -= heappop(minHeap)
        return maxScoreSeen
    
from sortedcontainers import SortedList
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        sortedArr = sorted((nums2[i], nums1[i]) for i in range(len(nums1)))
        sortedList = SortedList(nums1)
        sumOfKNums = sum(sortedList[len(sortedList)-k:])
        maxScoreSeen = 0

        for num2, num1 in sortedArr:
            maxScoreSeen = max(maxScoreSeen, sumOfKNums*num2)
            indexOfNum1 = bisect_left(sortedList, num1)
            sortedList.remove(num1)
            if len(sortedList)<k:
                break
            if indexOfNum1>len(sortedList)-k:
                sumOfKNums -= num1
                sumOfKNums += sortedList[len(sortedList)-k]
        return maxScoreSeen
