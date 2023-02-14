import heapq
class Solution:
    def longestPath(self, parent, s):
        if len(parent)<=1: return len(parent)

        adjList = {}
        for index, num in enumerate(parent):
            if index!=0:
                if not num in adjList:
                    adjList[num] = []
                if not index in adjList:
                    adjList[index] = []
                adjList[num].append(index)
                adjList[index].append(num)
        
        longestPath = 1
        visited = set()
        def dfs(num):
            nonlocal longestPath
            visited.add(num)
            possibleBranchesLengths = []
            for neighbor in adjList[num]:
                if neighbor not in visited:
                    char, lengthOfPath = dfs(neighbor)
                    if char!=s[num]:
                        heapq.heappush(possibleBranchesLengths, -lengthOfPath)

            maxLength1, maxLength2 = 0, 0
            if possibleBranchesLengths:
                maxLength1 = -heapq.heappop(possibleBranchesLengths)
            if possibleBranchesLengths:
                maxLength2 = -heapq.heappop(possibleBranchesLengths)

            longestPath = max(longestPath, 1 + maxLength1 + maxLength2)
            return s[num], 1 + maxLength1
            
        dfs(0)
        return longestPath

                