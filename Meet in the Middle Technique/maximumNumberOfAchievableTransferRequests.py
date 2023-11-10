class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        adjList = defaultdict(list)
        for u, v in requests:
            adjList[u].append(v)

        def getCycle(node, visited, path):
            path.append(node)
            if node in visited:
                return True, node
            visited.add(node)
            for neigh in adjList[node]:
                hasCycle, startNodeOfCycle = getCycle(neigh, visited, path)
                if hasCycle: return True, startNodeOfCycle
            path.pop()
            # forgot to remove
            visited.discard(node)
            return False, None
    
        possibleStartPoints, numProcessedRequests = range(n), 0
        while possibleStartPoints:
            nextStartPoints = []
            for node in possibleStartPoints:
                path = []
                hasCycle, startNodeOfCycle = getCycle(node, set(), path)
                if hasCycle:
                    path = path[path.index(startNodeOfCycle):]
                    numProcessedRequests += (len(path)-1)
                    for index in range(len(path)-1):
                        adjList[path[index]].remove(path[index+1])
                    nextStartPoints.append(node)
            possibleStartPoints = nextStartPoints
        return numProcessedRequests


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        maxRequests, m = 0, len(requests)
        for mask in range(1<<m):
            degreesArr, numRequests = [0 for _ in range(n)], 0 
            for index in range(m):
                if (1<<index)&mask:
                    numRequests += 1
                    degreesArr[requests[index][0]]-=1
                    degreesArr[requests[index][1]]+=1
            if all(degree==0 for degree in degreesArr): maxRequests = max(maxRequests, numRequests)
        return maxRequests

# TODO - MEET IN THE MIDDLE - https://leetcode.com/submissions/detail/984116227/