class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        def getMoves(target):
            return sum(abs(num-target) for num in nums)
        
        low, high, minMoves = min(nums), max(nums), 1e20
        while low<high:
            mid = (low+high)//2
            midMoves, nextMoves = getMoves(mid), getMoves(mid+1)
            minMoves = min(minMoves, midMoves, nextMoves)
            if midMoves<=nextMoves:
                high = mid
            else:
                low = mid + 1
        return minMoves if minMoves!=1e20 else 0


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n, k = len(nums), len(nums)//2
        return sum(abs(num-nums[k]) for num in nums)


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        def getKthElement(arr, k): # k is 1 indexed
            if not 1<=k<=len(arr): raise Exception("invalid k") 
            low, pivot = 0, len(arr)-1
            while low<=pivot:
                swap = low
                for index in range(low, pivot):
                    if arr[index]<arr[pivot]:
                        arr[swap], arr[index] = arr[index], arr[swap]
                        swap += 1
                arr[swap], arr[pivot] = arr[pivot], arr[swap]

                numsSmallerOrEqualToPivot = swap - low + 1
                if numsSmallerOrEqualToPivot==k:
                    return arr[swap]
                elif numsSmallerOrEqualToPivot<k:
                    k -= numsSmallerOrEqualToPivot
                    low = swap + 1
                else:
                    pivot = swap - 1

        median = getKthElement(nums, (len(nums)//2)+1)
        return sum(abs(num-median) for num in nums)