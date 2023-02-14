
def possibleBipartition(n, dislikes):
    colorArr = [-1 for _ in range(n+1)]
    adjList = [[] for _ in range(n+1)]
    for dislike in dislikes:
        adjList[dislike[0]].append(dislike[1])
        adjList[dislike[1]].append(dislike[0])

    def dfsTraversal(num):
        for neighNum in adjList[num]:
            if colorArr[neighNum]!=-1 and colorArr[neighNum]==colorArr[num]:
                return False
            if colorArr[neighNum]==-1:
                colorArr[neighNum] = abs(1-colorArr[num])
                if not dfsTraversal(neighNum):
                    return False  
        return True

    for i in range(1,n+1):
        if i in range(n+1) and colorArr[i]==-1:
            colorArr[i] = 0
            if not dfsTraversal(i):
                return False
    return True