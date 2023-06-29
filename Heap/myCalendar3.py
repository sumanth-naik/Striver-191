from sortedcontainers import SortedList, SortedDict
import heapq
class MyCalendarThree:

    def __init__(self):
        self.sortedListOfStartTimes = SortedList()

    def book(self, startTime: int, endTime: int) -> int:
        self.sortedListOfStartTimes.add((startTime, endTime))
        maxK, minHeapOfEndTimes = 1, []
        for startTime, endTime in self.sortedListOfStartTimes:
            heapq.heappush(minHeapOfEndTimes, (endTime, startTime))
            while minHeapOfEndTimes and minHeapOfEndTimes[0][0]<=startTime:
                heapq.heappop(minHeapOfEndTimes)
            maxK = max(maxK, len(minHeapOfEndTimes))
        return maxK


class MyCalendarThree:

    def __init__(self):
        self.sortedDict = SortedDict()

    def book(self, startTime: int, endTime: int) -> int:
        self.sortedDict[startTime] = self.sortedDict.get(startTime, 0) + 1
        self.sortedDict[endTime] =  self.sortedDict.get(endTime, 0) - 1
        numMeetings, maxK = 0, 0
        for time in self.sortedDict.keys():
            numMeetings += self.sortedDict[time]
            maxK = max(maxK, numMeetings)
        return maxK


import bisect

class MyCalendarThree:

    def __init__(self):
        # since time range is continuous storing only start time is enough
        self.startTimesAndCountsSortedList = SortedList([[0, 0]])
        self.maxK = 1

    def splitAt(self, time):
        index = bisect.bisect_right(self.startTimesAndCountsSortedList, [time, 1e9]) - 1
        if self.startTimesAndCountsSortedList[index][0]==time: return index
        self.startTimesAndCountsSortedList.add([time, self.startTimesAndCountsSortedList[index][1]])
        return index+1

    def book(self, startTime: int, endTime: int) -> int:
        startIndex = self.splitAt(startTime)
        endIndex = self.splitAt(endTime)
        for index in range(startIndex, endIndex):
            self.startTimesAndCountsSortedList[index][1] += 1
            self.maxK = max(self.maxK, self.startTimesAndCountsSortedList[index][1])
        return self.maxK
    


class MyCalendarThree:

    def __init__(self):
        # store max Booking in [L,R] here
        self.vals = {}
        # store values in this if entire [L, R] has a booking 
        # (lazy because we dont care about really updating entire segment tree)
        self.lazy = {}

    def update(self, start, end, index = 0, left = 0, right=10**9):
        if end<left or right<start: return
        if start<=left<=right<=end:
            self.lazy[index] += 1
            self.vals[index] += 1
        else:
            mid = (left+right)//2
            self.update(start, end, 2*index+1, left, mid)
            self.update(start, end, 2*index+2, mid+1, right)
            self.vals[index] = self.lazy[index] + max(self.vals[2*index+1], self.vals[2*index+2])
       
    def book(self, startTime: int, endTime: int) -> int:
        self.update(startTime, endTime-1)
        return self.vals[0]