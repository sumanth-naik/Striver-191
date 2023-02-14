

def findMinArrowShots(points):
    points.sort(key=lambda x:(x[0],x[1]))
    numArrows, index = 0, 0
    while index<len(points):
        nextBalloonToPickEnd = points[index][1]
        while index<len(points) and points[index][0]<=nextBalloonToPickEnd:
            nextBalloonToPickEnd = min(nextBalloonToPickEnd, points[index][1])
            index += 1
        numArrows += 1
    return numArrows
