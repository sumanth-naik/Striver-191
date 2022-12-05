def getNumSubArrays(i, j, prevJ):
    if(prevJ<i):
        return ((j-i+1)*(j-i+2))/2
    else:
        return ((j-i+1)*(j-i+2))/2 - getNumSubArrays(i, prevJ, -1)


def countSubArrysWithScoreLessThanK(arr, k):
    numSubArrays = 0
    i = 0
    j = 0
    n = len(arr)
    prevJ = -1
    sumFromIToJ = arr[0]
    while(j<n):
        #increment i if score is more tham or equal to k
        print("istart: ",i, j, prevJ, sumFromIToJ)
        while(sumFromIToJ*(j-i+1)>=k):
            sumFromIToJ = sumFromIToJ - arr[i]
            i = i+1
            if(i>j and i<n):
                j = i
                sumFromIToJ = sumFromIToJ + arr[j]
            if(i==n):
                break

        print("inc i: ",i, j, prevJ, sumFromIToJ)
        #increment j if you can
        while(j+1<n and (sumFromIToJ+arr[j+1])*(j-i+2)<k):
            j = j+1
            sumFromIToJ = sumFromIToJ + arr[j]
            
        print("inc j: ",i, j, prevJ, sumFromIToJ)
        numSubArrays = numSubArrays + getNumSubArrays(i, j, prevJ)
        
        prevJ = j
        i += 1
        j += 1
        if j<n:
            sumFromIToJ = sumFromIToJ-arr[i-1] + arr[j]
        print("inc i,j: ",i, j, prevJ, sumFromIToJ)
        print()

    return numSubArrays

nums = [1,2,1]
k = 6
print(countSubArrysWithScoreLessThanK(nums, k))
        

        
'''
def countSubarrays(self, nums: List[int], k: int) -> int:
    sum, res, j = 0, 0, 0
    for i, n in enumerate(nums):
        sum += n
        while sum * (i - j + 1) >= k:
            sum -= nums[j]
            j += 1
        res += i - j + 1
    return res
    
    
    adds all the subarrays that ends at i starting at j or later, both inclusive that are valid
    
    
        
https://leetcode.com/problems/count-subarrays-with-score-less-than-k/discuss/2138778/Sliding-Window
        
        '''
                
                
