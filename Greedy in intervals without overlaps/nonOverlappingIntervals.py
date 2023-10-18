class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        @lru_cache(None)
        def recursion(index):
            if index==len(intervals): return 0
            return max(1+recursion(bisect_left(intervals, intervals[index][1], key=lambda x:x[0])), recursion(index+1))

        return len(intervals) - recursion(0)
    

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        index, maxOverlappingIntervalsCount = 0, 0
        while index<len(intervals):
            maxOverlappingIntervalsCount += 1
            currEndTime = intervals[index][1]
            while index<len(intervals) and intervals[index][0]<currEndTime: index+=1
        return len(intervals) - maxOverlappingIntervalsCount
    

class Solution:
    def eraseOverlapIntervals(self, pairs: List[List[int]]) -> int:
        chainLength, chainTail = 0, -1e9
        for left, right in sorted(pairs, key=lambda x:x[1]):
            if chainTail<=left:
                chainLength += 1
                chainTail = right
        return len(pairs) - chainLength