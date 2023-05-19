




class Trie:
    def __init__(self):
        self.links = {}
        self.numPrefixes = 0
        self.numEnd = 0
        
    def insert(self, word):
        node = self
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

        
# trie = Trie()
# trie.insert("apple")
# trie.insert("app")
# trie.insert("apple")
# print(trie.countWordsStartingWith("a"))   
# print(trie.countWordsEqualTo("apple"))  
# trie.erase("apple")
# print(trie.countWordsStartingWith("a"))   
# print(trie.countWordsEqualTo("apple"))   








# Trie insert, search, delete on unique Strings
class Trie:
    def __init__(self) -> None:
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
        return node.isEnd

    def delete(self, word, index=0):
        if index==len(word):
            # doesnt matter if ends here or not
            self.isEnd = False
            return not len(self.children) 
        
        # word not there, dont delete anything
        if not word[index] in self.children: 
            return False
        
        if self.children[word[index]].delete(word, index+1):
            del self.children[word[index]]

        # delete only if i am not part of some other word and i am not the end of some other word
        return not len(self.children) and not self.isEnd
        
from collections import defaultdict
# empty string case not covered
# better to have a wrapper class than making code cumbersome
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.numEnd = 0
        self.numStartingWith = 0

    def insert(self, word):
        node = self
        for char in word:
            node = node.children[char]
            node.numStartingWith += 1
        node.numEnd += 1

    def countWordsEqualTo(self, word):
        node = self
        for char in word:
            if not char in node.children: return 0
            node = node.children[char]
        return node.numEnd

    def countWordsStartingWith(self, word):
        node = self
        for char in word:
            if not char in node.children: return 0
            node = node.children[char]
        return node.numStartingWith
    
    # erase when we know word exists
    def erase(self, word, index = 0):
        self.numStartingWith -= 1

        if index==len(word):
            self.numEnd -= 1
            return self.numEnd==0 and len(self.children)==0

        if word[index] not in self.children: return False

        if self.children[word[index]].erase(word, index+1):
            del self.children[word[index]]

        return self.numEnd==0 and len(self.children)==0
    
    def searchAndErase(self, word):
        if self.countWordsEqualTo(word): self.erase(word)


    # # simultaneous erase and search - unnecessary complication
    # def searchAndErase(self, word, index = 0):
    #     if index==len(word):
    #         if self.numEnd!=0:
    #             self.numEnd -= 1
    #             self.numStartingWith -= 1
    #             return self.numEnd==0 and len(self.children)==0, True
    #         return False, False
        
    #     if word[index] not in self.children: return False, False

    #     shouldDeleteChild, wordFound = self.children[word[index]].searchAndErase(word, index+1)
    #     if wordFound:
    #         self.numStartingWith -= 1
    #         if shouldDeleteChild:
    #             del self.children[word[index]]

    #     return self.numEnd==0 and len(self.children)==0, wordFound




trie = Trie()
trie.insert("code")
trie.insert("code")
print(trie.countWordsStartingWith("co"))
print(trie.countWordsStartingWith("code"))
print(trie.countWordsStartingWith("codes"))
print(trie.countWordsStartingWith("coding"))
print("*****")
trie.insert("coding")
print(trie.countWordsStartingWith("co"))
print(trie.countWordsStartingWith("code"))
print(trie.countWordsStartingWith("codes"))
print(trie.countWordsStartingWith("coding"))
print("*****")
trie.searchAndErase("coding")
print(trie.countWordsStartingWith("co"))
print(trie.countWordsStartingWith("code"))
print(trie.countWordsStartingWith("codes"))
print(trie.countWordsStartingWith("coding"))
print("*****")
trie.insert("coding")
trie.searchAndErase("cod")
print(trie.countWordsStartingWith("co"))
print(trie.countWordsStartingWith("code"))
print(trie.countWordsStartingWith("codes"))
print(trie.countWordsStartingWith("coding"))
print("*****")
trie.searchAndErase("code")
print(trie.countWordsStartingWith("co"))
print(trie.countWordsStartingWith("code"))
print(trie.countWordsStartingWith("codes"))
print(trie.countWordsStartingWith("coding"))
print("*****")
trie.searchAndErase("code")
print(trie.countWordsStartingWith("co"))
print(trie.countWordsStartingWith("code"))
print(trie.countWordsStartingWith("codes"))
print(trie.countWordsStartingWith("coding"))
print("*****")

trie.searchAndErase("coding")
print(trie.countWordsStartingWith("co"))
print(trie.countWordsStartingWith("code"))
print(trie.countWordsStartingWith("codes"))
print(trie.countWordsStartingWith("coding"))
print("*****")
trie.searchAndErase("code")
print(trie.countWordsStartingWith("co"))
print(trie.countWordsStartingWith("code"))
print(trie.countWordsStartingWith("codes"))
print(trie.countWordsStartingWith("coding"))
print("*****")


