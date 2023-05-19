from typing import List
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.numSubstrings = 0

    def insert(self, word):
        node = self
        for char in word:
            node = node.children[char]
            node.numSubstrings += 1
    
    def getNumSubstrings(self, word):
        node, numSubstrings = self, 0
        for char in word:
            node = node.children[char]
            numSubstrings += node.numSubstrings
        return numSubstrings

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words: trie.insert(word)
        for word in words: yield trie.getNumSubstrings(word)