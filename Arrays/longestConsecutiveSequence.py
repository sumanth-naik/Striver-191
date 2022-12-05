nums = [100,4,200,1,3,2]

numsSet = set(nums)
maxCount = 0
for num in numsSet:
    if not num-1 in numsSet:
        count = 0
        while num in numsSet:
            count += 1
            num += 1
        maxCount = max(maxCount,count)
print(maxCount)