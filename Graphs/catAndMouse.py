class Solution:
    def catMouseGame(self, adjList):
        memo = {}

        def dfs(mouseNode, catNode, steps):

            # mouse win case
            if mouseNode==0:
                return 1
            # cat win case
            if catNode==mouseNode:
                return 2
            # draw case
            if steps==2*len(adjList):
                return 0

            if (mouseNode, catNode, steps) not in memo:
                #mouse's turn
                if not steps&1:
                    hasAPathWhichLeadsToDraw, hasAPathWhereMouseWins = False, False
                    for neigh in adjList[mouseNode]:
                        childPathAnswer = dfs(neigh, catNode, steps+1)
                        # mouse win
                        if childPathAnswer==1:
                            hasAPathWhereMouseWins = True
                            break
                        # draw
                        elif childPathAnswer==0:
                            hasAPathWhichLeadsToDraw = True

                    if hasAPathWhereMouseWins:
                        memo[(mouseNode, catNode, steps)] = 1
                    elif hasAPathWhichLeadsToDraw:
                        memo[(mouseNode, catNode, steps)] = 0
                    else:
                        memo[(mouseNode, catNode, steps)] = 2

                #cat's turn
                else:
                    hasAPathWhereCatWins, hasAPathWhichLeadsToDraw = False, False
                    for neigh in adjList[catNode]:
                        if neigh!=0:
                            childPathAnswer = dfs(mouseNode, neigh, steps+1)
                            # cat win
                            if childPathAnswer==2:
                                hasAPathWhereCatWins = True
                                break
                            # draw
                            elif childPathAnswer==0:
                                hasAPathWhichLeadsToDraw = True

                    if hasAPathWhereCatWins:
                        memo[(mouseNode, catNode, steps)] = 2
                    elif hasAPathWhichLeadsToDraw:
                        memo[(mouseNode, catNode, steps)] = 0
                    else:
                        memo[(mouseNode, catNode, steps)] = 1

            return memo[(mouseNode, catNode, steps)]

        return dfs(1, 2, 0)

from functools import lru_cache
class Solution:
    def catMouseGame(self, adjList):

        @lru_cache(None)
        def dfs(mouseNode, catNode, steps):

            # mouse win case
            if mouseNode==0:
                return 1
            # cat win case
            if catNode==mouseNode:
                return 2
            # draw case
            if steps==2*len(adjList):
                return 0
           
            # mouse turn
            if not steps&1:
                if any(dfs(neigh, catNode, steps+1) == 1 for neigh in adjList[mouseNode]): return 1
                if all(dfs(neigh, catNode, steps+1) == 2 for neigh in adjList[mouseNode]) : return 2
                return 0

            #cat's turn
            else:
                if any(dfs(mouseNode, neigh, steps+1) == 2 for neigh in adjList[catNode] if neigh!=0): return 2
                if all(dfs(mouseNode, neigh, steps+1) == 1 for neigh in adjList[catNode] if neigh!=0): return 1
                return 0
            
        return dfs(1, 2, 0)


from collections import deque
class Solution:
    def catMouseGame(self, graph):
        n = len(graph)
        # (mouseVertex, catVertex, turn) represents node in possible moves Tree (decision tree)
        # (V, V, 2) possible states where V is number of vertices in graph
        # (0, *, *) -> mouse win
        # (x, x, *) -> cat win
        queueOfDecisionTreeNodes = deque()
        MOUSE, CAT = 0, 1 
        # helps to only add a decision tree node once to queue
        decisionTreeNodesWhoseDecisionsAreMade = set()
        for node in range(n):
            for k in range(2):
                # mouseNodeInGraph, catNodeInGraph, lastMoveInGraphBy, decisionTreeNodeWonBy
                decisionTreeNodesWhoseDecisionsAreMade.add((0, node, k))
                queueOfDecisionTreeNodes.append((0, node, k, MOUSE))
                if node!=0:
                    decisionTreeNodesWhoseDecisionsAreMade.add((node, node, k, CAT))
                    queueOfDecisionTreeNodes.append((node, node, k, CAT))

        outDegreeArr = [[[0 for _ in range(2)] for _ in range(n)] for _ in range(n)]
        for mouseNodeInGraph in range(n):
            for catNodeInGraph in range(n):
                for nextMoveBy in range(2):
                    if nextMoveBy==MOUSE:
                        outDegreeArr[mouseNodeInGraph][catNodeInGraph][nextMoveBy] = len(graph[mouseNodeInGraph])
                    if nextMoveBy==CAT:
                        outDegreeArr[mouseNodeInGraph][catNodeInGraph][nextMoveBy] = len(graph[catNodeInGraph])
                        if 0 in graph[catNodeInGraph]:
                            outDegreeArr[mouseNodeInGraph][catNodeInGraph][nextMoveBy] -= 1

        while queueOfDecisionTreeNodes:
            mouseNodeInGraph, catNodeInGraph, moveCorrespondsTo, decisionTreeNodeWonBy = queueOfDecisionTreeNodes.popleft()
            # reached the Decision Tree Root and move is by mouse
            if mouseNodeInGraph==1 and catNodeInGraph==2 and moveCorrespondsTo==MOUSE:
                # since 0 -> draw, 1 -> mouse win, 2 -> cat win
                return decisionTreeNodeWonBy + 1

            if moveCorrespondsTo==MOUSE:
                # if this moveCorrespondsTo mouse, we need to update all the moves that corresponds to cat that can lead here
                # check a cat move in decision tree that can use this state
                # i.e., all nodes that cat could have used to reach this catNodeInGraph from
                # i.e., all the edges in graph
                for catNodeInGraphThatCouldBringTheCatHere in graph[catNodeInGraph]:
                    if not (mouseNodeInGraph, catNodeInGraphThatCouldBringTheCatHere, CAT) in decisionTreeNodesWhoseDecisionsAreMade:
                        # because cat could not have come from 0 node
                        if catNodeInGraphThatCouldBringTheCatHere!=0:
                            if decisionTreeNodeWonBy==CAT:
                                queueOfDecisionTreeNodes.append((mouseNodeInGraph, catNodeInGraphThatCouldBringTheCatHere, CAT, CAT))
                                decisionTreeNodesWhoseDecisionsAreMade.add((mouseNodeInGraph, catNodeInGraphThatCouldBringTheCatHere, CAT))
                            if decisionTreeNodeWonBy==MOUSE:
                                outDegreeArr[mouseNodeInGraph][catNodeInGraphThatCouldBringTheCatHere][CAT] -= 1
                                if outDegreeArr[mouseNodeInGraph][catNodeInGraphThatCouldBringTheCatHere][CAT] == 0:
                                    queueOfDecisionTreeNodes.append((mouseNodeInGraph, catNodeInGraphThatCouldBringTheCatHere, CAT, MOUSE))
                                    decisionTreeNodesWhoseDecisionsAreMade.add((mouseNodeInGraph, catNodeInGraphThatCouldBringTheCatHere, CAT))
            if moveCorrespondsTo==CAT:
                for mouseNodeInGraphThatCouldBringTheMouseHere in graph[mouseNodeInGraph]:
                    if not (mouseNodeInGraphThatCouldBringTheMouseHere, catNodeInGraph, MOUSE) in decisionTreeNodesWhoseDecisionsAreMade:
                        if decisionTreeNodeWonBy==MOUSE:
                            queueOfDecisionTreeNodes.append((mouseNodeInGraphThatCouldBringTheMouseHere, catNodeInGraph, MOUSE, MOUSE))
                            decisionTreeNodesWhoseDecisionsAreMade.add((mouseNodeInGraphThatCouldBringTheMouseHere, catNodeInGraph, MOUSE))
                        if decisionTreeNodeWonBy==CAT:
                            outDegreeArr[mouseNodeInGraphThatCouldBringTheMouseHere][catNodeInGraph][MOUSE] -= 1
                            if outDegreeArr[mouseNodeInGraphThatCouldBringTheMouseHere][catNodeInGraph][MOUSE] == 0:
                                queueOfDecisionTreeNodes.append((mouseNodeInGraphThatCouldBringTheMouseHere, catNodeInGraph, MOUSE, CAT))
                                decisionTreeNodesWhoseDecisionsAreMade.add((mouseNodeInGraphThatCouldBringTheMouseHere, catNodeInGraph, MOUSE))
        return 0