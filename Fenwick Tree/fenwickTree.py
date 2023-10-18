# Every function is 0-indexed
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

# if it has negative numbers, transform it
# n = max(nums) - min(nums)
# each num is used as -> num - min(nums)