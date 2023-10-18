maze = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".",".",".","+"],["+","+","+","+",".","+","."]]

entrance = [0,1]

def onBoundary(m,n,i,j):
    if i==m-1 or i==0:
        return True
    if j==n-1 or j==0:
        return True
    return False

def isValid(m,n,i,j):
    if i>m-1 or i<0:
        return False
    if j>n-1 or j<0:
        return False
    return True

from collections import deque

def nearestExitBFS(maze, entrance):

    visited = set([tuple(entrance)])
    m, n = len(maze), len(maze[0])
    queue = deque()
    queue.append((entrance[0], entrance[1], 0))

    while queue:
        elem = queue.popleft()
        i, j, length = elem[0], elem[1], elem[2]
        if length>0 and onBoundary(m,n,i,j):
            return length
        for neigh in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            if isValid(m,n,neigh[0],neigh[1]) and neigh not in visited and maze[neigh[0]][neigh[1]]=='.':
                visited.add(neigh)
                queue.append((neigh[0], neigh[1], length+1))
    return -1

print(nearestExitBFS(maze, entrance))