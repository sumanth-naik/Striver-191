class Solution:
    def insert(self, intervals, newInterval):
        i, ansArr, isInserted = 0, [], False
        while i<len(intervals):
            if intervals[i][0]>newInterval[1] and not isInserted:
                ansArr.append(newInterval)
                isInserted = True
            elif intervals[i][1]>=newInterval[0] and not isInserted:
                start = min(intervals[i][0], newInterval[0])
                end = newInterval[1]
                while i<len(intervals) and intervals[i][0]<=newInterval[1]:
                    end = max(end, intervals[i][1])
                    i += 1
                ansArr.append([start, end])
                isInserted = True
            else:
                ansArr.append(intervals[i])
                i += 1
        if not isInserted:
            ansArr.append(newInterval)
        return ansArr
                    
    def insertElegant(self, intervals, newInterval):
        leftIntervals, midInterval, rightIntervals = [], newInterval, []
        for interval in intervals:
            if interval[1]<newInterval[0]:
                leftIntervals.append(interval)
            elif interval[0]>newInterval[1]:
                rightIntervals.append(interval)
            else:
                midInterval[0] = min(midInterval[0], interval[0])
                midInterval[1] = max(midInterval[1], interval[1])
        return leftIntervals +  [midInterval] + rightIntervals

