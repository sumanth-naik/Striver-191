from typing import List
class Trie:
    def __init__(self) -> None:
        self.children = defaultdict(Trie)
        self.setOfIndices = set()

    def insert(self, word, index):
        node = self
        for char in word:
            node = node.children[char]
            node.setOfIndices.add(index)
        
    def getIndices(self, word):
        node = self
        for char in word:
            if not char in node.children: return set()
            node = node.children[char]
        return node.setOfIndices


class WordFilter:

    def __init__(self, words: List[str]):
        self.prefixTrie = Trie()
        self.suffixTrie = Trie()
        for index, word in enumerate(words):
            self.prefixTrie.insert(word, index)
            self.suffixTrie.insert(word[::-1], index)

    def f(self, pref: str, suff: str) -> int:
        prefixIndices = self.prefixTrie.getIndices(pref)
        suffixIndices = self.suffixTrie.getIndices(suff[::-1])
        intersection = prefixIndices & suffixIndices
        return max(intersection) if intersection else -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)

from typing import List
class Trie:
    def __init__(self) -> None:
        self.children = defaultdict(Trie)
        self.maxIndex = -1

    def insert(self, word, index):
        node = self
        for char in word:
            node = node.children[char]
            node.maxIndex = max(node.maxIndex, index)
        
    def getMaxIndex(self, word):
        node = self
        for char in word:
            if not char in node.children: return -1
            node = node.children[char]
        return node.maxIndex

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for wordIndex, word in enumerate(words):
            for index in range(len(word)):
                self.trie.insert(word[index:]+"#"+word, wordIndex)

    def f(self, pref: str, suff: str) -> int:
        return self.trie.getMaxIndex(suff+"#"+pref)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)