import heapq
class Solution:
    def minimumTime(self, n: int, relations, time):
        # relations - 1 indexed
        # time, adjList, indegreeArr, timeAndNodeMinHeap - 0 indexed
        timePassed, adjList, timeAndNodeMinHeap, indegreeArr = 0, [[] for _ in range(n)], [], [0 for _ in range(n)]
        for prevCourse, nextCourse in relations:
            adjList[prevCourse-1].append(nextCourse-1)
            indegreeArr[nextCourse-1] += 1
        for courseNum, indegree in enumerate(indegreeArr):
            if indegree==0:
                heapq.heappush(timeAndNodeMinHeap,(time[courseNum], courseNum))
            
        while timeAndNodeMinHeap:
            timePassed, minTimeTakingCourse = heapq.heappop(timeAndNodeMinHeap)
            for neigh in adjList[minTimeTakingCourse]:
                indegreeArr[neigh] -= 1
                if indegreeArr[neigh] == 0:
                    heapq.heappush(timeAndNodeMinHeap,(time[neigh] + timePassed, neigh))
        return timePassed
    
class Solution:
    def minimumTime(self, n: int, relations, time):
        arrOfMaxTimeFromANode, adjList = [0 for _ in range(n)], [[] for _ in range(n)]
        for prevCourse, nextCourse in relations:
            adjList[prevCourse-1].append(nextCourse-1)
        
        def dfs(node):
            nonlocal arrOfMaxTimeFromANode
            if arrOfMaxTimeFromANode[node]==0:
                arrOfMaxTimeFromANode[node] = time[node] + max([dfs(neigh) for neigh in adjList[node]] + [0])
            return arrOfMaxTimeFromANode[node]
        for i in range(n):
            dfs(i) 
        return max(arrOfMaxTimeFromANode)
