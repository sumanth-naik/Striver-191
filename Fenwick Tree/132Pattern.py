from sortedcontainers import SortedList
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        sortedList, minima = SortedList(nums), nums[0]
        for mid in nums:
            sortedList.remove(mid)
            minima = min(minima, mid)
            if mid!=minima:
                index = bisect_left(sortedList, minima+1)
                if index!=len(sortedList) and sortedList[index]<mid: return True
        return False

    
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, secondLargest = [], -1e9
        for num in nums[::-1]:
            if stack and secondLargest>num: return True
            while stack and stack[-1]<num: secondLargest = stack.pop()
            stack.append(num)
        return False

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        
        minFromLeft = [nums[0]]
        for i in range(1, n):
            minFromLeft.append(min(minFromLeft[i-1], nums[i]))
        
        stack = [] 
        
        for j in range(n-1, -1, -1):
            if nums[j] > minFromLeft[j]:
                while stack and stack[-1] <= minFromLeft[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        
        return False


class BIT:
    def __init__(self, n):
        self.bitSize = n+1
        self.bit = defaultdict(int)

    def insert(self, index, val):
        index += 1
        while index<self.bitSize:
            self.bit[index] += val
            index += (index & -index)
    
    def getCountTill(self, index):
        total = 0
        index += 1
        while index>0:
            total += self.bit[index]
            index -= (index & -index)
        return total

    def rangeSum(self, left, right):
        return self.getCountTill(right)-self.getCountTill(left-1)


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minNum, maxNum = min(nums), max(nums)
        bit = BIT(maxNum-minNum+1)
        for num in nums:
            bit.insert(num-minNum, 1)

        minToLeft = nums[0]-minNum
        for num in nums:
            bit.insert(num-minNum, -1)
            minToLeft = min(minToLeft, num-minNum)
            if minToLeft<num-minNum and bit.rangeSum(minToLeft+1, num-minNum-1)>0: return True
        return False

