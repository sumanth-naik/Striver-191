




class Trie:
    def __init__(self):
        self.links = {}
        self.numPrefixes = 0
        self.numEnd = 0
        
    def insert(self, word):
        node  = self
        for char in word:
            if char not in node.links:
                node.links[char] = Trie()
            node.numPrefixes += 1
            node = node.links[char]
        node.numPrefixes += 1
        node.numEnd += 1

    def countWordsEqualTo(self, word):
        node = self
        for char in word:
            if char in node.links:
                node = node.links[char]
            else:
                return 0
        return node.numEnd

    def countWordsStartingWith(self, word):
        node = self
        for char in word:
            if char in node.links:
                node = node.links[char]
            else:
                return 0
        return node.numPrefixes

    def erase(self, word):
        branchDeleted = False
        node = self.links[word[0]]
        prevNode = self
        prevChar = word[0]
        for char in word[1:]:
            node.numPrefixes -= 1
            if(node.numPrefixes==0):
                del prevNode.links[prevChar]
                branchDeleted = True
                break
            else:
                prevNode = node
                prevChar = char
                node = node.links[char]

        if not branchDeleted:
            node.numPrefixes -= 1
            node.numEnd -= 1
        
        
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("apple")
print(trie.countWordsStartingWith("a"))   
print(trie.countWordsEqualTo("apple"))  
trie.erase("apple")
print(trie.countWordsStartingWith("a"))   
print(trie.countWordsEqualTo("apple"))   















