class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        minHeapOfEndDatesAndVals = []
        maxValSeenBeforeCurrDate, maxPairValues = 0, 0
        events.sort(reverse = True)
        
        while events:
            currDate = events[-1][0]
            while minHeapOfEndDatesAndVals and minHeapOfEndDatesAndVals[0][0]<currDate: # remove old intervals and update max
                maxValSeenBeforeCurrDate = max(maxValSeenBeforeCurrDate, heappop(minHeapOfEndDatesAndVals)[1])
            while events and events[-1][0]==currDate: # add new intervals and use the older max
                endDateAndVal = events.pop()[1:]
                heappush(minHeapOfEndDatesAndVals, endDateAndVal)
                maxPairValues = max(maxPairValues, endDateAndVal[1]+maxValSeenBeforeCurrDate)

        return maxPairValues

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        minHeapOfEndDatesAndVals, maxValSeenBeforeCurrDate, maxPairValues = [], 0, 0
        for start, end, val in sorted(events):
            while minHeapOfEndDatesAndVals and minHeapOfEndDatesAndVals[0][0]<start: # remove old intervals and update max
                maxValSeenBeforeCurrDate = max(maxValSeenBeforeCurrDate, heappop(minHeapOfEndDatesAndVals)[1])
            heappush(minHeapOfEndDatesAndVals, [end, val])
            maxPairValues = max(maxPairValues, val+maxValSeenBeforeCurrDate)
        return maxPairValues

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)

        @lru_cache(None)
        def recursion(index, k):
            if k==0 or index==n: return 0
            # take it, not take it
            return max(events[index][2]+recursion(bisect_left(events, [events[index][1]+1, -1e9, -1e9], index+1, n), k-1), recursion(index+1, k))

        return recursion(0, 2)