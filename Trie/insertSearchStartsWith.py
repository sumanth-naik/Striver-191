class Trie:
     
    def addNode(self, char, node):
        node.links[ord(char) - ord("a")] = Trie()

    def charExists(self, char, node):
        return node.links[ord(char) - ord("a")] is not None
    
    def getLinkedNode(self, char, node):
        return node.links[ord(char) - ord("a")]
    
    
    def __init__(self):
        self.links = [None for i in range(26)]
        self.flag = False
        
    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if not self.charExists(char, node):
                self.addNode(char, node)
            node = self.getLinkedNode(char, node)
        node.flag = True
          
    def search(self, word: str) -> bool:
        node  = self
        for char in word:
            if self.charExists(char, node):
                node = self.getLinkedNode(char, node)
            else:
                return False
        return node.flag

    def startsWith(self, prefix: str) -> bool:
        node = self
        for char in prefix:
            if self.charExists(char, node):
                node = self.getLinkedNode(char, node)
            else:
                return False
        return True
    
    






# shorter version

class Trie:
    
    def __init__(self):
        self.links = {}
        self.flag = False
    
    def insert(self, word):
        node = self
        for char in word:
            if char not in node.links:
                node.links[char] = Trie()
            node = node.links[char]
        node.flag = True
    
    def search(self, word):
        node = self
        for char in word:
            if char in node.links:
                node = node.links[char]
            else:
                return False
        return node.flag

    def startsWith(self, word):
        node = self
        for char in word:
            if char in node.links:
                node = node.links[char]
            else:
                return False
        return True




























