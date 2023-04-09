# Kosaraju, Tarjan Algos
# SCC, Articulation points and Bridges codes
class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, n, adjList):
        
        revAdjList = [[] for _ in range(n)]
        for node in range(n):
            for neigh in adjList[node]:
                revAdjList[neigh].append(node)

        stack = []
        visited = set()
        def dfs(node):
            nonlocal visited
            visited.add(node)
            for neigh in adjList[node]:
                if neigh not in visited:
                    dfs(neigh)
            stack.append(node)
        
        for node in range(n):
            if node not in visited:
                dfs(node)
        
        visited2 = set()
        def dfs2(node):
            nonlocal visited2
            visited2.add(node)
            for neigh in revAdjList[node]:
                if neigh not in visited2:
                    dfs2(neigh)

        numStronglyConnectedComponents = 0
        for node in reversed(stack):
            if node not in visited2:
                dfs2(node)
                numStronglyConnectedComponents += 1
        
        return numStronglyConnectedComponents
    


    #Function to find list of all strongly connected components in the graph.
    def kosaraju(self, n, adjList):
        
        revAdjList = [[] for _ in range(n)]
        for node in range(n):
            for neigh in adjList[node]:
                revAdjList[neigh].append(node)

        stack = []
        visited = set()
        def dfs(node):
            nonlocal visited
            visited.add(node)
            for neigh in adjList[node]:
                if neigh not in visited:
                    dfs(neigh)
            stack.append(node)
        
        for node in range(n):
            if node not in visited:
                dfs(node)
        
        visited2 = set()
        def dfs2(node, componentNodes):
            nonlocal visited2
            visited2.add(node)
            componentNodes.add(node)
            for neigh in revAdjList[node]:
                if neigh not in visited2:
                    dfs2(neigh, componentNodes)
            return componentNodes
        
        listOfStronglyConnectedComponents = []
        for node in reversed(stack):
            if node not in visited2:
                listOfStronglyConnectedComponents.append(sorted(dfs2(node, set())))
        
        return sorted(listOfStronglyConnectedComponents)
    
    #Function to find list of all strongly connected components in the graph.
    def tarjans(self, n, adjList):

        lowArr, timeOfVisitArr, time = [1e9 for _ in range(n)], [1e9 for _ in range(n)], 0
        stack, inStack, listOfStronglyConnectedComponents = [], [False for _ in range(n)], []

        def dfs(node):
            nonlocal lowArr, timeOfVisitArr, time, stack, listOfStronglyConnectedComponents
            lowArr[node] = time
            timeOfVisitArr[node] = time
            time += 1

            stack.append(node)
            inStack[node] = True

            for neigh in adjList[node]:
                if lowArr[neigh]==1e9:
                    dfs(neigh)
                # only take min if it can be from same SCC 
                # it can happen that we found some SCC in the dfs in future and we should not 
                # allow back edges to that SCC
                if inStack[neigh]:
                    lowArr[node] = min(lowArr[node], lowArr[neigh])

            # only the head node of SCC will have this True as others will have low pointing to head's low or some node in the SCC
            # And, the stack will be having all the nodes of SCC as head will be the first one to get into stack
            if lowArr[node]==timeOfVisitArr[node]:
                while True:
                    componentNode = stack.pop()
                    inStack[componentNode] = False
                    # all lowArr equal elements belong to same SCC
                    # we have to do this because there could be few nodes like doubly linked list and the last node will 
                    # not have the real low value
                    # Ex: 0<=>1<=>2       - 2 will never get lowTime[0]'s values... so any SCC nodes other side of any cut vertex will be problematic
                    lowArr[componentNode] = lowArr[node]
                    if componentNode==node: break

        for node in range(n):
            if lowArr[node]==1e9: dfs(node)

        mapOfComponents = defaultdict(list)
        for node, componentIndex in enumerate(lowArr):  
            mapOfComponents[componentIndex].append(node)
        for stronglyConnectedComponentNodes in mapOfComponents.values():
            listOfStronglyConnectedComponents.append(sorted(stronglyConnectedComponentNodes))
        return sorted(listOfStronglyConnectedComponents)
    






    def cutVertex(n, adjList):
        lowArr, timeOfVisitArr, time, cutVertexSet = [1e9 for _ in range(n)], [1e9 for _ in range(n)], 0, set()
        def tarjansAlgoForArticulationPoints(node, parent):
            nonlocal lowArr, timeOfVisitArr, time, cutVertexSet
            lowArr[node] = time
            timeOfVisitArr[node] = time
            time+=1

            childComponentCount = 0
            for neigh in adjList[node]:
                if neigh==parent: continue
                if lowArr[neigh]==1e9:
                    tarjansAlgoForArticulationPoints(neigh, node)
                    lowArr[node] = min(lowArr[node], lowArr[neigh])
                    # root of DFS needs special attention. Maintain childComponentCount for that
                    # >= since even if this node is visitable from different ways, once this vertex is deleted, it will increase num components
                    if lowArr[neigh] >= timeOfVisitArr[node] and parent!=-1:
                        cutVertexSet.add(node)
                    childComponentCount += 1
                else:
                    # if the neigh itself is cut vertex then we can not use its low as its low could have been something smaller
                    # and we would never reach that smaller one from node if neigh is deleted
                    lowArr[node] = min(lowArr[node], timeOfVisitArr[neigh])

            if childComponentCount>1 and parent==-1:
                cutVertexSet.add(node)
            
        for node in range(n):
            if lowArr[node]==1e9: tarjansAlgoForArticulationPoints(node, -1)






    def cutEdge(n, adjList):
        lowArr, timeOfVisitArr, time, cutEdgeSet = [1e9 for _ in range(n)], [1e9 for _ in range(n)], 0, set()
        def tarjansAlgoForBridges(node, parent):
            nonlocal lowArr, timeOfVisitArr, time, cutEdgeSet
            lowArr[node] = time
            timeOfVisitArr[node] = time
            time+=1

            for neigh in adjList[node]:
                # if we dont do this, then the child will have same low as parent and it will cause issue when using strictly > for comparison
                if neigh==parent: continue
                if lowArr[neigh]==1e9:
                    tarjansAlgoForBridges(neigh, node)
                    if lowArr[neigh] > timeOfVisitArr[node]:
                        cutEdgeSet.add(node)
                lowArr[node] = min(lowArr[node], lowArr[neigh])

        for node in range(n):
            if lowArr[node]==1e9: tarjansAlgoForBridges(node, -1)

