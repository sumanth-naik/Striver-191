class WordDictionary:
    
    
    def linkExists(self, char, node):
        return node.links[ord(char)-ord("a")] is not None
    
    def addLink(self, char, node):
        node.links[ord(char)-ord("a")] = WordDictionary()
        
    
    def getLink(self, char, node):
        return node.links[ord(char)-ord("a")]
    
    def getAllValidLinks(self, node):
        validLinks = []
        for i in range(26):
            if node.links[i] is not None:
                validLinks.append(node.links[i])
        return validLinks


    def __init__(self):
        self.links = [None for i in range(26)]
        self.flag = False
        self.searchCache = {}
        

    def addWord(self, word: str) -> None:
        node = self
        for char in word:
            if not self.linkExists(char, node):
                self.addLink(char, node)
            node = self.getLink(char, node)
        node.flag = True


    def recursiveSearch(self, node, word, index):
        if index == len(word):
            if node.flag:
                return True
            return False
        
        if word[index]==".":
            for link in self.getAllValidLinks(node):
                if(self.recursiveSearch(link, word, index+1)):
                    return True
        elif self.linkExists(word[index], node):
            return self.recursiveSearch(self.getLink(word[index], node), word, index + 1)
            
        
        return False
    
    
    def search(self, word: str) -> bool:
        if word not in self.searchCache:
            self.searchCache[word] = self.recursiveSearch(self, word, 0)
        return self.searchCache[word]



class Trie:
    
    def __init__(self):
        self.links = {}
        self.flag = False
       
    def addWord(self, word):
        node = self
        for char in word:
            if char not in node.links:
                node.links[char] = Trie()
            node = node.links[char]
        node.flag = True
        
    def search(self, node, word, index):
        
        if index==len(word):
            return node.flag
        
        if word[index] in node.links:
            return self.search(node.links[word[index]], word, index+1)
        
        if word[index] == ".":
            for char in node.links:
                if(self.search(node.links[char], word, index+1)):
                    return True
        return False
        

class WordDictionary:
    
    def __init__(self):
        self.root = Trie()
        self.searchCache = {}
        
    def addWord(self, word):
        self.root.addWord(word)
        self.searchCache = {}

    def search(self, word):
        if word not in self.searchCache:
            self.searchCache[word] = self.root.search(self.root, word, 0)
        return self.searchCache[word]
    




