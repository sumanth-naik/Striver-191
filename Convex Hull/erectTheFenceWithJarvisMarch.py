import math

points = [[0,1],[0,2],[0,8],[1,0],[1,3],[1,6],[2,7],[2,8],[2,9],[3,8],[4,4],[4,6],[5,2],[6,1],[6,7],[7,1],[7,2],[7,4],[8,4],[8,5],[8,7],[9,5],[9,8]]
points = [[0,2],[1,1],[2,2],[2,4],[4,2],[3,3]]


def dist(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 +(p1[1]-p2[1])**2)  

        
def getOrientation(p1,p2, p3):
    diffSlope = (p3[1]-p2[1])*(p2[0]-p1[0]) - (p2[1]-p1[1])*(p3[0]-p2[0])
    if diffSlope>0:
        return 1
    if diffSlope<0:
        return -1
    return 0
    
def jarvisMarch(points):
    points = [tuple(point) for point in points]
    leftMostPoint = min(points)
    hullSet = set([leftMostPoint])
    lastOnHull = leftMostPoint
    while True:
        potentialNext = None
        #potentialNext if the first point which is not added yet
        for point in points:
            if point not in hullSet:
                potentialNext = point
                break

        #if we haven't found any pothentailNect (all points are used)
        if not potentialNext:
            break

        # Add collinear points to potentialNext to this set
        # This needs to happen as if lastOnHull = (0,0) and potenitalNext = (2,0) and point = (1,0)
        # (1,0) needs to be added as well  

        #just remove this set if minimum number of points is required
        collinearWithPotentialNext = set()
        for point in points:
            orientation = getOrientation(lastOnHull, potentialNext, point)
            if orientation==1:
                potentialNext = point
                collinearWithPotentialNext = set()
            if orientation==0:
                # If further distnant collinear point is found update potentialNext
                if dist(lastOnHull, point)>dist(lastOnHull, potentialNext):
                    collinearWithPotentialNext.add(potentialNext)
                    potentialNext = point
                # If not, just add to collinearWithPotentialNext Set
                else:
                    collinearWithPotentialNext.add(point)


        # Don't forget to add collinearWithPotentialNext points to hullSet if we closed the hull
        if potentialNext in hullSet:
            hullSet = hullSet.union(collinearWithPotentialNext)
            break
        else:
            hullSet.add(potentialNext)
            hullSet = hullSet.union(collinearWithPotentialNext)
            lastOnHull = potentialNext

    return hullSet


points = [[0,0],[0,1],[0,2],[1,2],[2,2],[3,2],[3,1],[3,0],[2,0],[1,0],[1,1],[3,3]]

print(jarvisMarch(points))

[[0,0],[0,1],[0,2],[1,2],[2,2],[3,2],[3,1],[3,0],[2,0],[1,0],[1,1],[3,3]]
[[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
[[1,2],[2,2],[4,2]]
[[0,1],[0,2],[0,8],[1,0],[1,3],[1,6],[2,7],[2,8],[2,9],[3,8],[4,4],[4,6],[5,2],[6,1],[6,7],[7,1],[7,2],[7,4],[8,4],[8,5],[8,7],[9,5],[9,8]]
[[0,2],[1,1],[2,2],[2,4],[4,2],[3,3]]
[[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[1,3],[1,2],[2,1],[4,2],[0,3]]


print (math.atan(0.39))
print (math.atan(67))
print (math.atan(-21))