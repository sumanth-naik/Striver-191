import heapq
class Solution:
    def medianSlidingWindow(self, nums, k: int):

        # maxHeap stores one more number in case total is odd
        maxHeap, minHeap = [], []
        numValidInMaxHeap, numValidInMinHeap = 0, 0
        numsToLazyDeleteMap = defaultdict(int)

        def addToHeaps(num):
            nonlocal maxHeap, minHeap, numValidInMaxHeap, numValidInMinHeap
            if not maxHeap or -maxHeap[0]>=num:
                heapq.heappush(maxHeap, -num)
                numValidInMaxHeap += 1
            else:
                heapq.heappush(minHeap, num)
                numValidInMinHeap += 1
            rebalanceHeaps()

        def rebalanceHeaps():
            nonlocal maxHeap, minHeap, numValidInMaxHeap, numValidInMinHeap
            if numValidInMaxHeap>1+numValidInMinHeap:
                heapq.heappush(minHeap, -heapq.heappop(maxHeap))
                numValidInMaxHeap-=1
                numValidInMinHeap+=1
            elif numValidInMinHeap>numValidInMaxHeap:
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))
                numValidInMinHeap-=1
                numValidInMaxHeap+=1

        def updateNumValidInHeapsAndLazyDeleteMap(num):
            nonlocal numValidInMaxHeap, numValidInMinHeap, numsToLazyDeleteMap
            if -maxHeap[0]>=num:
                numValidInMaxHeap -= 1
            else:
                numValidInMinHeap -= 1
            numsToLazyDeleteMap[num] += 1

        def getMedian():
            nonlocal maxHeap, minHeap, numValidInMaxHeap, numValidInMinHeap, numsToLazyDeleteMap
            # lazy del
            while maxHeap and numsToLazyDeleteMap[-maxHeap[0]]>0:
                numsToLazyDeleteMap[-heapq.heappop(maxHeap)] -= 1
            while minHeap and numsToLazyDeleteMap[minHeap[0]]>0:
                numsToLazyDeleteMap[heapq.heappop(minHeap)] -= 1
            return -maxHeap[0] if k&1 else (-maxHeap[0]+minHeap[0])/2

        for index in range(k):
            addToHeaps(nums[index])

        listOfMedians = [getMedian()]

        for indexToAdd in range(k, len(nums)):
            indexToRemove = indexToAdd - k
            updateNumValidInHeapsAndLazyDeleteMap(nums[indexToRemove])
            addToHeaps(nums[indexToAdd])
            listOfMedians.append(getMedian())

        return listOfMedians

