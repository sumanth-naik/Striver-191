class Solution:
    def minJumps(self, arr):
        n = len(arr)

        mapOfValueToIndices = {}
        for index, val in enumerate(arr):
            if not val in mapOfValueToIndices:
                mapOfValueToIndices[val] = set()
            mapOfValueToIndices[val].add(index)

        # levelArr stores indices
        levelArr, level, visitedSet = [0], 0, set([0])
        while True:
            nextLevelArr = []
            for index in levelArr:
                if index==n-1:
                    return level
                for di in [1,-1]:
                    if 0<=index+di<n:
                        if index+di not in visitedSet:
                            visitedSet.add(index+di)
                            nextLevelArr.append(index+di)
                if arr[index] in mapOfValueToIndices:
                    for indexWithSameNumber in mapOfValueToIndices[arr[index]]:
                        if indexWithSameNumber not in visitedSet:
                            visitedSet.add(indexWithSameNumber)
                            nextLevelArr.append(indexWithSameNumber)
                    del mapOfValueToIndices[arr[index]]
            level+=1
            levelArr = nextLevelArr
