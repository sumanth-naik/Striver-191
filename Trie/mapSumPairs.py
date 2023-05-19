
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.sumOfValues = 0
    
    def insert(self, word, val):
        node = self
        for char in word:
            node = node.children[char]
            node.sumOfValues += val

    def getSumOfValuesWithPrefix(self, prefix):
        node = self
        for char in prefix:
            if not char in node.children: 
                return 0
            node = node.children[char]
        return node.sumOfValues

class MapSum:

    def __init__(self):
        self.trie = Trie()
        self.keyValMap = {}

    def insert(self, key: str, val: int) -> None:
        if key in self.keyValMap:
            self.trie.insert(key, val - self.keyValMap[key])
        else:
            self.trie.insert(key, val)
        self.keyValMap[key] = val

    def sum(self, prefix: str) -> int:
        return self.trie.getSumOfValuesWithPrefix(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)