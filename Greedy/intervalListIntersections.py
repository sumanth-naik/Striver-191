class Solution:
    def intervalIntersection(self, firstList, secondList):

        intersectionsList = []
        firstListIndex, secondListIndex = 0, 0

        while True:
            if firstListIndex==len(firstList) or secondListIndex==len(secondList): break
            firstListIntervalStart, firstListIntervalEnd = firstList[firstListIndex]
            secondListIntervalStart, secondListIntervalEnd = secondList[secondListIndex]

            if max(firstListIntervalStart, secondListIntervalStart)<=min(firstListIntervalEnd, secondListIntervalEnd):
                intersectionsList.append([max(firstListIntervalStart, secondListIntervalStart), min(firstListIntervalEnd, secondListIntervalEnd)])

            if firstListIntervalEnd<secondListIntervalEnd: firstListIndex+=1
            else: secondListIndex+=1

        return intersectionsList