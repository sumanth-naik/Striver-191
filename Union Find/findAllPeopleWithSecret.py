class UnionFind:
    def __init__(self) -> None:
        self.parent = {}
        self.size = {}
    
    def findParent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def addNode(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.size[node] = 1

    def union(self, node1, node2):
        self.addNode(node1)
        self.addNode(node2)
        parent1 = self.findParent(node1) 
        parent2 = self.findParent(node2) 
        if parent1!=parent2:
            if self.size[parent1]>self.size[parent2]:
                self.parent[parent2] = parent1
                self.size[parent1] += self.size[parent2]
            else:
                self.parent[parent1] = parent2
                self.size[parent2] += self.size[parent1]

    def belongsToSameComponent(self, node1, node2):
        return self.findParent(node1) == self.findParent(node2)

    def getParentToNodesInComponentMap(self):
        parentsToNodesInComponentMap = defaultdict(list)
        for node in self.parent:
            parent = self.findParent(node)
            parentsToNodesInComponentMap[parent].append(node)
        return parentsToNodesInComponentMap



class Solution:
    def findAllPeople(self, n: int, meetings, firstPerson: int):
        timeToPersonsWithMeetingsMap = defaultdict(list)
        for person1, person2, time in meetings:
            timeToPersonsWithMeetingsMap[time].append((person1, person2))
        
        secretKnowingPeopleSet = {0, firstPerson}
        for time in sorted(timeToPersonsWithMeetingsMap.keys()):
            unionFind = UnionFind()
            for person1, person2 in timeToPersonsWithMeetingsMap[time]:
                unionFind.union(person1, person2)
            parentsKnowingSecretsSet = set()
            for person1, person2 in timeToPersonsWithMeetingsMap[time]:
                if person1 in secretKnowingPeopleSet or person2 in secretKnowingPeopleSet:
                    parentsKnowingSecretsSet.add(unionFind.findParent(person1))
            for parent, nodes in unionFind.getParentToNodesInComponentMap().items():
                if parent in parentsKnowingSecretsSet:
                    secretKnowingPeopleSet.update(nodes)
                
        return secretKnowingPeopleSet