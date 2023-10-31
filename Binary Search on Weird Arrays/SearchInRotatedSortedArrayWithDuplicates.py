# Key Idea 1: check if num is at low, mid or high
# Key Idea 2: check if low to mid is sorted; or mid to high is sorted
# Key Idea 3: if any part is sorted, apply binary search to eliminate
# Key Idea 4: If no part is sorted, move left and right

class Solution:
    def search(self, nums, target: int) -> bool:
        n = len(nums)
        low, high = 0, n-1

        while low<=high:
            mid = (low+high)//2
            if target in [nums[low], nums[mid], nums[high]]: return True

            # if left part is sorted 
            if nums[low]<nums[mid]:
                # if strictly in between low and mid
                if nums[low]<=target<nums[mid]: high = mid-1
                else: low = mid+1

            # if right part is sorted
            elif nums[mid]<nums[high]:
                # if strictly in between mid and high
                if nums[mid]<target<=nums[high]: low = mid+1
                else: high = mid-1

            # no sorting condition satisfied and num is not at low, mid or high, so move both
            else:
                low += 1
                high -=1
        return False