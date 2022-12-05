nums = [4,5,6,7,0,1,2]
target = 0

low = 0
high = len(nums) - 1

last = nums[len(nums)-1]
first = nums[0]
while(low<=high):
    mid = (low+high)//2
    if nums[mid] ==target:
        print(mid)
    if nums[mid]>last:
        if(last<target<nums[mid]):
            high = mid - 1
        else:
            low = mid + 1
    else:
        if(nums[mid]<target<=last):
            low = mid + 1
        else:
            high = mid - 1
            
            
    
while(low<=high):
    mid = (low+high)//2
    if nums[mid]==target: print(mid)
    if nums[mid]>=nums[low]:
        if nums[low]<=target<nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        if nums[mid]<target<=nums[high]:
            low = mid + 1
        else:
            high = mid - 1
