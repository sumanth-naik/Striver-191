
nums = [-4,-3,-2,-1,0,0,1,2,3,4]

target = 0

validTuples = set()
nums.sort()
n = len(nums)
for i in range(0,n):
    for j in range(i+1, n):
        twoSumTarget = target - nums[i] - nums[j]
        
        l=n-1
        k=j+1
        while(k<l):
            print(i,j,k,l)
            if(twoSumTarget==nums[k] + nums[l]):
                print(i,j,k,l,"came")
                validTuples.add((nums[i],nums[j],nums[k],nums[l]))
                k += 1
                l -= 1
            elif(twoSumTarget>nums[k] + nums[l]):
                k += 1
            else:
                l -= 1
                
print(validTuples)
