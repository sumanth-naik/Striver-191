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

    def getLongestWord(self, node, largestWordSoFar, currentWord):
        if len(currentWord)>len(largestWordSoFar[0]):
            largestWordSoFar[0] = currentWord

        for char in sorted(node.children):
            if node.children[char].isEnd:
                self.getLongestWord(node.children[char], largestWordSoFar, currentWord+char)

    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words: trie.insert(word)
        largestWord = [""]
        trie.getLongestWord(trie, largestWord, "")
        return largestWord[0]