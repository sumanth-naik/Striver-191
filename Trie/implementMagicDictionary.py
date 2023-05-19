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

    def searchWithOneDiff(self, node, word, index, isDiffUsed):
        if index==len(word): return node.isEnd and isDiffUsed
        if word[index] in node.children and self.searchWithOneDiff(node.children[word[index]], word, index+1, isDiffUsed):
            return True
        if not isDiffUsed:
            for char in node.children:
                if char!=word[index] and self.searchWithOneDiff(node.children[char], word, index+1, True):
                    return True
        return False


class MagicDictionary:

    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary: self.trie.insert(word)

    def search(self, searchWord: str) -> bool:
        return self.trie.searchWithOneDiff(self.trie, searchWord, 0, False)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)