nums = [1,3,-1,-3,-2,4]
k = 3

from collections import deque

def slidingWindowMax(nums, k):
    deq = deque()
    windowMaxList = []
    for i in range(0, len(nums)):
        num = nums[i]
        while deq and deq[-1][0]<num:
            deq.pop()
        deq.append((num, i))
        
        if i>=k-1:
            windowMaxList.append(deq[0][0])
            if deq and deq[0][1]<=i-k+1:
                deq.popleft()
            
    return windowMaxList


print(slidingWindowMax(nums,k))
            