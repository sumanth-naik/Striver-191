class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        leftMaxArray = []
        leftMax = -10e10
        n = len(nums)
        for i in range(0, n):
            if i%k==0:
                leftMax = -10e10
            leftMax = max(leftMax, nums[i])
            leftMaxArray.append(leftMax)

        rightMaxArray = []
        rightMax = -10e10
        for i in range(n-1, -1, -1):
            rightMax = max(rightMax, nums[i])
            rightMaxArray.append(rightMax)
            if i%k==0:
                rightMax = -10e10
        rightMaxArray.reverse()
        
        return [max(rightMaxArray[i],leftMaxArray[i+k-1]) for i in range(n-k+1)]

        
        
        
        
#         deq = deque()
#         windowMaxList = []
#         for i in range(0, len(nums)):
#             num = nums[i]
#             while deq and deq[-1][0]<num:
#                 deq.pop()
#             deq.append((num, i))

#             if i>=k-1:
#                 windowMaxList.append(deq[0][0])
#                 if deq and deq[0][1]<=i-k+1:
#                     deq.popleft()

#         return windowMaxList






#         maxHeap = [-nums[i] for i in range(0,k-1)]
#         removeCountMap = {}
#         windowMaxList = []
#         heapq.heapify(maxHeap)

#         for i in range(k-1, len(nums)):
#             heapq.heappush(maxHeap, -nums[i])

#             while maxHeap[0] in removeCountMap:
#                 removeCountMap[maxHeap[0]] -= 1
#                 if removeCountMap[maxHeap[0]]==0:
#                     del removeCountMap[maxHeap[0]]
#                 heapq.heappop(maxHeap)

#             windowMaxList.append(-maxHeap[0])
#             if -nums[i-k+1] not in removeCountMap:
#                 removeCountMap[-nums[i-k+1]] = 0
#             removeCountMap[-nums[i-k+1]] += 1

#         return windowMaxList

# 5 min
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq, windowMaximumsArr = deque(), []
        for index, num in enumerate(nums):
            while deq and deq[-1][1]<num: deq.pop()
            deq.append((index, num))
            if index>=k-1:
                windowMaximumsArr.append(deq[0][1])
                if deq[0][0]==index-k+1: deq.popleft()
        return windowMaximumsArr

# 9 min
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        leftMaxArr, rightMaxArr = [nums[0]], [nums[-1]]
        for index in range(1, n):
            leftMaxArr.append(max(nums[index], leftMaxArr[-1] if index%k!=0 else -1e10))
        for index in range(n-2, -1, -1):
            rightMaxArr.append(max(nums[index], rightMaxArr[-1] if (index+1)%k!=0 else -1e10))
        rightMaxArr.reverse()
        return [max(rightMaxArr[index], leftMaxArr[index+k-1]) for index in range(n-k+1)]

# 4 min
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap, maximumsArr = [], []
        for index, num in enumerate(nums):
            heapq.heappush(maxHeap, (-num, index))
            if index>=k-1:
                while maxHeap[0][1]<=index-k: heapq.heappop(maxHeap)
                maximumsArr.append(-maxHeap[0][0])
        return maximumsArr



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