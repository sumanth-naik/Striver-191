def maximumMeetings(n,start,end):
    combined = [(start[i], end[i]) for i in range(n)]
    combined.sort(key=lambda x: x[1])
    endTime = 0
    numMeetings = 0
    for slot in combined:
        if endTime<slot[0]:
            numMeetings += 1
            endTime = slot[1]
    return numMeetings
    
start = [10, 12, 20]
end =  [20, 25, 30]
print(maximumMeetings(len(start), start, end))