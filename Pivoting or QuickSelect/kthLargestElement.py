nums =  [3,2,3,4,2,4,5,5,6]
k = 4


def findKthLargest(nums, k):
    
    high = len(nums) - 1
    low = 0

    while low<=high:

        pivot = nums[high]
        swapPointer = low

        for i in range(low, high):
            if nums[i]>pivot:
                nums[swapPointer], nums[i] = nums[i], nums[swapPointer]
                swapPointer += 1
            
        nums[swapPointer], nums[high] = nums[high], nums[swapPointer]

        numberOfNumsGreaterOrEqualToPivot = swapPointer - low + 1
        if numberOfNumsGreaterOrEqualToPivot==k:
            return nums[swapPointer]
        elif numberOfNumsGreaterOrEqualToPivot<k:
            low = swapPointer + 1
            k -= numberOfNumsGreaterOrEqualToPivot
        else:
            high = swapPointer - 1


print(findKthLargest(nums, k))