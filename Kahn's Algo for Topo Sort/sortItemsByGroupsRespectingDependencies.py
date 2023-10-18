# WA and too much complexity if we dont assign group numbers to no-group items
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        indegreeArrOfSameGroup, indegreeArrOfDiffGroup = [0 for _ in range(n)], [0 for _ in range(m)]
        groupToNodesMap = defaultdict(list)
        for node, groupNum in enumerate(group): 
            groupToNodesMap[groupNum].append(node)

        adjList = defaultdict(list)

        for node, preReqsOfNode in enumerate(beforeItems):
            for prereq in preReqsOfNode:
                adjList[prereq].append(node)
                if group[node]==group[prereq] or group[node]==-1:
                    indegreeArrOfSameGroup[node] += 1
                else:
                    indegreeArrOfDiffGroup[group[node]] += 1

        topoSortArr, queueOfNodesOfCurrentGroup, queueOfNextGroups, noGroupNodes = [], deque(), deque(), []
        for node, indegreeVal in enumerate(indegreeArrOfSameGroup):
            if indegreeVal==0:
                if group[node]==-1:
                    noGroupNodes.append(node)

        for groupNum, indegreeVal in enumerate(indegreeArrOfDiffGroup):
            if indegreeVal==0:
                queueOfNextGroups.append(groupNum)

        while queueOfNodesOfCurrentGroup or queueOfNextGroups or noGroupNodes:
            if noGroupNodes: 
                topoSortArr.append(noGroupNodes)
                continue
            if queueOfNodesOfCurrentGroup==[]:
                queueOfNodesOfCurrentGroup = groupToNodesMap[queueOfNextGroups.popleft()]
            node = queueOfNodesOfCurrentGroup.popleft()
            topoSortArr.append(node)
            if node in adjList:
                for neigh in adjList[node]:
                    if group[node]==group[neigh] or group[neigh]==-1:
                        indegreeArrOfSameGroup[neigh] -= 1
                        if indegreeArrOfSameGroup[neigh]==0:
                            if group[neigh]==-1:
                                noGroupNodes.append(neigh)
                            else:
                                queueOfNodesOfCurrentGroup.append(neigh)
                    else:
                        indegreeArrOfDiffGroup[group[neigh]] -= 1
                        if indegreeArrOfDiffGroup[group[neigh]]==0:
                            queueOfNextGroups.append(group[neigh])
        
        return topoSortArr if len(topoSortArr)==n else []

                        


# 18 min
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        itemAdjList, groupAdjList, itemIndegrees, groupIndegrees = defaultdict(list), defaultdict(list), defaultdict(int), defaultdict(int)

        groupNumber = m
        for item in range(n):
            if group[item]==-1:
                group[item] = groupNumber
                groupNumber += 1
            groupIndegrees[group[item]] = 0
            itemIndegrees[item] = 0
        
        for item, prereqs in enumerate(beforeItems):
            for prereq in prereqs:
                itemAdjList[prereq].append(item)
                itemIndegrees[item] += 1
                if group[item]!=group[prereq]:
                    groupAdjList[group[prereq]].append(group[item])
                    groupIndegrees[group[item]] += 1
        
        def topoSort(adjList, indegrees):
            topoSortArr = []
            queue = deque([node for node, indegree in indegrees.items() if indegree==0])
            while queue:
                node = queue.popleft()
                topoSortArr.append(node)
                for neigh in adjList[node]:
                    indegrees[neigh] -= 1
                    if indegrees[neigh]==0:
                        queue.append(neigh)
            return topoSortArr if len(topoSortArr)==len(indegrees) else None
        
        itemsOrder = topoSort(itemAdjList, itemIndegrees)
        if itemsOrder==None: return []
        groupsOrder = topoSort(groupAdjList, groupIndegrees)
        if groupsOrder==None: return []

        groupToItemsMap = defaultdict(list)
        for item in itemsOrder:
            groupToItemsMap[group[item]].append(item)
        
        sortedArr = []
        for groupNum in groupsOrder:
            sortedArr.extend(groupToItemsMap[groupNum])
        return sortedArr


# 18 min
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        groupNumber = m
        for item in range(n):
            if group[item]==-1:
                group[item] = groupNumber
                groupNumber += 1
                
        itemAdjList, groupAdjList, itemIndegrees, groupIndegrees = defaultdict(list), defaultdict(list), [0] * n, [0] * groupNumber

        for item, prereqs in enumerate(beforeItems):
            for prereq in prereqs:
                itemAdjList[prereq].append(item)
                itemIndegrees[item] += 1
                if group[item]!=group[prereq]:
                    groupAdjList[group[prereq]].append(group[item])
                    groupIndegrees[group[item]] += 1
        
        def topoSort(adjList, indegrees):
            topoSortArr = []
            queue = deque([node for node, indegree in enumerate(indegrees) if indegree==0])
            while queue:
                node = queue.popleft()
                topoSortArr.append(node)
                for neigh in adjList[node]:
                    indegrees[neigh] -= 1
                    if indegrees[neigh]==0:
                        queue.append(neigh)
            return topoSortArr if len(topoSortArr)==len(indegrees) else None
        
        itemsOrder = topoSort(itemAdjList, itemIndegrees)
        if itemsOrder==None: return []
        groupsOrder = topoSort(groupAdjList, groupIndegrees)
        if groupsOrder==None: return []

        groupToItemsMap = defaultdict(list)
        for item in itemsOrder:
            groupToItemsMap[group[item]].append(item)
        
        sortedArr = []
        for groupNum in groupsOrder:
            sortedArr.extend(groupToItemsMap[groupNum])
        return sortedArr




# 24 min
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        groupIncrementor = m
        adjList, groupToNodesMap = defaultdict(list), defaultdict(list)
        indegreeArrOfSameGroup, indegreeArrOfDiffGroup = defaultdict(int), {}

        for node in range(len(group)):
            if group[node]==-1:
                group[node] = groupIncrementor
                groupIncrementor += 1
            groupToNodesMap[group[node]].append(node)
            indegreeArrOfDiffGroup[group[node]] = 0
        
        for node, prereqs in enumerate(beforeItems):
            for prereq in prereqs:
                adjList[prereq].append(node)
                if group[node]==group[prereq]:
                    indegreeArrOfSameGroup[node] += 1
                else:
                    indegreeArrOfDiffGroup[group[node]] += 1
        # print(adjList, groupToNodesMap, group)
        # print(indegreeArrOfSameGroup, indegreeArrOfDiffGroup)
        queueOfCurrentGroupNodes, queueOfNextGroups, topoSortArr = deque(), deque([groupNum for groupNum, indegreeVal in indegreeArrOfDiffGroup.items() if indegreeVal==0]), []
        while queueOfCurrentGroupNodes or queueOfNextGroups:
            # print(queueOfCurrentGroupNodes, queueOfNextGroups, topoSortArr)
            if not queueOfCurrentGroupNodes:
                for groupNode in groupToNodesMap[queueOfNextGroups.popleft()]:
                    if indegreeArrOfSameGroup[groupNode]==0:
                        queueOfCurrentGroupNodes.append(groupNode)
            else:
                node = queueOfCurrentGroupNodes.popleft()
                topoSortArr.append(node)
                for neigh in adjList[node]:
                    if group[node]==group[neigh]:
                        indegreeArrOfSameGroup[neigh] -= 1
                        if indegreeArrOfSameGroup[neigh]==0:
                            queueOfCurrentGroupNodes.append(neigh)
                    else:
                        indegreeArrOfDiffGroup[group[neigh]] -= 1
                        if indegreeArrOfDiffGroup[group[neigh]]==0:
                            queueOfNextGroups.append(group[neigh])
            
        return topoSortArr if len(topoSortArr)==n else []
    
# Cleaner Version
# Time, Space -> O(|V| + |E|)
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        groupNumber, groupToItemsMap = m, defaultdict(list)
        # assign group numbers to items which are not part of any group and populate groupToItemsMap
        for item in range(len(group)):
            if group[item]==-1:
                group[item] = groupNumber
                groupNumber += 1
            groupToItemsMap[group[item]].append(item)
        
        # single adjList for entire graph. itemIndegreesArr only considers intra-group. groupIndegreesArr only considers inter-group
        adjList, itemIndegreesArr, groupIndegreesArr = defaultdict(list), [0]*n, [0]*groupNumber

        for item, prereqs in enumerate(beforeItems):
            for prereq in prereqs:
                adjList[prereq].append(item)
                if group[item]==group[prereq]:
                    itemIndegreesArr[item] += 1
                else:
                    groupIndegreesArr[group[item]] += 1 

        queueOfCurrentGroupItems, queueOfNextGroups, topoSortArr = deque(), deque([groupNum for groupNum, indegree in enumerate(groupIndegreesArr) if indegree==0]), []
        while queueOfCurrentGroupItems or queueOfNextGroups:
            if not queueOfCurrentGroupItems:
                # populate all items in the next group (popped from queueOfNextGroups) which have no indegree
                queueOfCurrentGroupItems = deque(groupItem for groupItem in groupToItemsMap[queueOfNextGroups.popleft()] if itemIndegreesArr[groupItem]==0)
            # if else is required as a cycle will lead to queueOfCurrentGroupItems having no items and the next popleft() will throw runtime-error otherwise
            else:
                # processes only one group at a time (since only same group items are added to queueOfCurrentGroupItems) -> group items in topoSortArr will be adjacent
                # but simultaneously updates groupIndegreesArr which lets us populate queueOfNextGroups
                item = queueOfCurrentGroupItems.popleft()
                topoSortArr.append(item)
                for neigh in adjList[item]:
                    if group[item]==group[neigh]:
                        itemIndegreesArr[neigh] -= 1
                        if itemIndegreesArr[neigh]==0:
                            queueOfCurrentGroupItems.append(neigh)
                    else:
                        groupIndegreesArr[group[neigh]] -= 1
                        if groupIndegreesArr[group[neigh]]==0:
                            queueOfNextGroups.append(group[neigh])
            
        return topoSortArr if len(topoSortArr)==n else []
    
# ref: https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/solutions/402945/c-with-picture-generic-topological-sort/
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        adjList, indegreesArr = defaultdict(list), defaultdict(int)

        def getGroupStartNode(node): 
            return n+group[node] if group[node]!=-1 else node
        
        def getGroupEndNode(node): 
            return n+m+group[node] if group[node]!=-1 else node

        def addEdge(u, v):
            nonlocal adjList, indegreesArr
            adjList[u].append(v)
            indegreesArr[v] += 1

        for node, prereqs in enumerate(beforeItems):
            if group[node]!=-1:
                addEdge(getGroupStartNode(node), node)
                addEdge(node, getGroupEndNode(node))
            for prereq in prereqs:
                if group[prereq]==group[node]:
                    addEdge(prereq, node) 
                else:
                    addEdge(getGroupEndNode(prereq), getGroupStartNode(node)) 
        
        def dfs(node, topoSortArr, indegreesArr):
            if node<n: topoSortArr.append(node)
            indegreesArr[node] = -1
            for neigh in adjList[node]:
                indegreesArr[neigh] -= 1 
                if indegreesArr[neigh]==0:
                    dfs(neigh, topoSortArr, indegreesArr)
        
        topoSortArr = []
        for node in range(n+2*m):
            if indegreesArr[node]==0: 
                dfs(node, topoSortArr, indegreesArr)
        
        return topoSortArr if len(topoSortArr)==n else []