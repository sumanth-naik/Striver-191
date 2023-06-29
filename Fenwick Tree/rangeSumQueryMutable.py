from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.fenwickTreeArr = [0 for _ in range(len(nums)+1)]
        self.nums = nums
        for index, num in enumerate(nums):
            self.updateFenwickTree(index+1, num)

    def updateFenwickTree(self, index, diff):
        while index<len(self.fenwickTreeArr):
            self.fenwickTreeArr[index] += diff
            index += (index & (-index))

    def update(self, index: int, val: int) -> None:
        self.updateFenwickTree(index+1, val - self.nums[index])
        self.nums[index] = val

    def sumFromFenwickTree(self, index):
        total = 0
        while index>0:
            total += self.fenwickTreeArr[index]
            index -= (index & (-index))
        return total
    
    def sumRange(self, left: int, right: int) -> int:
        return self.sumFromFenwickTree(right+1) - self.sumFromFenwickTree(left)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


    
# 1 indexing
class BIT:
    def __init__(self, n) -> None:
        self.bit = [0 for _ in range(n+1)]

    def addValue(self, index, value):
        while index<len(self.bit):
            self.bit[index] += value
            index += (index & (-index))

    def getSum(self, index):
        total = 0
        while index>0:
            total += self.bit[index]
            index -= (index & (-index))
        return total
    
    # inclusive
    def getSumInRange(self, left, right):
        return self.getSum(right) - self.getSum(left-1)
    
class NumArray:

    def __init__(self, nums: List[int]):
        self.bit = BIT(len(nums))
        for index, num in enumerate(nums):
            self.bit.addValue(index+1, num)
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        self.bit.addValue(index+1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.bit.getSumInRange(left+1, right+1)



class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0 for _ in range(4*self.n)]
        self.buildTree(nums, 0, 0, len(nums)-1)

    def buildTree(self, nums, nodeIndex, left, right):
        if left==right:
            self.tree[nodeIndex] = nums[left]
            return
        mid = (left+right)//2
        self.buildTree(nums, 2*nodeIndex+1, left, mid)
        self.buildTree(nums, 2*nodeIndex+2, mid+1, right)
        self.tree[nodeIndex] = self.tree[2*nodeIndex+1] + self.tree[2*nodeIndex+2]
    
    def query(self, nodeIndex, left, right, queryLeft, queryRight):
        if right<queryLeft or queryRight<left:
            return 0
        if queryLeft<=left and right<=queryRight:
            return self.tree[nodeIndex]
        mid = (left+right)//2
        return self.query(2*nodeIndex+1, left, mid, queryLeft, queryRight) + self.query(2*nodeIndex+2, mid+1, right, queryLeft, queryRight)

    # left, right are wrt nums
    def update(self, nodeIndex, left, right, numsIndex, val):
        if numsIndex<left or right<numsIndex:
            return
        if left==right==numsIndex:
            self.tree[nodeIndex] = val
            return
        mid = (left+right)//2
        if numsIndex<=mid:
            self.update(2*nodeIndex+1, left, mid, numsIndex, val)
        else:
            self.update(2*nodeIndex+2, mid+1, right, numsIndex, val)
        self.tree[nodeIndex] = self.tree[2*nodeIndex+1] + self.tree[2*nodeIndex+2]


class NumArray:

    def __init__(self, nums: List[int]):
        self.segmentTree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.segmentTree.update(0, 0, self.segmentTree.n -1, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.segmentTree.query(0, 0, self.segmentTree.n-1, left, right)
