class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        mergedIntervals = [intervals[0]]
        for left, right in intervals[1:]:
            if left<=mergedIntervals[-1][1]: 
                mergedIntervals[-1][1] = max(right, mergedIntervals[-1][1])
            else:
                mergedIntervals.append([left, right])
        return mergedIntervals