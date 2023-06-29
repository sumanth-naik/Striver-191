
class BIT:
    def __init__(self, n):
        self.bitSize = n+1
        self.bit = [0 for _ in range(self.bitSize)]
    
    def add(self, index):
        index += 1
        while index<self.bitSize:
            self.bit[index] += 1
            index += (index & -index)

    def sumTill(self, index):
        total = 0
        while index>0:
            total += self.bit[index]
            index -= (index & -index)
        return total
    
    def getSumInRange(self, left, right):
        return self.sumTill(right+1) - self.sumTill(left)
    

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        bit, sortedIndices, ansArr = BIT(n), sorted(range(n), key=lambda index:nums[index]), [0 for _ in range(n)]
        for index in sortedIndices:
            ansArr[index] = bit.getSumInRange(index, n-1)
            bit.add(index)
        return ansArr

        


# Merge sort 27min
from copy import deepcopy
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        arr, inversionsArr = [(val, index) for index, val in enumerate(nums)], [0 for _ in range(len(nums))]

        def merge(left, mid, right):
            nonlocal arr, inversionsArr
            i, j, tempArr = left, mid+1, []
            inversionsArrHelper, inversionsArrIndex = [0 for _ in range(right-left+1)], 0 

            while i<=mid and j<=right:
                if arr[i][0]<=arr[j][0]: 
                    tempArr.append(arr[i])
                    i += 1
                    inversionsArrIndex += 1
                else:
                    tempArr.append(arr[j])
                    j += 1
                    inversionsArrHelper[inversionsArrIndex] += 1
            tempArr.extend(arr[i:mid+1] + arr[j:right+1])

            cumulativeInversions, inversionsArrIndex = 0, 0
            for (_, index), inversionVal in zip(arr[left:mid+1], inversionsArrHelper):
                cumulativeInversions += inversionVal
                inversionsArr[index] += cumulativeInversions
            
            for i in range(left, right+1):
                arr[i] = tempArr[i-left]

        def mergeSort(left, right):
            if left==right: return
            mid = (left+right)//2
            mergeSort(left, mid)
            mergeSort(mid+1, right)
            merge(left, mid, right)

        mergeSort(0, len(arr)-1)
        return inversionsArr