isConnected = [[1,1,0],[1,1,0],[0,0,1]]

def markProvince(visited, isConnected, i):
    for j in range(len(isConnected)):
        if isConnected[i][j] and j not in visited:
            visited.add(j)
            markProvince(visited,isConnected,j)

def findNumProvinces(isConnected):

    visited = set()
    numProvinces = 0

    for i in range(len(isConnected)):
        if i not in visited:
            visited.add(i)
            markProvince(visited, isConnected, i)
            numProvinces += 1
    return numProvinces

print(findNumProvinces(isConnected))