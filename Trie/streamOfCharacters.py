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

    def search(self, word):
        node = self
        for char in word:
            if not char in node.children: return False
            node = node.children[char]
            if node.isEnd: return True
        return False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trieRoot = Trie()
        self.suffix = ""
        self.maxWordLength = 0

        for word in words:
            self.trieRoot.insert(reversed(word))
            self.maxWordLength = max(self.maxWordLength, len(word))

    def query(self, letter: str) -> bool:
        self.suffix = letter + self.suffix
        if len(self.suffix)>self.maxWordLength: self.suffix = self.suffix[:self.maxWordLength]
        return self.trieRoot.search(self.suffix)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)