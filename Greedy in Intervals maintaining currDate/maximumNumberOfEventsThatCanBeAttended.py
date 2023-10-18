class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        events.sort(key = lambda x: (x[0],x[1]))
        minHeap, numEvents = [], 0
        dayAttendable = 1
        index = 0
        while index<len(events):
            if index<len(events):
                currEventStartDay = events[index][0]

            if not minHeap:
                dayAttendable = currEventStartDay

            #add all events starting today to heap
            while index<len(events) and currEventStartDay==events[index][0]:
                heapq.heappush(minHeap, events[index][1])
                index += 1        

            #attend all events attendable till today
            while minHeap and minHeap[0]>=dayAttendable and dayAttendable<=currEventStartDay:
                heapq.heappop(minHeap)
                numEvents += 1
                dayAttendable += 1

            #remove elems with endDay before today from heap
            while minHeap and minHeap[0]<currEventStartDay:
                heapq.heappop(minHeap)

        while minHeap:
            if minHeap[0]>=dayAttendable:
                numEvents += 1
                dayAttendable += 1
            heapq.heappop(minHeap)

        return numEvents

# Why this fails: [[1,5],[1,5],[1,5],[2,3],[2,3]]
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        numEvents, lastEventEnd = 0, 1
        for start, end in sorted(events, key = lambda x:(x[1], x[0])):
            if lastEventEnd<=end:
                numEvents += 1
                lastEventEnd = max(start, lastEventEnd)+1
        return numEvents

        
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse=True)
        minHeapOfEndDates, attendedEventsCount, currDate = [], 0, 1
        while events or minHeapOfEndDates: # loop is actually on currDate
            if not minHeapOfEndDates: # if nothing in heap, skip ahead to a date some event starts
                currDate = events[-1][0]
            
            while events and events[-1][0]==currDate: # Add all started events on currDate
                heappush(minHeapOfEndDates, events.pop()[1]) 
            
            heappop(minHeapOfEndDates) # there will be atleast one event on currDate for sure
            attendedEventsCount += 1 # attend an event on currDate
            
            while minHeapOfEndDates and minHeapOfEndDates[0]==currDate: 
                heappop(minHeapOfEndDates) # cant attend any other event ending on currDate

            currDate += 1

        return attendedEventsCount


