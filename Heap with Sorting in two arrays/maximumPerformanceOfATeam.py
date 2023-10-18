class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        minHeapOfSpeeds, sumOfSpeeds, maxPerf, MOD = [], 0, 0, 10**9+7
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            heappush(minHeapOfSpeeds, s)
            sumOfSpeeds += s
            maxPerf = max(maxPerf, sumOfSpeeds*e)
            if len(minHeapOfSpeeds)==k:
                sumOfSpeeds -= heappop(minHeapOfSpeeds)
        return maxPerf%MOD