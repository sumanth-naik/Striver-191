import math
def bucketSort(nums):
    sortedArray = []
    numBuckets = len(nums)
    minNum = min(nums)
    maxNumsInEachBucket = math.ceil((max(nums) - minNum +1)/numBuckets)
    buckets = [[] for _ in range(numBuckets)]
    for num in nums:
        buckets[(num-minNum)//maxNumsInEachBucket].append(num)
    for bucket in buckets:
        bucket.sort()
        for num in bucket:
            sortedArray.append(num)
    return sortedArray

def maximumGap(nums) -> int:   
    sortedArr = bucketSort(nums) 
    maxGap = 0
    for i in range(len(nums)-1):
        maxGap = max(maxGap, sortedArr[i+1]-sortedArr[i])
    return maxGap
nums = [3,6,9,1]   
print(maximumGap(nums))