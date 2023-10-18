class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x:x[0])

        @lru_cache(None)
        def binSearch(currEventEnd):
            return bisect_right(events, currEventEnd, key=lambda x:x[0])

        @lru_cache(None)
        def recursion(index, kLeft):
            if kLeft==0 or index>=len(events): return 0
            valOfCurrEvent, currEventEnd = events[index][2], events[index][1]
            return max(recursion(index+1, kLeft), valOfCurrEvent + recursion(binSearch(currEventEnd), kLeft-1))

        return recursion(0, k)