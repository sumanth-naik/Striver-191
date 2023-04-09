class Solution:
    def minTime(self, n, edges, hasApple) -> int:
        childrenMap = {}
        for edge in edges:
            if not edge[0] in childrenMap:
                childrenMap[edge[0]] = []
            childrenMap[edge[0]].append(edge[1])
            if not edge[1] in childrenMap:
                childrenMap[edge[1]] = []
            childrenMap[edge[1]].append(edge[0])
            
        visited = set()
        def minTime(num):
            visited.add(num)
            totalTime = 0
            if num in childrenMap:
                for child in childrenMap[num]:
                    if child not in visited:
                        totalTime += minTime(child)
            visited.remove(num)
            return (totalTime + 2) if ((hasApple[num] or totalTime>0) and num!=0) else totalTime
        
        return minTime(0) 