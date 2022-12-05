import copy
import heapq
import numpy as np

class TrappingWaterProblemSolver():
    def __init__(self, buildingHeights):
        self.buildingHeights = buildingHeights
        self.waterLevelsArr = [None for x in self.buildingHeights]

    def printWaterLevelsSum(self):
        sumOfWaterLevels = sum(filter(None,self.waterLevelsArr))
        print(sumOfWaterLevels)
        
    def printWaterLevelsArr(self):
        print(self.waterLevelsArr)

    def printBuildings(self):
        maxHeight = max(self.buildingHeights)
        for level in range(maxHeight+1, 0, -1):
            for arrElem in self.buildingHeights:
                if(arrElem>=level):
                    print("||", end="")
                elif(arrElem+1 == level):
                    print("__", end="")
                else:
                    print("  ",end="")
            print("")
    
    
    def printBuildingsAndWater(self):
        waterLevelsArrCopy = copy.deepcopy(self.waterLevelsArr)
        maxHeight = max(self.buildingHeights)
        for level in range(maxHeight+1, 0, -1):
            for i in range(0,len(self.buildingHeights)):
                arrElem = self.buildingHeights[i]
                if(arrElem>=level):
                    print("||", end="")
                elif(waterLevelsArrCopy[i] and waterLevelsArrCopy[i]>0 and level==waterLevelsArrCopy[i]+arrElem):
                    print("--", end="")
                    waterLevelsArrCopy[i] = waterLevelsArrCopy[i] - 1
                elif(arrElem+1 == level):
                    print("__", end="")
                else:
                    print("  ",end="")
            print("")
        if(sum(filter(None,waterLevelsArrCopy))!=0):
           print("something is wrong")


#Doesnt work properly in case of duplicate heights as heapsort is not stable
# O(nlogn) since heap pop takes logn n
class TrappingWaterProblemSolverWithHeap(TrappingWaterProblemSolver):
    
    def __init__(self, buildingHeights):
        super().__init__(buildingHeights)
        
    
    def assignWaterLevels(self, currentTallBuildingHeight, indexOfCurrentTallBuilding, indexOfPreviousTallBuilding):
        if(indexOfCurrentTallBuilding>indexOfPreviousTallBuilding):
            #iterate left
            for buildingIndex in range(indexOfCurrentTallBuilding-1,indexOfPreviousTallBuilding,-1):
                #iterate only is the buildings are smaller than the current tall building
                if(self.buildingHeights[buildingIndex]<self.buildingHeights[indexOfCurrentTallBuilding]):
                    self.waterLevelsArr[buildingIndex] = currentTallBuildingHeight - self.buildingHeights[buildingIndex]
                else:
                    return
        else:
            #iterate right
            for buildingIndex in range(indexOfCurrentTallBuilding+1,indexOfPreviousTallBuilding,1):
                #iterate only is the buildings are smaller than the current tall building
                if(self.buildingHeights[buildingIndex]<self.buildingHeights[indexOfCurrentTallBuilding]):
                    self.waterLevelsArr[buildingIndex] = currentTallBuildingHeight - self.buildingHeights[buildingIndex]
                else:
                    return
    
    def solve(self):
        
        arrOfBuildingHeightsAndTheirIndexTuple = list(enumerate(self.buildingHeights))
        #negative height as heapq only implements min heap
        arrOfBuildingHeightsAndTheirIndexTuple = [((-tup[1],tup[0])) for tup in arrOfBuildingHeightsAndTheirIndexTuple]
        heapq.heapify(arrOfBuildingHeightsAndTheirIndexTuple)
        
        #print(arrOfBuildingHeightsAndTheirIndexTuple)
        prevTallBuildingIndex = arrOfBuildingHeightsAndTheirIndexTuple[0][1]
        if(arrOfBuildingHeightsAndTheirIndexTuple[0][0]!=arrOfBuildingHeightsAndTheirIndexTuple[1][0]):
            prevTallBuildingTuple = heapq.heappop(arrOfBuildingHeightsAndTheirIndexTuple)
            prevTallBuildingIndex = prevTallBuildingTuple[1]
        while(len(arrOfBuildingHeightsAndTheirIndexTuple)>0):
            stackOfSameHeightBuildings = []
            
            currentTallBuildingTuple = heapq.heappop(arrOfBuildingHeightsAndTheirIndexTuple)
            stackOfSameHeightBuildings.append(currentTallBuildingTuple)
            
            minIndexOfCurrentHeightBuildings = 10000000
            while(len(arrOfBuildingHeightsAndTheirIndexTuple)>0 and arrOfBuildingHeightsAndTheirIndexTuple[0][0]==currentTallBuildingTuple[0]):
                currentTallBuildingTuple = heapq.heappop(arrOfBuildingHeightsAndTheirIndexTuple)
                stackOfSameHeightBuildings.append(currentTallBuildingTuple)
                minIndexOfCurrentHeightBuildings = min(minIndexOfCurrentHeightBuildings,currentTallBuildingTuple[0])
            
            if(prevTallBuildingIndex<minIndexOfCurrentHeightBuildings):
                stackOfSameHeightBuildings.reverse()
            
            while(len(stackOfSameHeightBuildings)>0):
                currentTallBuildingTuple = stackOfSameHeightBuildings.pop()
                currentTallBuildingIndex = currentTallBuildingTuple[1]
                currentTallBuildingHeight = -currentTallBuildingTuple[0]
                
                '''
                print("------------------")
                print(waterLevelsArr)
                print(buildingHeights)
                print(currentTallBuildingHeight)
                print(currentTallBuildingIndex)
                print(prevTallBuildingIndex)
                print("------------------")
                '''
                
                if(self.waterLevelsArr[currentTallBuildingIndex]==None):
                    self.assignWaterLevels(currentTallBuildingHeight, currentTallBuildingIndex, prevTallBuildingIndex)
                    if(prevTallBuildingIndex-currentTallBuildingIndex):
                        prevTallBuildingIndex = currentTallBuildingIndex
    
   


class TrappingWaterProblemSolverWithLeftMaxRightMaxTechnique(TrappingWaterProblemSolver):
    
    def __init__(self, buildingHeights):
        super().__init__(buildingHeights)
        self.indexOfMaxHeightBuildingOnLeft = [None] * len(buildingHeights)
        self.indexOfMaxHeightBuildingOnRight = [None] * len(buildingHeights)


        
    def fillIndexOfMaxHeightBuildingOnLeft(self):
        maxHeight = -1
        for i in range(0,len(self.buildingHeights)):
            if(self.buildingHeights[i]>=maxHeight):
                self.indexOfMaxHeightBuildingOnLeft[i] = i
                maxHeight = self.buildingHeights[i]
            else:
                self.indexOfMaxHeightBuildingOnLeft[i] = self.indexOfMaxHeightBuildingOnLeft[i-1]
    
    def fillIndexOfMaxHeightBuildingOnRight(self):
        maxHeight = -1
        for i in range(len(self.buildingHeights)-1, -1, -1):
            if(self.buildingHeights[i]>=maxHeight):
                self.indexOfMaxHeightBuildingOnRight[i] = i
                maxHeight = self.buildingHeights[i]
            else:
                self.indexOfMaxHeightBuildingOnRight[i] = self.indexOfMaxHeightBuildingOnRight[i+1]
  
    def solve(self):
        
        self.fillIndexOfMaxHeightBuildingOnLeft()
        self.fillIndexOfMaxHeightBuildingOnRight()
        
        for buildingIndex in range(0,len(self.buildingHeights)):
            if(self.indexOfMaxHeightBuildingOnRight[buildingIndex]!=buildingIndex and self.indexOfMaxHeightBuildingOnLeft[buildingIndex]!=buildingIndex):
                self.waterLevelsArr[buildingIndex] = min(self.buildingHeights[self.indexOfMaxHeightBuildingOnLeft[buildingIndex]],self.buildingHeights[self.indexOfMaxHeightBuildingOnRight[buildingIndex]]) - self.buildingHeights[buildingIndex]
   
    
# Verfied on LeetCode

class TrappingWaterProblemSolverWithTwoPointerFromLeftAndRightTechnique(TrappingWaterProblemSolver):
    
    def __init__(self, buildingHeights):
        super().__init__(buildingHeights)
        
    def solve(self):
        leftPointerIndex = 0
        rightPointerIndex = len(self.buildingHeights)-1
        
        rightMax = -1
        leftMax = -1
        
        
        while(leftPointerIndex<rightPointerIndex):
            if(self.buildingHeights[leftPointerIndex] > self.buildingHeights[rightPointerIndex]):
                #move right pointer
                rightMax = max(rightMax, self.buildingHeights[rightPointerIndex])
                self.waterLevelsArr[rightPointerIndex] = rightMax - self.buildingHeights[rightPointerIndex]
                rightPointerIndex = rightPointerIndex - 1
                
            else:
                #move left pointer
                leftMax = max(leftMax, self.buildingHeights[leftPointerIndex])
                self.waterLevelsArr[leftPointerIndex] = leftMax - self.buildingHeights[leftPointerIndex]
                leftPointerIndex = leftPointerIndex + 1
    
    
        
def trapRainWaterProblem():
    buildingHeights = np.random.randint(0,15,20)
    
    heapSolver = TrappingWaterProblemSolverWithHeap(buildingHeights)
    heapSolver.solve()
    heapSolver.printBuildings()
    heapSolver.printWaterLevelsArr()
    heapSolver.printWaterLevelsSum()
    heapSolver.printBuildingsAndWater()
    
        
    leftMaxRightMaxSolver = TrappingWaterProblemSolverWithLeftMaxRightMaxTechnique(buildingHeights)
    leftMaxRightMaxSolver.solve()
    leftMaxRightMaxSolver.printWaterLevelsArr()
    leftMaxRightMaxSolver.printWaterLevelsSum()
    leftMaxRightMaxSolver.printBuildingsAndWater()
    
    
    twoPointerSolver = TrappingWaterProblemSolverWithTwoPointerFromLeftAndRightTechnique(buildingHeights)
    twoPointerSolver.solve()
    twoPointerSolver.printWaterLevelsArr()
    twoPointerSolver.printWaterLevelsSum()
    #twoPointerSolver.printBuildingsAndWater()
    
    
    
trapRainWaterProblem() 