class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        maxHeapOfQuality, minPaid, qualitiesSum = [], 1e9, 0
        for ratio, qualityOfPerson in sorted((wage[index]/quality[index], quality[index]) for index in range(len(wage))):
            heappush(maxHeapOfQuality, -qualityOfPerson)
            qualitiesSum += qualityOfPerson
            if len(maxHeapOfQuality)==k:
                minPaid = min(minPaid, qualitiesSum*ratio)
                qualitiesSum += heappop(maxHeapOfQuality)
        return minPaid
