# nums = [2,0,1,2]
# target = 1

# def search(nums, target):
    
#     low = 0
#     high = len(nums) - 1

#     while(low<=high):

#         mid = (low+high)//2
#         if(nums[mid]==target): 
#             return True
#         if(nums[low]==nums[mid]==nums[high]):
#             low = low + 1
#             high = high - 1

#         elif nums[low] <= nums[mid] <= nums[high]:
#             if target < nums[mid]:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         elif nums[high] <= nums[low] <= nums[mid]:
#             if nums[low] <= target < nums[mid]:
#                 high = mid - 1
#             else: 
#                 low = mid + 1
#         else:
#             if nums[mid]< target <= nums[high]:
#                 low = mid + 1
#             else:
#                 high = mid -1
#     return False
# print(search(nums,target))


class Solution:
    def search(self, nums, target: int) -> bool:
        n = len(nums)
        low, high = 0, n-1

        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target: return True

            # if left part is sorted 
            if nums[low]<nums[mid]:
                # if strictly in between low and mid
                if nums[low]<=target<nums[mid]: high = mid-1
                else: low = mid+1

            # if right part is sorted
            if nums[mid]<nums[high]:
                # if strictly in between mid and high
                if nums[mid]<target<=nums[high]: low = mid+1
                else: high = mid-1

            # no sorting condition satisfied, so move one step left or right
            elif nums[low]==nums[mid]: 
                low += 1
            elif nums[mid]==nums[high]: 
                high -=1
        return False