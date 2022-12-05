
import heapq
events= [[6,6],[3,4],[22,26],[29,32],[8,10],[8,9],[30,30],[19,21],[30,34],[20,20],[29,32],[4,5],[16,17],[3,3],[14,16],[9,10],[2,5],[7,11],[3,3],[18,20],[26,28],[15,19],[26,27],[22,22],[2,3],[16,20],[2,3],[23,27],[25,28],[17,20]]
# events = [[2, 3], [2, 3], [2, 5], [3, 3], [3, 3], [3, 4], [4, 5], [6, 6]]
def maxNumOfMeetingsThatCanBeAttended(events):
    print(len(events))
    events.sort(key = lambda x: (x[0],x[1]))
    print(events)
    minHeap, numEvents = [], 0
    prevDayAttendable = 1
    index = 0
    while index<len(events):
        currEventStartDay = events[index][0]

        #fill days till yesterday
        while minHeap and prevDayAttendable<currEventStartDay:
            endDay = heapq.heappop(minHeap)
            if endDay>=prevDayAttendable:
                print("event attended", endDay, prevDayAttendable)
                numEvents += 1
                prevDayAttendable += 1
            else:
                print("evicted",endDay)

        while index<len(events) and currEventStartDay==events[index][0]:
            heapq.heappush(minHeap, events[index][1])
            index += 1
            print("Added", minHeap)
        
        #remove endDay before currEventStartDay from heap
        while minHeap and minHeap[0]<currEventStartDay:
            heapq.heappop(minHeap)
        #fill today
        print("event attended" ,heapq.heappop(minHeap))
        numEvents += 1

        prevDayAttendable = currEventStartDay + 1

    maxEndDate = max(events, key=lambda x:x[1])[1]
    print(minHeap, numEvents, maxEndDate)
    #fill days till maxEndDate
    while minHeap and prevDayAttendable<=maxEndDate:
        endDay = heapq.heappop(minHeap)
        if endDay>=prevDayAttendable:
            numEvents += 1
            prevDayAttendable += 1

    return numEvents


events = [[1,2],[1,2],[1,6],[1,2],[1,2]]
def maxNumOfMeetingsThatCanBeAttended(events):
    events.sort(key = lambda x: (x[0],x[1]))
    minHeap, numEvents = [], 0
    dayAttendable = 1
    index = 0
    while index<len(events):
        currEventStartDay = events[index][0]

        # assign valid dayAttendable incase there is nothing in heap
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

    # add all endTimes which are valid from the heap
    while minHeap:
        if minHeap[0]>=dayAttendable:
            numEvents += 1
            dayAttendable += 1
        heapq.heappop(minHeap)
        
    return numEvents




print(maxNumOfMeetingsThatCanBeAttended(events))






