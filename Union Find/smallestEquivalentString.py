
class UnionFind:

    def __init__(self):
        self.parent = {}

    def findParent(self, char):
        if self.parent[char]!=char:
            self.parent[char] = self.findParent(self.parent[char])
        return self.parent[char]

    def addCharIfNotPresent(self, char):
        if not char in self.parent:
            self.parent[char] = char

    def union(self, char1, char2):
        self.addCharIfNotPresent(char1)
        self.addCharIfNotPresent(char2)
        parent1 = self.findParent(char1)
        parent2 = self.findParent(char2)
        if not parent1==parent2:
            if parent1<parent2:
                self.parent[parent2] = parent1
            else:
                self.parent[parent1] = parent2
        

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str):
        unionFind = UnionFind()

        for i in range(len(s1)):
            unionFind.union(s1[i], s2[i])

        ansArr = []
        for char in baseStr:
            if char in unionFind.parent:
                ansArr.append(unionFind.findParent(char))
            else:
                ansArr.append(char)
        return ''.join(ansArr)