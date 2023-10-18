class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        if len(dist)>ceil(hour): return -1

        def isPossibleToReachOnTime(speed):
            timeTaken = 0
            for index in range(len(dist)):
                timeTaken += (ceil(dist[index]/speed) if index!=len(dist)-1 else dist[index]/speed)
            return timeTaken<=hour
        
        decimalPartInHour = hour%1 or 1
        low, high = 1, ceil(max(dist)/decimalPartInHour)
        while low<high:
            mid = (low+high)//2
            if isPossibleToReachOnTime(mid): high = mid
            else: low = mid + 1

        return low