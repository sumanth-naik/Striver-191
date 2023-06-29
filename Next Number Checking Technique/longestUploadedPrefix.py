class LUPrefix:

    def __init__(self, n: int):
        self.maxConsecutiveLength = 0
        self.numbersSet = set()

    def upload(self, video: int) -> None:
        self.numbersSet.add(video)
        while self.maxConsecutiveLength+1 in self.numbersSet: self.maxConsecutiveLength += 1

    def longest(self) -> int:
        return self.maxConsecutiveLength


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()

class BIT:
    def __init__(self, n):
        self.size = n+1
        self.tree = [0 for _ in range(self.size)]

    def add(self, index, val=1):
        while index<self.size:
            self.tree[index] += val
            index += (index & -index)

    def sumTill(self, index):
        total = 0
        while index>0:
            total += self.tree[index]
            index -= (index & -index)
        return total

    def getLongestLength(self):
        low, high = 0, self.size-1
        while low<high:
            mid = (low + high + 1)//2
            if self.sumTill(mid)==mid:
                low = mid
            else:
                high = mid - 1
        return low

class LUPrefix:

    def __init__(self, n: int):
        self.bit = BIT(n)

    def upload(self, video: int) -> None:
        self.bit.add(video)

    def longest(self) -> int:
        return self.bit.getLongestLength()


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()

class UnionFind:
    def __init__(self) -> None:
        self.parent = defaultdict(int)
        self.size = defaultdict(int)

    def addNode(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.size[node] = 1

        for diff in [1, -1]:
            if node+diff in self.parent:
                self.union(node, node+diff)

    def findParent(self, node):
        if self.parent[node]!=node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        parent1 = self.findParent(node1)
        parent2 = self.findParent(node2)
        if parent1!=parent2:
            if self.size[parent1]>self.size[parent2]:
                self.parent[parent2] = parent1
                self.size[parent1] += self.size[parent2]
            else:
                self.parent[parent1] = parent2
                self.size[parent2] += self.size[parent1]
        
    def getNode1ComponentSize(self):
        if not 1 in self.parent: return 0
        return self.size[self.findParent(1)]

class LUPrefix:

    def __init__(self, n: int):
        self.unionFind = UnionFind()

    def upload(self, video: int) -> None:
        self.unionFind.addNode(video)

    def longest(self) -> int:
        return self.unionFind.getNode1ComponentSize()
