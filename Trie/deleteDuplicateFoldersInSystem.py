from typing import List

class Trie:
    def __init__(self) -> None:
        self.children = defaultdict(Trie)
        self.serialization = ""
    
    def insert(self, words):
        node = self
        for word in words:
            node = node.children[word]

    def populateSerializations(self, node, nodeWord, seralizationsToCountMap):
        childSerializations = ""
        for child in sorted(node.children):
            childSerializations += self.populateSerializations(node.children[child], child, seralizationsToCountMap)
        node.serialization = childSerializations
        seralizationsToCountMap[node.serialization] += 1
        return nodeWord + node.serialization + "."
    
    def getUniquePaths(self, node, pathSoFar, uniquePaths, seralizationsToCountMap):
        if node.serialization and seralizationsToCountMap[node.serialization]>1: return
        if pathSoFar: uniquePaths.append(pathSoFar)
        for child in sorted(node.children):
            self.getUniquePaths(node.children[child], pathSoFar + [child], uniquePaths, seralizationsToCountMap)


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        trie, seralizationsToCountMap, uniquePaths = Trie(), defaultdict(int), []
        for path in paths: trie.insert(path)
        trie.populateSerializations(trie, "/", seralizationsToCountMap)
        trie.getUniquePaths(trie, [], uniquePaths, seralizationsToCountMap)
        return uniquePaths