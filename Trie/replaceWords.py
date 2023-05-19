from typing import List

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.isEnd = False

    def insert(self, word):
        node = self
        for char in word:
            node = node.children[char]
        node.isEnd = True

    @lru_cache(None)
    def shortestStringInTrie(self, word):
        node = self
        for index, char in enumerate(word):
            node = node.children[char]
            if node.isEnd: return word[:index+1]
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:   
        trie = Trie()
        for word in dictionary: trie.insert(word)
        return ' '.join(trie.shortestStringInTrie(sentenceWord) for sentenceWord in sentence.split(" "))
