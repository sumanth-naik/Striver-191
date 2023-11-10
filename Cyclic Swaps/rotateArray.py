# Key Idea 1: Each Cycle is independent. 
# Key Idea 2: Each Cycle starts at 'start' and ends when (start + someJumps*k)%n==start
#             => (someJumps * k) % n = 0      
#             => someJumps = n/gcd(n,k)    ----> Each cycle will deal with these many numbers
# Key Idea 3: There will be gcd(n, k) cycles [n/someJumps]

# Note: We need someJumps - 1 swaps. Each swap will be with start index only. 
#       In fact, someJump'th swap will be a self swap

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k==0: return
        n = len(nums)
        numCycles = gcd(n, k)
        for start in range(numCycles):
            for index in range(start, (n*k)//numCycles, k): # Note
                nums[index%n], nums[start] = nums[start], nums[index%n]




# Key Idea: reverse each part once and reverse the whole thing

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

