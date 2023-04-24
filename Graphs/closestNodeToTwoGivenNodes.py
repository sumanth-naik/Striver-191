class Solution:
    def closestMeetingNode(self, edges, node1: int, node2: int):
        if node1 is node2: return node1
        visited1, visited2 = set([node1]), set([node2])
        while node1 is not None or node2 is not None:
            if node1 is not None and edges[node1] not in visited1 and edges[node1]!=-1:
                node1 = edges[node1]
                visited1.add(node1)
            else:
                node1 = None
            if node2 is not None and edges[node2] not in visited2 and edges[node2]!=-1:
                node2 = edges[node2]
                visited2.add(node2)
            else: 
                node2 = None
            solutions = []
            if node1 in visited2:
                solutions.append(node1)
            if node2 in visited1:
                solutions.append(node2)
            if solutions:
                return min(solutions)
        return -1