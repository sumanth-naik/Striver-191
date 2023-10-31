# Key Idea 1: Recognise that we can flip greedily the next k numbers if this num is 0. But leads to n*k algo
# Key Idea 2: Maintain currFlippedTimes and isFlippedArr to avoid that factor of k
# Key Idea 3: currFlippedTimes should indicate if we need to flip this bit or not
# Key Idea 4: isFlippedArr should be used like sliding window to remove out of window flip counts in currFlippedTimes
# ref: https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/solutions/238609/java-c-python-one-pass-and-o-1-space/comments/239423

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        currFlippedTimes, isFlippedArr, n = 0, [False]*len(nums), len(nums)
        for index in range(n):
            if index-k>=0: # Key Idea 4
                currFlippedTimes -= isFlippedArr[index-k]
            if currFlippedTimes%2==nums[index]: # Key Idea 3
                if index+k>n: return -1
                currFlippedTimes += 1
                isFlippedArr[index] = True
        return sum(isFlippedArr)


# Key Idea 5: Instead of using isFlippedArr to store info, repurpose nums. 
#             If flipped when nums[i]==0, store 2; when nums[i]==1, store 3. 
# Note 1: Revert them back

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        currFlippedTimes, n, count = 0, len(nums), 0
        for index in range(n):
            if index-k>=0 and nums[index-k]>1:
                currFlippedTimes -= 1
                nums[index-k] -= 2 # Note 1
            if currFlippedTimes%2==nums[index]:
                if index+k>n:
                    for prev in range(max(0, index-k), index): # Note 1
                        if nums[prev]>1: nums[prev] -= 2
                    return -1
                nums[index] += 2
                currFlippedTimes += 1
                count += 1
        return count
            

