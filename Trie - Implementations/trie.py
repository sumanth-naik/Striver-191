# insert, search, startsWith
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
            if not char in node.children: 
                return False
            node = node.children[char]
        return node.isEnd
    
    def startsWith(self, word):
        node = self
        for char in word:
            if not char in node.children:
                return False
            node = node.children[char]
        return True
    
    def searchWithWildCard(self, node, word, index):
        if index==len(word): 
            return node.flag
        if word[index] in node.links: 
            return self.searchWithWildCard(node.links[word[index]], word, index+1)
        if word[index]==".":
            return any(self.searchWithWildCard(node.links[ch], word, index+1) for ch in node.links.keys()) 
        return False


# Trie for anything to do with word -> value mapping
# check number of times a word was added or
# store the sum of values of keys
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
    


# De-dupe in Trie
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
        # always sort if comparing
        for child in sorted(node.children):
            childSerializations += self.populateSerializations(node.children[child], child, seralizationsToCountMap)
        node.serialization = childSerializations
        seralizationsToCountMap[node.serialization] += 1
        return nodeWord + node.serialization + "."
    
    def getUniquePaths(self, node, pathSoFar, uniquePaths, seralizationsToCountMap):
        if node.serialization and seralizationsToCountMap[node.serialization]>1: return
        if pathSoFar: uniquePaths.append(pathSoFar)
        # always sort if comparing
        for child in sorted(node.children):
            self.getUniquePaths(node.children[child], pathSoFar + [child], uniquePaths, seralizationsToCountMap)
