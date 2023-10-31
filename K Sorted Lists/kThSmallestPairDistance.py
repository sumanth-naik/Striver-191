# Key Idea 1: order doesn't matter

'''
    1 2 3 4

1   - 1 2 3
2     - 1 2
3       - 1
4         -      
'''
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        def countSmallerOrEqualTo(num):
            count, j = 0, 0
            for i in range(n-1):
                while j+1!=n and nums[j+1]-nums[i]<=num:
                    j += 1
                count += (j-i)
            return count

        low, high = 0, nums[-1]-nums[0]
        while low<high:
            mid = (low+high)//2
            count = countSmallerOrEqualTo(mid)
            if count==k: # mid may not be present
                high = mid
            elif count>k: # duplicates case
                high = mid
            else:
                low = mid+1
        return low