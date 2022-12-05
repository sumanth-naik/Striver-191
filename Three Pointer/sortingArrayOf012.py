
nums = [2,0,2,1,1,0]

left, mid, right = 0, 0, len(nums) - 1

while(mid<=right):
    if(nums[mid]==0):
        nums[mid], nums[left] = nums[left], nums[mid]
        mid += 1
        left += 1
    elif(nums[mid]==1):
        mid += 1
    else:
        nums[mid], nums[right] = nums[right], nums[mid]
        right -= 1
        
print(nums)
        

