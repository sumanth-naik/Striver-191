points = [[1,2],[2,2],[4,2]]


def getOrientation(p1,p2,p3):
    orientation = (p3[1]-p2[1])*(p2[0]-p1[0]) - (p2[1]-p1[1])*(p3[0]-p2[0])
    if orientation>0:
        return 1
    elif orientation<0:
        return -1
    return 0

def monotoneChain(points):
    if len(points)<=2:
        return points

    # atleastOnePointNonColinear = False
    # p1,p2 = None, None
    # for point in points:
    #     if not p1: p1 = point
    #     elif not p2: p2 = point
    #     else:
    #         if getOrientation(p1,p2,point)!=0:
    #             atleastOnePointNonColinear = True
    #             break
    #         else:
    #             p2,p1 = point, p2
    # if not atleastOnePointNonColinear: return points

    sortedPoints = sorted(points, key=lambda point: (point[0], point[1]))
    topHull = []
    for point in sortedPoints:
        print(topHull, point)
        while len(topHull)>=2 and getOrientation(topHull[-2], topHull[-1], point)==1:
            topHull.pop()
        topHull.append(point)
    
    bottomHull = []
    for point in reversed(sortedPoints):
        while len(bottomHull)>=2 and getOrientation(bottomHull[-2], bottomHull[-1], point)==1:
            bottomHull.pop()
        bottomHull.append(point)
    
    hull = topHull + bottomHull[1:len(bottomHull)-1]
    return set([tuple(point) for point in hull])

print(monotoneChain(points))


[[0,0],[0,1],[0,2],[3,3],[3,2],[3,1],[3,0],[2,0],[1,0]]
[[1,1],[2,4],[3,3],[4,2],[2,0]]
[[1,2],[2,2],[4,2],[2,2]]
[[0,1],[0,2],[0,8],[2,9],[9,8],[9,5],[7,1],[1,0]]
[[0,2],[2,4],[3,3],[4,2],[1,1]]
[[0,3],[1,4],[2,5],[3,5],[4,5],[5,5],[6,5],[7,4],[7,3],[7,2],[6,1],[5,0],[4,0],[3,0],[2,1],[1,2]]

[[3,1],[0,0],[3,2],[2,0],[3,3],[1,0],[3,0],[0,2],[0,1]]
[[2,0],[2,4],[3,3],[4,2],[1,1]]
[[1,2],[4,2],[2,2]]
[[7,1],[0,2],[2,9],[9,8],[0,1],[9,5],[0,8],[1,0]]
[[4,2],[3,3],[2,4],[1,1],[0,2]]
[[7,2],[6,5],[7,3],[7,4],[3,5],[5,0],[1,2],[2,5],[0,3],[5,5],[4,0],[1,4],[2,1],[3,0],[6,1],[4,5]]



[[0,0],[0,1],[0,2],[3,3],[3,2],[3,1],[3,0],[2,0],[1,0]]
[[1,1],[2,4],[3,3],[4,2],[2,0]]
[[1,2],[2,2],[4,2],[2,2]]
[[0,1],[0,2],[0,8],[2,9],[9,8],[9,5],[7,1],[1,0]]
[[0,2],[2,4],[3,3],[4,2],[1,1]]
[[0,3],[1,4],[2,5],[3,5],[4,5],[5,5],[6,5],[7,4],[7,3],[7,2],[6,1],[5,0],[4,0],[3,0],[2,1],[1,2]]



[[3,1],[0,0],[3,2],[2,0],[3,3],[1,0],[3,0],[0,2],[0,1]]
[[2,0],[2,4],[3,3],[4,2],[1,1]]
[[1,2],[4,2],[2,2]]
[[7,1],[0,2],[2,9],[9,8],[0,1],[9,5],[0,8],[1,0]]
[[4,2],[3,3],[2,4],[1,1],[0,2]]
[[7,2],[6,5],[7,3],[7,4],[3,5],[5,0],[1,2],[2,5],[0,3],[5,5],[4,0],[1,4],[2,1],[3,0],[6,1],[4,5]]