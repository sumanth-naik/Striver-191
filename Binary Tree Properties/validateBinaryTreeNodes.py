'''
Key Idea: Figure out all necessary conditions
Necessary Conditions: 
1. A binary tree must have one and only one root. 
2. Every node other than the root must have exactly one parent. 
3. The tree must be connected - every node must be reachable from one node (the root).
4. There cannot be a cycle. 

1,2,3 or 2,3,4 are enough. 4 can be derived if 1,2,3 are guaranteed. 1 can be derived if 2,3,4 are guaranteed.
'''

# solves with condition 1,2 and 3 in mind
# Key Idea 1: Create indegreeArr to find if there is one and only one root
# Key Idea 2: Use DFS/BFS to find cycles with visited set
# Key Idea 3: Use visited set size to check if all belong to same component
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegreeArr = [0]*n
        for index, (left, right) in enumerate(zip(leftChild, rightChild)):
            if left!=-1:
                indegreeArr[left] += 1
            if right!=-1:
                indegreeArr[right] += 1 
                
        if indegreeArr.count(0)==1: # condition 1
            root = indegreeArr.index(0)
        else:
            return False

        visited = set()
        def dfs(node):  # condition 2
            visited.add(node)
            if leftChild[node]!=-1:
                if leftChild[node] in visited: return False
                if not dfs(leftChild[node]): return False
            if rightChild[node]!=-1:
                if rightChild[node] in visited: return False
                if not dfs(rightChild[node]): return False
            return True
        
        if not dfs(root): return False
        return len(visited)==n # condition 3


# solves with condition 1,2 and 3 in mind
# Key Idea 1: Create a set of children. Every node except root must be there in that set.
# Key Idea 2: Use DFS/BFS to find cycles with visited set
# Key Idea 3: Use visited set size to check if all belong to same component
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        children = set(leftChild+rightChild)
        children.discard(-1)
        if not len(children)==n-1: return False # condition 1

        root = (set(range(n)) - children).pop()

        visited = set()
        def dfs(node): #condition 2
            if node==-1: return True
            if node in visited: return False
            visited.add(node)
            return dfs(leftChild[node]) and dfs(rightChild[node])

        return dfs(root) and len(visited)==n # condition 3

            
# solves with condition 2,3 and 4 in mind
# Key Idea 1: Use union find to prevent two parents and cycle while performing union
# Key Idea 2: Track number of components
class UnionFind:
    def __init__(self, n):
        self.components = n
        self.parent =list(range(n))
    
    def findParent(self, node):
        if self.parent[node]!=node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def union(self, parent, child):
        if child==-1: return True
        parentParent = self.findParent(parent)
        childParent = self.findParent(child)

        if childParent!=child or parentParent==child: return False # condition 2, 4

        self.parent[child] = parent
        self.components -= 1
        return True

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        unionFind = UnionFind(n)
        for parent, (left, right) in enumerate(zip(leftChild, rightChild)):
            if not unionFind.union(parent, left) or not unionFind.union(parent, right): return False
        return unionFind.components==1 # condition 3


# solves with conditions 1,2 and 3 in mind
# Key Idea 1: Create indegreeArr to find if there is one and only one root
# Key Idea 2: Use Kahn's Algorithm(without any topoSortArr). Check that there isn't any node with indeg>1
# Key Idea 3: Use visited set size to check if all belong to same component
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegreeArr = [0] * n
        for parent, (left, right) in enumerate(zip(leftChild, rightChild)):
            if left!=-1: indegreeArr[left] += 1
            if right!=-1: indegreeArr[right] += 1
        
        queue = deque([node for node in range(n) if indegreeArr[node]==0])
        if len(queue)!=1: return False # condition 1
        visited = set(queue)

        while queue:
            node = queue.popleft()
            for child in [leftChild[node], rightChild[node]]:
                if child!=-1:
                    indegreeArr[child] -= 1
                    if indegreeArr[child] == 0:
                        visited.add(child)
                        queue.append(child)
                    else:
                        return False # condition 2
        return len(visited)==n # condition 3
                