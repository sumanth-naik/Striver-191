

points = [[0,0],[0,1],[0,2],[1,2],[2,2],[3,2],[3,1],[3,0],[2,0],[1,0],[1,1],[3,3]]
[[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
[[1,2],[2,2],[4,2]]
[[0,1],[0,2],[0,8],[1,0],[1,3],[1,6],[2,7],[2,8],[2,9],[3,8],[4,4],[4,6],[5,2],[6,1],[6,7],[7,1],[7,2],[7,4],[8,4],[8,5],[8,7],[9,5],[9,8]]
[[0,2],[1,1],[2,2],[2,4],[4,2],[3,3]]
[[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[1,3],[1,2],[2,1],[4,2],[0,3]]
import math



        
def getOrientation(p1,p2, p3):
    diffSlope = (p3[1]-p2[1])*(p2[0]-p1[0]) - (p2[1]-p1[1])*(p3[0]-p2[0])
    if diffSlope>0:
        return 1
    if diffSlope<0:
        return -1
    return 0

def polarAngle(point, bottomMostPoint):
    return math.atan2(point[1]-bottomMostPoint[1],point[0]-bottomMostPoint[0])

def dist(point1, point2):
    return math.sqrt((point2[1]-point1[1])**2 + (point2[0]-point1[0])**2)

def grahamScan(points):
    points = [tuple(point)  for point in points]
    if len(points)==1: return points
    bottomMostPoint = min(points, key= lambda point: (point[1], point[0]))
    print(bottomMostPoint)
    polarAngleWiseSortedPoints = sorted(points, key= lambda point: (polarAngle(point, bottomMostPoint), -dist(point, bottomMostPoint)))
    print(polarAngleWiseSortedPoints)
    start = 0
    if bottomMostPoint==polarAngleWiseSortedPoints[0]:
        hullStack = [bottomMostPoint, polarAngleWiseSortedPoints[1]]
        start = 2
    else:
        hullStack = [bottomMostPoint, polarAngleWiseSortedPoints[0]]
        start = 1
    collinearPointsMap = {}
    for i in range(start, len(polarAngleWiseSortedPoints)):
        point = polarAngleWiseSortedPoints[i]
        print(point, hullStack, collinearPointsMap)
        beforeLast, last = hullStack[-2], hullStack[-1]
        while getOrientation(beforeLast, last, point)==-1 and getOrientation(bottomMostPoint, last, point)!=0:
            hullStack.pop()
            if last in collinearPointsMap:
                del collinearPointsMap[last]
            print(hullStack)
            beforeLast, last = hullStack[-2], hullStack[-1]
        if getOrientation(bottomMostPoint, last, point)==0:
            if not last in collinearPointsMap:
                collinearPointsMap[last] = []
            collinearPointsMap[last].append(point)
        else:
            hullStack.append(point)
        print(hullStack)

    minAngle = polarAngle(hullStack[0], hullStack[1])
    maxAngle = polarAngle(hullStack[0], hullStack[-1])
    for keyPoint in collinearPointsMap:
        polarAngleOfKeyPointWithBottomMostPoint = polarAngle(bottomMostPoint, keyPoint)
        if polarAngleOfKeyPointWithBottomMostPoint==minAngle or polarAngleOfKeyPointWithBottomMostPoint==maxAngle:
            hullStack += collinearPointsMap[keyPoint]
    return hullStack

print(grahamScan(points))