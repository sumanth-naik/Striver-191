
ax1 = -3
ay1 = 0
ax2 = 3
ay2 = 4
bx1 = 0
by1 = -1
bx2 = 9
by2 = 2
def computeArea(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        return min(computeAreaWithBSmallerThanA(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2), computeAreaWithBSmallerThanA(bx1, by1, bx2, by2, ax1, ay1, ax2, ay2))

        
def addInternalPoints(ax1, ay1, ax2, ay2, bx, by, internalPoints):
    if ax1<=bx<=ax2 and ay1<=by<=ay2: 
        internalPoints.append((bx, by))

def computeAreaWithBSmallerThanA(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):

    areaSum = (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1)
    bx3 = bx1
    by3 = by2
    bx4 = bx2
    by4 = by1
    ax3, ay3, ax4, ay4 = ax1, ay2, ax2, ay1

    if ax1<=bx1<=bx2<=ax2 and by1<=ay1<=ay2<=by2:
        return areaSum - (bx2-bx1)*(ay2-ay1) 
    internalPoints = []
    for bx, by in [(bx1, by1), (bx2, by2), (bx3, by3), (bx4, by4)]:
        addInternalPoints(ax1, ay1, ax2, ay2, bx, by, internalPoints)
    print(internalPoints)
    if len(internalPoints)==0:
        return areaSum

    if len(internalPoints)==1:
        internalPoint = internalPoints.pop()
        if internalPoint[0]==bx1 and internalPoint[1]==by1:
            return areaSum - (ax2-bx1)*(ay2-by1)
        elif internalPoint[0]==bx2 and internalPoint[1]==by2:
            return areaSum - (bx2-ax1)*(by2-ay1)
        elif internalPoint[0]==bx3 and internalPoint[1]==by3:
            return areaSum - (ax4-bx3)*(by3-ay4)
        elif internalPoint[0]==bx4 and internalPoint[1]==by4:
            return areaSum - (bx4-ax3)*(ay3-by4)
    
    internalPoint1 = internalPoints.pop()
    internalPoint2 = internalPoints.pop()

    if internalPoint1[0]==internalPoint2[0] and internalPoint1[0]==bx1:
        return areaSum - (ax2-bx1)*(by3-by1)
    if internalPoint1[0]==internalPoint2[0] and internalPoint1[0]==bx2:
        return areaSum - (bx2-ax1)*(by2-by4)
    if internalPoint1[1]==internalPoint2[1] and internalPoint1[1]==by1:
        return areaSum - (bx4-bx1)*(ay2-by1)
    if internalPoint1[1]==internalPoint2[1] and internalPoint1[1]==by2:
        return areaSum - (bx2-bx3)*(by2-ay1)
    print( areaSum - (bx2-bx1)*(by2-by1))
    return areaSum - (bx2-bx1)*(by2-by1)

print(computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))





def smartCompute(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    overlapWidth = min(ax2,bx2) - max(ax1,bx1)
    overlapHeight = min(ay2,by2) - max(ay1,by1)
    sumOfRectangleAreas = abs(ax1-ax2)*abs(ay1-ay2) + abs(bx1-bx2)*abs(by1-by2)
    if overlapWidth>0 and overlapHeight>0:
        return sumOfRectangleAreas - overlapWidth*overlapHeight
    return sumOfRectangleAreas