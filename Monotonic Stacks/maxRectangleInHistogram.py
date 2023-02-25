import numpy as np



def printMaxRectangle(buildingHeights, maxAreaLocation):
    maxHeight = max(buildingHeights)
    maxRectangleHeight = buildingHeights[maxAreaLocation[1]]
    for level in range(maxHeight+1, 0, -1):
        for i in range(0,len(buildingHeights)):
            arrElem = buildingHeights[i]
            if(level<=maxRectangleHeight):
                if(i>maxAreaLocation[0] and i<maxAreaLocation[2]):
                    print("--", end="")
                    continue
            if(arrElem>=level):
                print("||", end="")
            elif(arrElem+1 == level):
                print("__", end="")
            else:
                print("  ",end="")
        print("")

def maxRectangleinHistogramSolver(histogramArr):
    leftEndIndicesArr = getLeftEndIndices(histogramArr)
    print(leftEndIndicesArr)
    rightEndIndicesArr = getRightEndIndices(histogramArr)
    print(rightEndIndicesArr)
    maxRectangle = -1
    maxAreaLocation = (-1,-1,-1)
    for i in range(0, len(histogramArr)):
        area = histogramArr[i] * (abs(leftEndIndicesArr[i] - rightEndIndicesArr[i])-1)
        if(max(maxRectangle, area) != maxRectangle):
            maxRectangle = max(maxRectangle, area)
            maxAreaLocation = (leftEndIndicesArr[i], i , rightEndIndicesArr[i])
    print(maxRectangle)
    printMaxRectangle(histogramArr, maxAreaLocation)
    
def getLeftEndIndices(histogramArr):
    stack = [0]
    leftEndIndicesArr = [-1] * len(histogramArr)
    for index in range(1,len(histogramArr)):
        currentHeight = histogramArr[index]
        while(len(stack)>0 and currentHeight<=histogramArr[stack[len(stack)-1]]):
            stack.pop()
        if(len(stack)==0):
            leftEndIndicesArr[index] = -1
        else:
            leftEndIndicesArr[index] = stack[len(stack)-1]
        stack.append(index)
    return leftEndIndicesArr

    
def getRightEndIndices(histogramArr):
    stack = [len(histogramArr)-1]
    rightEndIndicesArr = [len(histogramArr)] * len(histogramArr)
    for index in range(len(histogramArr)-2,-1,-1):
        currentHeight = histogramArr[index]
        while(len(stack)>0 and currentHeight<=histogramArr[stack[len(stack)-1]]):
            stack.pop()
        if(len(stack)==0):
            rightEndIndicesArr[index] = len(histogramArr)
        else:
            rightEndIndicesArr[index] = stack[len(stack)-1]
        stack.append(index)
    return rightEndIndicesArr


def printBuildings(buildingHeights):
    maxHeight = max(buildingHeights)
    for level in range(maxHeight+1, 0, -1):
        for arrElem in buildingHeights:
            if(arrElem>=level):
                print("||", end="")
            elif(arrElem+1 == level):
                print("__", end="")
            else:
                print("  ",end="")
        print("")
        
        
        
        
        
# Verfified on LeetCode that its working

def maxRectangleinHistogramSinglePassSolver(histogramArr):
    maxRectangleArea = -1
    n = len(histogramArr)
    stack = [-1]
    for index in range(0,n):
        if(len(stack) == 1 or histogramArr[index] > histogramArr[stack[len(stack)-1]]):
            stack.append(index)
        else:
            while(len(stack)>1 and histogramArr[index] < histogramArr[stack[len(stack)-1]]):
                poppedIndex = stack.pop()
                #index is right boundary (non inclusive) of poppedIndex Building
                #stack.top() is the left boundary
                poppedIndexRectangleArea = (index - stack[len(stack) - 1] - 1) * histogramArr[poppedIndex]
                maxRectangleArea = max(maxRectangleArea, poppedIndexRectangleArea)
            stack.append(index)
                
    while(len(stack)>1):
        poppedIndex = stack.pop()
        #index is right boundary (non inclusive) of poppedIndex Building
        #stack.top() is the left boundary
        poppedIndexRectangleArea = (n - stack[len(stack) - 1] - 1) * histogramArr[poppedIndex]
        maxRectangleArea = max(maxRectangleArea, poppedIndexRectangleArea)
        
    print(maxRectangleArea)
        



histogramArr = np.random.randint(0, 10, 10)
printBuildings(histogramArr)
maxRectangleinHistogramSolver(histogramArr)
maxRectangleinHistogramSinglePassSolver(histogramArr)



















