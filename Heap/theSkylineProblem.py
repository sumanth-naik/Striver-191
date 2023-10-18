import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        points, IS_END, IS_START = [], "end", "start"
        for left, right, height in buildings:
            points.append((left, height, IS_START))
            points.append((right, height, IS_END))
        points.sort(key=lambda x:(x[0],-x[1]) if x[2]==IS_START else (x[0],x[1]))

        skylinePoints, currentTallestBuildingHeight, maxHeap, lazyDelMap = [], 0, [0], {}
        for xCoordinate, height, type in points:
            if type==IS_START:
                heapq.heappush(maxHeap, -height)
            else:
                if not -height in lazyDelMap: lazyDelMap[-height] = 0
                lazyDelMap[-height] += 1
            
            while maxHeap[0] in lazyDelMap:
                height = heapq.heappop(maxHeap)
                lazyDelMap[height] -= 1
                if lazyDelMap[height]==0: del lazyDelMap[height]
            
            if currentTallestBuildingHeight!=maxHeap[0]:
                currentTallestBuildingHeight = maxHeap[0]
                skylinePoints.append((xCoordinate, -currentTallestBuildingHeight))
            
        return skylinePoints