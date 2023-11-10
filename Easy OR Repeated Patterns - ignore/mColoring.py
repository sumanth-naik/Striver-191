''' Leetcode adjList style to give the path that we know exists '''

n = 3
paths = [[1,2],[2,3],[3,1]]

def createAdjList(paths, n):
    adjList = [[] for i in range(0, n+1)]
    for edge in paths:
        adjList[edge[0]].append(edge[1])
        adjList[edge[1]].append(edge[0])
    return adjList
        
print(createAdjList(paths, n))


def isValidColoring(index, color, adjList, colorArr):
    for neigh in adjList[index]:
        if(colorArr[neigh] == color):
            return False
    return True

def mColoring(index, n, adjList, colorArr):
    if(index==n+1):
        return True
    
    for color in range(1, 5):
        if(isValidColoring(index, color, adjList, colorArr)):
            colorArr[index] = color
            if mColoring(index+1, n, adjList, colorArr): return True
            colorArr[index] = -1
            
    return False

colorArr = [-1 for i in range(0, n+1)]
mColoring(1, n, createAdjList(paths, n), colorArr)
print(colorArr[1:])






'''GFG Matrix style to check if path exixts'''

print(".....")

n = 3

graph = [[0, 1, 1],
         [1, 0, 1],
         [1, 1, 0]]

def isValidColoringMatrix(index, color, graph, colorArr):
    for i in range(0, len(graph)):
        if(graph[index][i] ==1 and colorArr[i] == color):
            return False
    return True

def mColoringMatrix(vertex, n, graph, colorArr, m):
    if(vertex==n+1):
        return 1
    
    for color in range(1, m+1):
        if(isValidColoringMatrix(vertex-1, color, graph, colorArr)):
            colorArr[vertex-1] = color
            if(mColoringMatrix(vertex+1, n, graph, colorArr, m)==1):
                return 1
            colorArr[vertex-1] = -1
            
    return 0

colorArr = [-1 for i in range(0, n)]
m = 3
print(mColoringMatrix(1, n, graph, colorArr, m))
print(colorArr)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    