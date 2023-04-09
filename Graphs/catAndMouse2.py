from collections import deque
class Solution:
    def canMouseWin(self, grid, catJump: int, mouseJump: int) -> bool:
        catJump += 1
        mouseJump += 1
        m, n = len(grid), len(grid[0])
        # decision tree Node = (mousePositionInGrid, catPositionInGrid, turn) -> winner
        queue = deque()
        visitedDecisionTreeNodes = set()
        foodIndex = None
        mouseIndex = None
        catIndex = None
        MOUSE, CAT = 0, 1
        for i in range(m):
            for j in range(n):
                # wall
                if grid[i][j]=="#":
                    continue
                if grid[i][j]=="F":
                    foodIndex = (i,j)
                    continue
                if grid[i][j]=="M":
                    mouseIndex = (i,j)
                if grid[i][j]=="C":
                    catIndex = (i,j)
                queue.append(((i,j), (i,j), CAT, CAT))
                queue.append(((i,j), (i,j), MOUSE, CAT))
                visitedDecisionTreeNodes.add(((i,j), (i,j), CAT))
                visitedDecisionTreeNodes.add(((i,j), (i,j), MOUSE))

        for i in range(m):
            for j in range(n):
                if grid[i][j]!="#":      
                    queue.append(((i,j), foodIndex, CAT, CAT))         
                    queue.append(((i,j), foodIndex, MOUSE, CAT))    
                    queue.append((foodIndex, (i,j), CAT, MOUSE))         
                    queue.append((foodIndex, (i,j), MOUSE, MOUSE))
                    visitedDecisionTreeNodes.add(((i,j), foodIndex, CAT))
                    visitedDecisionTreeNodes.add(((i,j), foodIndex, MOUSE))    
                    visitedDecisionTreeNodes.add((foodIndex, (i,j), CAT))         
                    visitedDecisionTreeNodes.add((foodIndex, (i,j), MOUSE))

                      
        # outdegree arr for nodes in decsion tree
        outDegreeMap = {}
        for mouse1 in range(m):
            for mouse2 in range(n):
                if not grid[mouse1][mouse2]=="#":
                    for cat1 in range(m):
                        for cat2 in range(n):
                            if not grid[cat1][cat2]=="#":
                                for k in range(2):
                                    if not ((mouse1,mouse2), (cat1,cat2), k) in outDegreeMap:
                                        outDegreeMap[((mouse1,mouse2), (cat1,cat2), k)] = 0
                                # mouse jumps
                                for mult in (1, -1):
                                    # down, up jump
                                    for di in range(mouseJump):
                                        if 0<=mouse1+mult*di<m:
                                            if grid[mouse1+mult*di][mouse2]=="#":
                                                break
                                            outDegreeMap[((mouse1,mouse2), (cat1,cat2), 0)] += 1

                                    # right, left jump
                                    for dj in range(mouseJump):
                                        if 0<=mouse2+mult*dj<n:
                                            if grid[mouse1][mouse2+mult*dj]=="#":
                                                break
                                            outDegreeMap[((mouse1,mouse2), (cat1,cat2), 0)] += 1
                        
                                # cat jumps
                                for mult in (1, -1):
                                    # down, up jump
                                    for di in range(catJump):
                                        if 0<=cat1+mult*di<m:
                                            if grid[cat1+mult*di][cat2]=="#":
                                                break
                                            outDegreeMap[((mouse1,mouse2), (cat1,cat2), 1)] += 1
                                            if (cat1+mult*di, cat2)==(mouse1, mouse2):
                                                break

                                    # right, left jump
                                    for dj in range(catJump):
                                        if 0<=cat2+mult*dj<n:
                                            if grid[cat1][cat2+mult*dj]=="#":
                                                break
                                            outDegreeMap[((mouse1,mouse2), (cat1,cat2), 1)] += 1  
                                            if (cat1, cat2+mult*dj)==(mouse1, mouse2):
                                                break          

        while queue:
            mousePositionInGrid, catPositionInGrid, turn, winner = queue.popleft()

            if grid[mousePositionInGrid[0]][mousePositionInGrid[1]]=="M" and grid[catPositionInGrid[0]][catPositionInGrid[1]]=="C" and turn==MOUSE:
                return True if winner==MOUSE else False

            if turn==MOUSE:
                # find cat moves which can lead to this state
                for mult in (1,-1):
                    for i in range(catJump):
                        parentNodeCatPosition = (catPositionInGrid[0]+mult*i, catPositionInGrid[1])
                        if 0<=parentNodeCatPosition[0]<m:
                            # cat cant jump over wall and mouse
                            if grid[parentNodeCatPosition[0]][parentNodeCatPosition[1]]=="#" or parentNodeCatPosition==mousePositionInGrid:
                                break
                            if not (mousePositionInGrid, parentNodeCatPosition, CAT) in visitedDecisionTreeNodes:
                                if winner==CAT:
                                    visitedDecisionTreeNodes.add((mousePositionInGrid, parentNodeCatPosition, CAT))
                                    queue.append((mousePositionInGrid, parentNodeCatPosition, CAT, CAT))
                                else:
                                    outDegreeMap[(mousePositionInGrid, parentNodeCatPosition, CAT)] -= 1
                                    if outDegreeMap[(mousePositionInGrid, parentNodeCatPosition, CAT)] == 0:
                                        visitedDecisionTreeNodes.add((mousePositionInGrid, parentNodeCatPosition, CAT))
                                        queue.append((mousePositionInGrid, parentNodeCatPosition, CAT, MOUSE))

                    for j in range(catJump):
                        parentNodeCatPosition = (catPositionInGrid[0], catPositionInGrid[1]+mult*j)
                        if 0<=parentNodeCatPosition[1]<n:
                            # cat cant jump over wall and mouse
                            if grid[parentNodeCatPosition[0]][parentNodeCatPosition[1]]=="#" or parentNodeCatPosition==mousePositionInGrid:
                                break
                            if not (mousePositionInGrid, parentNodeCatPosition, CAT) in visitedDecisionTreeNodes:
                                if winner==CAT:
                                    visitedDecisionTreeNodes.add((mousePositionInGrid, parentNodeCatPosition, CAT))
                                    queue.append((mousePositionInGrid, parentNodeCatPosition, CAT, CAT))
                                else:
                                    outDegreeMap[(mousePositionInGrid, parentNodeCatPosition, CAT)] -= 1
                                    if outDegreeMap[(mousePositionInGrid, parentNodeCatPosition, CAT)] == 0:
                                        visitedDecisionTreeNodes.add((mousePositionInGrid, parentNodeCatPosition, CAT))
                                        queue.append((mousePositionInGrid, parentNodeCatPosition, CAT, MOUSE))

            if turn==CAT:
                # find mouse moves which can lead to this state
                for mult in (1,-1):
                    for i in range(mouseJump):
                        parentNodeMousePosition = (mousePositionInGrid[0]+mult*i, mousePositionInGrid[1])
                        if 0<=parentNodeMousePosition[0]<m:
                            # mouse cant jump over wall
                            if grid[parentNodeMousePosition[0]][parentNodeMousePosition[1]]=="#":
                                break
                            if not (parentNodeMousePosition, catPositionInGrid, MOUSE) in visitedDecisionTreeNodes:
                                if winner==MOUSE:
                                    visitedDecisionTreeNodes.add((parentNodeMousePosition, catPositionInGrid, MOUSE))
                                    queue.append((parentNodeMousePosition, catPositionInGrid, MOUSE, MOUSE))
                                else:
                                    outDegreeMap[(parentNodeMousePosition, catPositionInGrid, MOUSE)] -= 1
                                    if outDegreeMap[(parentNodeMousePosition, catPositionInGrid, MOUSE)] == 0:
                                        visitedDecisionTreeNodes.add((parentNodeMousePosition, catPositionInGrid, MOUSE))
                                        queue.append((parentNodeMousePosition, catPositionInGrid, MOUSE, CAT))

                    for j in range(mouseJump):
                        parentNodeMousePosition = (mousePositionInGrid[0], mousePositionInGrid[1]+mult*j)
                        if 0<=parentNodeMousePosition[1]<n:
                            # mouse cant jump over wall
                            if grid[parentNodeMousePosition[0]][parentNodeMousePosition[1]]=="#":
                                break
                            if not (parentNodeMousePosition, catPositionInGrid, MOUSE) in visitedDecisionTreeNodes:
                                if winner==MOUSE:
                                    visitedDecisionTreeNodes.add((parentNodeMousePosition, catPositionInGrid, MOUSE))
                                    queue.append((parentNodeMousePosition, catPositionInGrid, MOUSE, MOUSE))
                                else:
                                    outDegreeMap[(parentNodeMousePosition, catPositionInGrid, MOUSE)] -= 1
                                    if outDegreeMap[(parentNodeMousePosition, catPositionInGrid, MOUSE)] == 0:
                                        visitedDecisionTreeNodes.add((parentNodeMousePosition, catPositionInGrid, MOUSE))
                                        queue.append((parentNodeMousePosition, catPositionInGrid, MOUSE, CAT))
        
                                        
                                        
        def mouseCanReachFood(mouseI, mouseJ, visitedSet):
            if grid[mouseI][mouseJ]=="F":
                return True
            visitedSet.add((mouseI, mouseJ))
            for di, dj in [(0,1), (1,0), (-1,0), (0,-1)]:
                for size in range(1, mouseJump):
                    newI, newJ = mouseI+size*di, mouseJ+size*dj
                    if 0<=newI<m and 0<=newJ<n:
                        if grid[newI][newJ]=="#":
                            break
                        if (newI, newJ) not in visitedSet:
                            if mouseCanReachFood(newI, newJ, visitedSet):
                                return True

        def catCanReachFood(catI, catJ, visitedSet):
            if grid[catI][catJ]=="F":
                return True
            visitedSet.add((catI, catJ))
            for di, dj in [(0,1), (1,0), (-1,0), (0,-1)]:
                for size in range(1, catJump):
                    newI, newJ = catI+size*di, catJ+size*dj
                    if 0<=newI<m and 0<=newJ<n:
                        if grid[newI][newJ]=="#":
                            break
                        if (newI, newJ) not in visitedSet:
                            if catCanReachFood(newI, newJ, visitedSet):
                                return True

        return True if mouseCanReachFood(mouseIndex[0], mouseIndex[1], set()) and not catCanReachFood(catIndex[0], catIndex[1], set()) else False
    
[
        ".....M",
        "##.#.#",
        "#....#",
        ".##...",
        "...C..",
        "F.....",
        ".#..#."
        
]