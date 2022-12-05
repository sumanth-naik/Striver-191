import heapq
nums = [1,3,-1,-3,-2,4]
k = 3
def maxSlidingWindow(nums, k):
    maxHeap = [-nums[i] for i in range(0,k-1)]
    removeCountMap = {}
    windowMaxList = []
    heapq.heapify(maxHeap)

    for i in range(k-1, len(nums)):
        heapq.heappush(maxHeap, -nums[i])
        
        while maxHeap[0] in removeCountMap:
            removeCountMap[maxHeap[0]] -= 1
            if removeCountMap[maxHeap[0]]==0:
                del removeCountMap[maxHeap[0]]
            heapq.heappop(maxHeap)
        
        windowMaxList.append(-maxHeap[0])
        if -nums[i-k+1] not in removeCountMap:
            removeCountMap[-nums[i-k+1]] = 0
        removeCountMap[-nums[i-k+1]] += 1

    return windowMaxList

print(maxSlidingWindow(nums,k))