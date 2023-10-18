class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i, num in enumerate([nums[-(k%len(nums))+index] for index in range(len(nums))]):
            nums[i] = num    

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(startIndex, endIndex):
            for diff in range((endIndex-startIndex)//2 + 1):
                nums[startIndex+diff], nums[endIndex-diff] = nums[endIndex-diff], nums[startIndex+diff]
        n = len(nums)
        k %= n
        reverse(0, n-k-1)
        reverse(n-k, n-1)
        reverse(0, n-1)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        numSwaps, n, startIndex = 0, len(nums), 0
        # This is needed to not run the same loop twice. Loops are always crossing and never disjoint.
        while numSwaps<n:
            currentIndex, currentIndexVal = startIndex, nums[startIndex]
            while True:
                nextIndex = (currentIndex + k)%n
                currentIndex, currentIndexVal, nums[nextIndex] = nextIndex, nums[nextIndex], currentIndexVal
                numSwaps += 1
                if currentIndex==startIndex: break
            startIndex += 1
        
