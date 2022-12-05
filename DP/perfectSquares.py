n = 17


import math
def getSquaresTillN(n):
    squares = []   
    for i in range(1, int(math.sqrt(n))+1):
        square = i*i
        if square<=n:
            squares.append(square)
    return squares



def recursivePerfectSquares(n, squares, numUsed, dp):
    if n==0:
        return numUsed
    if dp[n][1]<=numUsed and dp[n][0]!=-1:
        return dp[n][0]
    minim = 1e9
    for square in squares:
        if square<= n and n-square>=0:
            minim = min(minim, recursivePerfectSquares(n-square, squares, numUsed+1, dp))
    dp[n] = (minim, numUsed)
    return dp[n][0]

def perfectSquares(n):
    squares = getSquaresTillN(n)
    squares.reverse()
    dp = [(-1, 1e9) for _ in range(n+1)]
    return recursivePerfectSquares(n,squares,0, dp)

print(perfectSquares(n))


def perfectSquaresIterative(n):
    squares = getSquaresTillN(n)
    dp = [1e9 for _ in range(n+1)]
    dp[0] = 0
    for i in range(1, n+1):
        for square in squares:
            if square<=i:
                dp[i] = min(dp[i], dp[i-square]+1)
            else:
                break
    return dp[n]

print(perfectSquaresIterative(n))




def perfectSquaresMath(n):
    squaresSet = set(getSquaresTillN(n))
    if n in squaresSet: 
        return 1
    for i in range(int(math.sqrt(n))+1):
        if n-i*i in squaresSet:
            return 2
    while n%4==0:
        n = n>>2
    if n%8==7:
        return 4
    return 3
#print(perfectSquaresMath(12))
for i in range(1,100):
    # print(i, perfectSquaresMath(i))
    if(perfectSquaresMath(i)!=perfectSquaresIterative(i)):
        print("wrong", i)



from collections import deque
def perfectSquaresBFS(n):
    squares = getSquaresTillN(n)

    queue = deque()
    queue.append((n,0))
    visited = set([(n,0)])
    while queue:
        elem = queue.popleft()
        num = elem[0]
        jumps = elem[1] 
        for square in squares:
            if square<=num:
                next = (num-square, jumps+1)
                if next[0]==0: return next[1]
                if next not in visited:
                    queue.append(next)
                    visited.add(next)
            else:
                break

for i in range(1,100):
    # print(i, perfectSquaresMath(i))
    mathAns = perfectSquaresMath(i)
    bfsAns = perfectSquaresBFS(i)
    if(mathAns!=bfsAns):
        print("wrong", i , " - ", mathAns, bfsAns)







