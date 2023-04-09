class Solution:
    def maximumScore(self, scores, edges):

        adjList = [[] for _ in range(len(scores))]
        for u,v in edges:
            adjList[u].append((scores[v], v))
            adjList[v].append((scores[u], u))

        for index in range(len(scores)):
            adjList[index] = [v for score,v in nlargest(3, adjList[index])]

        maxScore = -1
        for u,v in edges:
            def getMaxWithThisEdge(u, v, uIndex, vIndex):
                while uIndex<len(adjList[u]) and vIndex<len(adjList[v]):
                    if adjList[u][uIndex] in [u,v]:
                        uIndex += 1
                    elif adjList[v][vIndex] in [u,v]:
                        vIndex += 1
                    elif adjList[u][uIndex]==adjList[v][vIndex]:
                        return max(getMaxWithThisEdge(u, v, uIndex+1, vIndex), getMaxWithThisEdge(u, v, uIndex, vIndex+1))
                    else:
                        return scores[adjList[u][uIndex]] + scores[adjList[v][vIndex]] + scores[u] + scores[v]
                return -1
            maxScore = max(maxScore, getMaxWithThisEdge(u, v, 0, 0))
        
        return maxScore