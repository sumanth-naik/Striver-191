
nums = [1,1,1,1,1,0,0,1]

low = 0
high = len(nums) - 1

while(low<high):
    mid = (low+high)//2
    if nums[mid]<nums[high]:
        high = mid
    elif nums[mid]>nums[high]:
        low = mid + 1
    else:
        high-=1

print(nums[low])