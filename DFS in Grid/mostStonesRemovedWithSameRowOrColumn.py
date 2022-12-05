

stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]

def findIslands(visited, stone, colMap, rowMap):
    for row in colMap[stone[0]]:
        if row!=stone[1] and (stone[0],row) not in visited:
            visited.add((stone[0],row))
            findIslands(visited,[stone[0],row], colMap, rowMap)
    for col in rowMap[stone[1]]:
        if col!=stone[0] and (col,stone[1]) not in visited:
            visited.add((col,stone[1]))
            findIslands(visited,[col,stone[1]], colMap, rowMap)



def removeStones(stones):
    colMap = {}
    rowMap = {}

    for stone in stones:
        if not stone[0] in colMap:
            colMap[stone[0]] = set()
        if not stone[1] in rowMap:
            rowMap[stone[1]] = set()
        colMap[stone[0]].add(stone[1])
        rowMap[stone[1]].add(stone[0])

    visited = set()
    numIslands = 0
    for stone in stones:
        if not (stone[0], stone[1]) in visited:
            findIslands(visited, stone, colMap, rowMap)
            numIslands += 1

    return len(stones) - numIslands

print(removeStones(stones))

