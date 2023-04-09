class Solution:
    def minDays(self, grid) -> int:
        m, n = len(grid), len(grid[0])

        visited = set()
        def dfs(i, j):
            nonlocal visited
            visited.add((i,j))
            for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                neighI, neighJ = i+di, j+dj
                if 0<=neighI<m and 0<=neighJ<n and (neighI, neighJ) not in visited and grid[neighI][neighJ]==1:
                    dfs(neighI, neighJ)

        numComponents = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in visited:
                    numComponents+=1
                    dfs(i,j)

        if len(visited)==0 or len(visited)==1: return len(visited)
        if numComponents!=1: return 0
        if len(visited)==2: return 2
        cutVertexSet = set()
        lowMatrix, timeOfVisitMatrix, time = [[1e9 for _ in range(n)] for _ in range(m)], [[1e9 for _ in range(n)] for _ in range(m)], 1
        def tarjansAlgoForArticulationPoints(i, j, parentI, parentJ):
            nonlocal lowMatrix, timeOfVisitMatrix, time, cutVertexSet
            lowMatrix[i][j] = time
            timeOfVisitMatrix[i][j] = time
            time+=1
            childComponentCount = 0
            for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                neighI, neighJ = i+di, j+dj
                if 0<=neighI<m and 0<=neighJ<n and grid[neighI][neighJ]==1:
                    if (neighI, neighJ)==(parentI, parentJ): continue
                    if lowMatrix[neighI][neighJ]==1e9:
                        tarjansAlgoForArticulationPoints(neighI, neighJ, i, j)
                        lowMatrix[i][j] = min(lowMatrix[i][j], lowMatrix[neighI][neighJ])
                        if lowMatrix[neighI][neighJ] >= timeOfVisitMatrix[i][j] and (parentI, parentJ)!=(-1,-1):
                            cutVertexSet.add((i,j))
                        childComponentCount += 1
                    else:
                        lowMatrix[i][j] = min(lowMatrix[i][j], timeOfVisitMatrix[neighI][neighJ])
            if childComponentCount>1 and (parentI, parentJ)==(-1,-1):
                cutVertexSet.add((i,j))



        i, j = visited.pop()
        tarjansAlgoForArticulationPoints(i, j, -1, -1)

        return 1 if cutVertexSet else 2
        
'''
Changes wrt bridge
1. parent is not processed at all
2. if visited is the neigh -> use low[node] = min(low[node], timeVisited[neigh])  ----  visited may have updated its low but that visited node itself might be an articulation point
3. cut vertex condition changes from low[neigh]>time[node] to low[neigh]>=time[node] and parent!=-1   ----  nodes in the child component should reach someone before me. jsut reaching me(= case) if not sufficient as I may be removed
4. childComponentCount>1 and isRoot (parent==-1) then cut vertex   ----  root node is handled separately

'''
 


