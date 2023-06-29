def countReversePairs(low, mid, high, arr, ans):
    i = low
    j = mid + 1    
    for i in range(low, mid + 1):
        while(j <= high and arr[i] > 2 * arr[j]):
            j = j + 1
        ans[0] = ans[0] + (j - (mid + 1))

def merge(low, mid, high, arr, temp):
    i = low
    j = mid + 1
    k = low
    while(i <= mid and j <= high):
        if(arr[i]<=arr[j]):
            temp[k] = arr[i]
            k = k + 1
            i = i + 1
        else:
            temp[k] = arr[j]
            k = k + 1
            j = j + 1
            
    while(i <= mid):
        temp[k] = arr[i]
        k = k + 1
        i = i + 1
        
    while(j <= high):
        temp[k] = arr[j]
        k = k + 1
        j = j + 1
        
    for x in range(low, high + 1):
        arr[x] = temp[x]


def mergeSortHelper(low, high, arr, temp, ans):
    if(low == high):
        return arr, ans
    
    mid = (low + high)//2
    
    mergeSortHelper(low, mid, arr, temp, ans)
    mergeSortHelper(mid + 1, high, arr, temp, ans)
    
    countReversePairs(low, mid, high, arr, ans)
    merge(low, mid, high, arr, temp)
    
    return arr, ans

def mergeSort(arr):
    temp = [None] * len(arr)
    return mergeSortHelper(0,len(arr)-1, arr, temp, [0])
    
    



import bisect
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        numInversePairs = 0

        def merge(left, mid, right):
            nonlocal nums, numInversePairs
            i, j, tempArr = left, mid + 1, []

            low, high = i, mid+1
            for num in nums[j:right+1]:
                index = bisect.bisect_left(nums, 2*num+1, low, high)
                if index==high: break
                numInversePairs += (high-index)
                low = index

            while i<=mid and j<=right:
                if nums[i]<=nums[j]:
                    tempArr.append(nums[i])
                    i += 1
                else:
                    tempArr.append(nums[j])
                    j += 1

            tempArr.extend(nums[i:mid+1] + nums[j:right+1])

            for index in range(left, right+1):
                nums[index] = tempArr[index-left]

        def mergeSort(left, right):
            if left==right: return
            mid = (left+right)//2
            mergeSort(left, mid)
            mergeSort(mid+1, right)
            merge(left, mid, right)
            
        mergeSort(0, len(nums)-1)
        return numInversePairs



class BIT:
    def __init__(self, n):
        self.bitSize = n+1
        self.bit = [0 for _ in range(n+1)]

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
    
    def sumInRange(self, left, right):
        return self.sumTill(right+1) - self.sumTill(left)
    

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        bit, reversePairsCount, n = BIT(len(nums)), 0, len(nums)
        sortedNumsAndIndices, leftPointer = sorted((num, index) for index, num in enumerate(nums)), 0
        for num, index in sortedNumsAndIndices:
            while leftPointer<n and num>2*sortedNumsAndIndices[leftPointer][0]:
                bit.add(sortedNumsAndIndices[leftPointer][1])
                leftPointer += 1
            reversePairsCount += (bit.sumInRange(index+1, n-1)) # index+1 needed for negative numbers
        return reversePairsCount

from sortedcontainers import SortedList
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sortedList, reversePairsCount = SortedList(), 0
        for num in nums:
            index = bisect.bisect_right(sortedList, num*2)
            reversePairsCount += (len(sortedList)-index)
            sortedList.add(num)
        return reversePairsCount
    


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def divideAndConquerWithSort(left, right):
            if left==right: return 0
            
            mid = (left+right)//2
            count = divideAndConquerWithSort(left, mid) + divideAndConquerWithSort(mid+1, right)

            start, end = left, mid+1
            for num in nums[mid+1:right+1]:
                start = bisect.bisect_right(nums, 2*num, start, end)
                count += (end-start)

            nums[left:right+1] = sorted(nums[left:right+1])
            return count

        return divideAndConquerWithSort(0, len(nums)-1)