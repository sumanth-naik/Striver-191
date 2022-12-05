

nums = [4,5,6,7,0]

low = 0
high = len(nums) -1
while(low<high):
    mid = (low+high)//2
    if(nums[mid]>nums[high]):
        low = mid+1
    else:
        high = mid
        
print(nums[low])