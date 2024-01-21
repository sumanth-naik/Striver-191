# fails for n=2 and meetings=[[0,10],[1,2],[12,14],[13,15]]
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        minHeapOfEndTimeAndRoomNumber, numMeetings = [(0, roomNum) for roomNum in range(n)], [0 for _ in range(n)]
        heapify(minHeapOfEndTimeAndRoomNumber)
        meetings.reverse()
        while meetings:
            start, end = meetings.pop()
            bestEndTime, roomNum = heappop(minHeapOfEndTimeAndRoomNumber)
            print(meetings, roomNum)
            numMeetings[roomNum] += 1
            heappush(minHeapOfEndTimeAndRoomNumber, (bestEndTime+end-start+1, roomNum))
            print(minHeapOfEndTimeAndRoomNumber)

        mostMeetings = max(numMeetings)
        for roomNum in range(n):
            if numMeetings[roomNum]==mostMeetings:
                return roomNum



class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available, booked = [roomNum for roomNum in range(n)], []
        numMeetings = [0 for _ in range(n)]
        heapify(available)
        meetings.sort(reverse=True)
        while meetings:
            start, end = meetings.pop()
            actualMeetingStart = start # this is wrong, should be max(actualMeetingStart, start)
            if not available:
                actualMeetingStart = max(start, booked[0][0])
            while booked and booked[0][0]<=actualMeetingStart:
                endTime, roomNum = heappop(booked)
                heappush(available, roomNum)
            roomNum = heappop(available)
            numMeetings[roomNum] += 1
            heappush(booked,((actualMeetingStart + end-start), roomNum))

        mostMeetings = max(numMeetings)
        for roomNum in range(n):
            if numMeetings[roomNum]==mostMeetings:
                return roomNum


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available, booked = [roomNum for roomNum in range(n)], []
        numMeetings, currDate = [0 for _ in range(n)], 0
        heapify(available)
        for start, end in sorted(meetings):
            currDate = max(start, currDate)
            if not available:
                currDate = max(booked[0][0], currDate)
            
            while booked and booked[0][0]<=currDate:
                endTime, roomNum = heappop(booked)
                heappush(available, roomNum)
           
            roomNum = heappop(available)
            numMeetings[roomNum] += 1
            heappush(booked, (currDate + end-start, roomNum))

        return numMeetings.index(max(numMeetings))

