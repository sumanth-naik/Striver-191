from typing import List
class Trie:
    def __init__(self) -> None:
        self.children = defaultdict(Trie)
        self.isEnd = False

    def insert(self, word):
        node = self
        for char in word:
            node = node.children[char]
        node.isEnd = True

    def getPrefixIndices(self, word, currIndex):
        node, indicesList, index = self, [], currIndex
        for index in range(currIndex, len(word)):
            char = word[index]
            if char not in node.children:
                return indicesList
            node = node.children[char]
            if node.isEnd:
                indicesList.append(index)
        return indicesList


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:  
        trie = Trie()
        for word in words: 
            trie.insert(word)

        @lru_cache(None)
        def recursion(word, i):
            if len(word)==i: return True
            indicesList = trie.getPrefixIndices(word, i)
            for index in indicesList:
                if i==0 and index==len(word)-1: continue
                if recursion(word, index+1): return True

        return [word for word in words if recursion(word, 0)]


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:  
        trie = Trie()
        for word in words: 
            trie.insert(word)

        @lru_cache(None)
        def recursion(word, multipleUsed):
            indicesList = trie.getPrefixIndices(word, 0)
            for index in indicesList:
                if index==len(word)-1: return multipleUsed
                if recursion(word[index+1:], True): return True

        return [word for word in words if recursion(word, False)]