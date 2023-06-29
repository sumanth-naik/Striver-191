class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def bisectLeft():
            low, high = 0, n
            while low<high:
                mid = (low+high)//2
                if nums[mid]<target:
                    low = mid + 1
                else:
                    high = mid
            return low
        
        def bisectRight():
            low, high = 0, n
            while low<high:
                mid = (low+high)//2
                if nums[mid]<=target:
                    low = mid + 1
                else:
                    high = mid
            return low
        
        leftIndex = bisectLeft()
        return [-1,-1] if leftIndex==n or nums[leftIndex]!=target else [leftIndex, bisectRight()-1]
