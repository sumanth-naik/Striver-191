class Solution:
    def isPossible(self, n: int, edges):
        degreeArr = [0 for _ in range(n+1)]
        for edge in edges:
            degreeArr[edge[0]] += 1
            degreeArr[edge[1]] += 1
        
        oddDegreeNodes = [node for node in range(n+1) if degreeArr[node]&1]

        if len(oddDegreeNodes)>4: return False
        if len(oddDegreeNodes)==0: return True

        if len(oddDegreeNodes)==4:
            edgesSet = set((min(edge[0],edge[1]), max(edge[0], edge[1])) for edge in edges)
            (node1, node2, node3, node4) = sorted(oddDegreeNodes)
            if not (node1, node2) in edgesSet and not (node3, node4) in edgesSet: return True
            if not (node1, node3) in edgesSet and not (node2, node4) in edgesSet: return True
            if not (node1, node4) in edgesSet and not (node2, node3) in edgesSet: return True
            return False
        if len(oddDegreeNodes)==2:
            # Case 1: direct edge possible?
            # Case 2: does an even degree node without edge to any of these two odd degree nodes exist
            evenDegreeNodesWhichCanNotBeUsed, edgeExistsBetweenThem = set(), False
            for edge in edges:
                if edge[0] in oddDegreeNodes and edge[1] in oddDegreeNodes:
                    edgeExistsBetweenThem = True
                    continue
                if edge[0] in oddDegreeNodes:
                    evenDegreeNodesWhichCanNotBeUsed.add(edge[1])
                if edge[1] in oddDegreeNodes:
                    evenDegreeNodesWhichCanNotBeUsed.add(edge[0])
            return True if len(evenDegreeNodesWhichCanNotBeUsed)<n-2 or not edgeExistsBetweenThem else False


class Solution:
    def isPossible(self, n: int, edges):

        adjSet = defaultdict(set)
        for u, v in edges:
            adjSet[u].add(v)
            adjSet[v].add(u)

        oddDegreeNodes = [i for i in range(1, n+1) if len(adjSet[i])&1]

        if len(oddDegreeNodes)==0: return True
        if len(oddDegreeNodes)>4: return False

        if len(oddDegreeNodes)==2: return len(adjSet[oddDegreeNodes[0]] | adjSet[oddDegreeNodes[1]])<n
        if len(oddDegreeNodes)==4:
            a, b, c, d = oddDegreeNodes
            return (not a in adjSet[b] and not c in adjSet[d]) or \
                    (not a in adjSet[c] and not b in adjSet[d]) or \
                    (not a in adjSet[d] and not b in adjSet[c])
    