from copy import deepcopy
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        sortedSums, m, n = deepcopy(mat[-1]), len(mat), len(mat[0])
        for index in range(m-1, -1, -1):
            tempSortedSums = []
            for sortedSum in sortedSums:
                for num in mat[index]:
                    tempSortedSums.append(sortedSum+num)
            tempSortedSums.sort()
            sortedSums = tempSortedSums[:200]
        return sortedSums[k-1]
    
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        sortedSums = [0]
        for row in mat:
            sortedSums = sorted([x+y for x in sortedSums for y in row])[:k]
        return sortedSums[k-1]  


# BS on Answer
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])

        def countSubArraysWithSumLesserOrEqualToTargetSum(rowIndex, currentSum, targetSum):
            if currentSum>targetSum: return 0
            if rowIndex==m: return 1
            count = 0
            for columnIndex in range(n):
                subtreeCount = countSubArraysWithSumLesserOrEqualToTargetSum(rowIndex+1, currentSum+mat[rowIndex][columnIndex], targetSum) 
                if subtreeCount==0: break # Prune the search of next numbers in the current row
                count += subtreeCount
                if count>=k: break # Prune because in Binary Search we only care about count >= k and not the exact count
            return count
        
        low, high, smallestTargetSum = m, 5000*m, -1
        while low<=high:
            mid = (low+high)//2
            if countSubArraysWithSumLesserOrEqualToTargetSum(0, 0, mid)<k:
                low = mid + 1
            else:
                smallestTargetSum = mid
                high = mid - 1
        return smallestTargetSum
    
import heapq
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:

        def getKSmallestWithTwoArrays(arr1, arr2):
            m, n = len(arr1), len(arr2)
            minHeap, ansArr = [(arr1[0]+arr2[0], 0, 0)], []
            while minHeap and len(ansArr)<k:
                pairSum, arr1Index, arr2Index = heapq.heappop(minHeap)
                ansArr.append(pairSum)
                if arr2Index+1<n: heapq.heappush(minHeap, (arr1[arr1Index]+arr2[arr2Index+1], arr1Index, arr2Index+1))
                if arr2Index==0 and arr1Index+1<m: heapq.heappush(minHeap, (arr1[arr1Index+1]+arr2[arr2Index], arr1Index+1, arr2Index))
            return ansArr

        arr2 = [0]
        for arr1 in mat:
            arr2 = getKSmallestWithTwoArrays(arr1, arr2)
        return arr2[k-1]