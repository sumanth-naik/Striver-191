class BIT:
    def __init__(self, n):
        self.bitSize = n+1
        self.bit = defaultdict(int)

    def insert(self, index):
        index += 1
        while index<self.bitSize:
            self.bit[index] += 1
            index += (index & -index)
    
    def getCountTill(self, index):
        total = 0
        index += 1
        while index>0:
            total += self.bit[index]
            index -= (index & -index)
        return total


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums, numPairs = [num1-num2 for num1, num2 in zip(nums1, nums2)], 0
        minNum, maxNum = min(nums), max(nums)
        bit = BIT(max(maxNum-minNum, maxNum-minNum+diff))
        for num in nums:
            if num-minNum+diff>=0:
                numPairs += (bit.getCountTill(num-minNum+diff))
            bit.insert(num-minNum)
        return numPairs
    


from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        sortedList, nums, count = SortedList(), [num1-num2 for num1, num2 in zip(nums1, nums2)], 0
        for num in nums:
            count += bisect_right(sortedList, num+diff)
            sortedList.add(num)
        return count



        