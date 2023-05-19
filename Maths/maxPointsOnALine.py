def slopeAndIntercept(x1, y1, x2, y2):
    num, den = y2-y1, x2-x1
    if den==0:
        return float('inf'), x1
    else:
        return num/den, round(y1 - (num/den)*x1, 5)

def maxPointsOnALine(points):
    if len(points)==1: return 1
    slopeAndInterceptCounts = {}
    for firstPoint in points:
        for secondPoint in points:
            if firstPoint is not secondPoint:
                slope, intercept = slopeAndIntercept(firstPoint[0], firstPoint[1], secondPoint[0], secondPoint[1])
                if (slope,intercept) not in slopeAndInterceptCounts:
                    slopeAndInterceptCounts[(slope,intercept)] = 0
                slopeAndInterceptCounts[(slope,intercept)] += 1
    maxCount = max(slopeAndInterceptCounts.values())
    return (int)(sqrt(1+4*maxCount)+1)//2

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        def getSlope(x1, y1, x2, y2):
            num, den = (y2-y1), (x2-x1)
            if den==0: return -float('inf')
            return round(num/den, 10)
        
        maxPoints = 0
        for x1, y1 in points:
            slopesMap = defaultdict(int)
            for x2, y2 in points: 
                if (x1,y1)!=(x2,y2):
                    slopesMap[getSlope(x1,y1,x2,y2)] += 1
            maxPoints = max(maxPoints, max(slopesMap.values() or [0]))
        return maxPoints+1