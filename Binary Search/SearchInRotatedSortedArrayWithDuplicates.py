nums = [2,0,1,2]
target = 1

def search(nums, target):
    
    low = 0
    high = len(nums) - 1

    while(low<=high):

        mid = (low+high)//2
        if(nums[mid]==target): 
            return True
        if(nums[low]==nums[mid]==nums[high]):
            low = low + 1
            high = high - 1

        elif nums[low] <= nums[mid] <= nums[high]:
            if target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        elif nums[high] <= nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else: 
                low = mid + 1
        else:
            if nums[mid]< target <= nums[high]:
                low = mid + 1
            else:
                high = mid -1
    return False
print(search(nums,target))