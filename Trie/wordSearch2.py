
'''
Brute force

charDict = {}
m = len(board)
n = len(board[0])
for i in range(m):
    for j in range(n):
        char = board[i][j]
        if(char not in charDict):
            charDict[char] = []
        charDict[char].append((i,j))
        
charPairSet = set()
for i in range(m):
    for j in range(n):
        for neigh in [[1+i,j],[i,j+1],[i-1,j],[i,j-1]]:
            if(neigh[0]>=0 and neigh[0]<m and neigh[1]>=0 and neigh[1]<n):
                charPairSet.add(board[i][j]+board[neigh[0]][neigh[1]])
print(charPairSet)
def findWord(word, currMatrixIndex, wordIndex, visited, board):
    i = currMatrixIndex[0]
    j = currMatrixIndex[1]
    if(wordIndex == len(word)):
        return True
    if(i<0 or i>m-1 or j<0 or j>n-1 or board[i][j]!=word[wordIndex] or currMatrixIndex in visited):
        return False
    
    
    for neigh in [[1,0],[0,1],[0,-1],[-1,0]]:
        visited.add(currMatrixIndex)
        if(findWord(word, (i + neigh[0], j + neigh[1]), wordIndex+1, visited, board)):
            return True
        visited.remove(currMatrixIndex)

validWords = []
for word in words:
    
    shouldSearch = True
    for i in range(len(word)):
        if(word[i] not in charDict):
            shouldSearch = False
            #print(word)
            break
        if(i!=len(word)-1 and word[i]+word[i+1] not in charPairSet):
            shouldSearch = False
            #print(word)
            break  
    
    if shouldSearch:
        reversedWord = False
        if len(charDict[word[0]])>len(charDict[word[len(word)-1]]):
            #print(word)
            reversedWord = True
            word = word[::-1]
        for charIndex in charDict[word[0]]:
            if(findWord(word, charIndex, 0, set(), board)):
                if reversedWord:
                    validWords.append(word[::-1])
                else:
                    validWords.append(word)
                break
                
print(validWords)
'''

'''
Complicated Trie - Nov 5th, 2022

class Trie:
    def __init__(self):
        self.links = {}
        self.numPrefixes = 0
        self.numEnds = 0

    def insert(self, word):
        node = self
        for char in word:
            if char not in node.links:
                node.links[char] = Trie()
            node.numPrefixes += 1
            node = node.links[char]
        node.numPrefixes += 1
        node.numEnds += 1


    def countWordsEqualTo(self, word):
        node = self
        for char in word:
            if char in node.links:
                node = node.links[char]
            else:
                return 0
        return node.numEnds

    def countWordsStartingWith(self, word):
        node = self
        for char in word:
            if char in node.links:
                node = node.links[char]
            else:
                return 0
        return node.numPrefixes

    def delete(self, word):
        print("DELETING" + word)
        print(self.links, self.numPrefixes, self.numEnds)
        treePruned = False
        prevNode = self
        prevChar = word[0]
        node = self.links[prevChar]
        for char in word[1:]:
            node.numPrefixes -= 1
            if(node.numPrefixes==0):
                del prevNode.links[prevChar]
                treePruned = True
                break
            else:
                prevNode = node
                prevChar = char
                node = node.links[char]

        if not treePruned:
            node.numPrefixes -= 1
            node.numEnds -= 1

def searchAlongTrie(trieNode, trieRoot, board, visited, i, j, wordSoFar, validWords):

    if trieNode.numEnds>0 and wordSoFar+board[i][j] not in validWords:
        print( visited, i, j, wordSoFar,board[i][j], validWords)
        validWords.add(wordSoFar+board[i][j])
        trieRoot.delete(wordSoFar+board[i][j])

    for (k,l) in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
        if(k<len(board) and l<len(board[0]) and k>=0 and l>=0 and board[k][l] in trieNode.links and (k,l) not in visited):
            visited.add((i,j))
            searchAlongTrie(trieNode.links[board[k][l]], trieRoot, board, visited, k, l, wordSoFar+board[i][j], validWords)
            visited.remove((i,j))



trie = Trie()
for word in words:
    trie.insert(word)

m = len(board)
n = len(board[0])
validWords = set()
for i in range(m):
    for j in range(n):
        if board[i][j] in trie.links:
            visited = set()
            searchAlongTrie(trie.links[board[i][j]], trie, board, visited, i, j, "", validWords)
print(list(validWords))
'''



# Consise Trie - May 16th 2023

from collections import defaultdict
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.indexOfWord = -1

    # store index instead of isEnd, to not maintain wordSoFar in DFS
    def insert(self, word, index):
        node = self
        for char in word:
            node = node.children[char]
        node.indexOfWord = index


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        trieRoot = Trie()
        for index, word in enumerate(words):
            trieRoot.insert(word, index)

        validWords = []

        # merging trie delete with backtracking is best because, we can recursively delete if found and keep track of proper i,j at the same time
        def backTrackingWithTrieDelete(i, j, visitedIndices, trieNode):
            nonlocal validWords
            if trieNode.indexOfWord!=-1:
                validWords.append(words[trieNode.indexOfWord])
                # CORNER CASE: AVOID DUPLICATION
                trieNode.indexOfWord = -1
            if trieNode.children:
                for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                    newI, newJ = i+di, j+dj
                    if 0<=newI<m and 0<=newJ<n and (newI, newJ) not in visitedIndices and board[newI][newJ] in trieNode.children:
                        visitedIndices.add((newI, newJ))
                        shouldDeleteChild = backTrackingWithTrieDelete(newI, newJ, visitedIndices, trieNode.children[board[newI][newJ]])
                        visitedIndices.remove((newI, newJ))
                        if shouldDeleteChild:
                            del trieNode.children[board[newI][newJ]]
            # usual trie delete checks and deletes one word only with
            # len(self.children)==0 and not self.isEnd
            # we should delete all found words and not just one word
            # also, we would not delete unnecessarily because, if we don't find the word, that trieNode would have children
            return len(trieNode.children)==0

        for i in range(m):
            for j in range(n):
                if board[i][j] in trieRoot.children:
                    backTrackingWithTrieDelete(i, j, {(i, j)}, trieRoot.children[board[i][j]])

        return validWords










