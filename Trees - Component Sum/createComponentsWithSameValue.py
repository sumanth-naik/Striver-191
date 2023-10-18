class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:

        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def canCut(node, parent, neededSum):
            currSum = nums[node]
            for neigh in adjList[node]:
                if neigh!=parent: 
                    currSum += canCut(neigh, node, neededSum)
            return 0 if currSum==neededSum else currSum
        
        sumNums = sum(nums)
        for componentSum in range(max(nums), sumNums//2+1):
            if sumNums%componentSum==0 and canCut(0, -1, componentSum)==0:
                return sumNums//componentSum - 1
        return 0


class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:

        indegreeArr, adjList = [0 for _ in range(len(nums))], defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            indegreeArr[u] += 1
            indegreeArr[v] += 1

        leaves = [node for node in range(len(nums)) if indegreeArr[node]==1]

        def bfsCanCut(neededSum):
            indegreeArrCopy, values = indegreeArr[:], nums[:]
            queue = deque(leaves[:])

            while queue:
                node = queue.popleft()
                if values[node]>neededSum: 
                    return False
                for neigh in adjList[node]:
                    if indegreeArrCopy[neigh]!=1:
                        indegreeArrCopy[neigh] -= 1
                        if values[node]<neededSum: 
                            values[neigh] += values[node]
                        if indegreeArrCopy[neigh]==1:
                            queue.append(neigh)
                        break
            return True

        sumNums = sum(nums)
        for componentSum in range(max(nums), sumNums//2+1):
            if sumNums%componentSum==0 and bfsCanCut(componentSum):
                return sumNums//componentSum - 1
        return 0