# TLE even if this is actually O(n^2)
from collections import defaultdict
class Trie:
    def __init__(self) -> None:
        self.children = defaultdict(Trie)
        self.end = 0
        self.isEcho = False

    def insertNew(self, char):
        node = self.children[char]
        node.end += 1
        return node
    
    def insertOld(self, node, char):
        node.end -= 1
        node = node.children[char]
        node.end += 1
        return node
    
    def insert(self, nodesList, char):
        return [self.insertNew(char)] + [self.insertOld(node, char) for node in nodesList]

    def markEcho(self, word):
        count = 0
        node = self
        for char in word:
            if not char in node.children: return count
            node = node.children[char]
            if node.end>0 and not node.isEcho: 
                node.isEcho = True
                count += 1
        return count


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int: 
        trieRoot, count = Trie(), 0
        trieEndsList = [trieRoot]
        for index in range(len(text)):
            count += trieRoot.markEcho(text[index:])
            trieEndsList = trieRoot.insert(trieEndsList, text[index])
        return count


# Rolling equality counter
# https://leetcode.com/problems/distinct-echo-substrings/solutions/477643/rolling-equality-counter/?orderBy=most_votes

class Solution:
    def distinctEchoSubstrings(self, text: str) -> int: 
        setOfEchoStrings, n = set(), len(text)
        for sizeOfEchoString in range(1, n//2+1):
            numberOfSameChars = sum(text[index]==text[index+sizeOfEchoString] for index in range(sizeOfEchoString))
            if numberOfSameChars==sizeOfEchoString: setOfEchoStrings.add(text[:sizeOfEchoString])
            for leftIndex in range(n-2*sizeOfEchoString):
                numberOfSameChars = numberOfSameChars - (text[leftIndex]==text[leftIndex+sizeOfEchoString]) + (text[leftIndex+sizeOfEchoString]==text[leftIndex+2*sizeOfEchoString])
                if numberOfSameChars==sizeOfEchoString: setOfEchoStrings.add(text[leftIndex+1:leftIndex+sizeOfEchoString+1])
        return len(setOfEchoStrings)


# Brute Hashing (not rolling hash to be specific)
# Trickier hash collision checks
# class Solution:
#     def distinctEchoSubstrings(self, text: str) -> int: 
#         hashesToIndicesMap, n = defaultdict(lambda:defaultdict(list)), len(text)
#         d, q = 26, 1e9+7
#         setOfEchoStrings = set()
#         for startIndex in range(n):
#             hash = 0
#             for endIndex in range(startIndex, n):
#                 hash = (hash*d + text[endIndex])%q
#                 lengthOfString = endIndex-startIndex
#                 hashCollision = False
#                 if hash in hashesToIndicesMap and lengthOfString in hashesToIndicesMap[hash]:
#                     currentText = text[startIndex:endIndex+1]
#                     if any(text[prevStart:prevEnd+1]==currentText for prevStart, prevEnd in hashesToIndicesMap[hash][lengthOfString]):
#                         hashCollision = True
#                 if not hashCollision:
#                     hashesToIndicesMap[hash][lengthOfString].append((startIndex, endIndex))




# Sliding window + hashing => rolling hash
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int: 
        d, q, powMod = 26, int(1e9+7), 1
        setOfEchoStrings, n = set(), len(text)
        for sizeOfEchoString in range(1, n//2+1):
            rollingHash1, rollingHash2, powMod = 0, 0, (powMod*d)%q

            for index in range(sizeOfEchoString):
                rollingHash1 = (rollingHash1*d + ord(text[index]))%q
                rollingHash2 = (rollingHash2*d + ord(text[index+sizeOfEchoString]))%q

            startIndex = 0
            while True:
                if rollingHash1==rollingHash2 and text[startIndex:startIndex+sizeOfEchoString]==text[startIndex+sizeOfEchoString:startIndex+2*sizeOfEchoString]:
                    setOfEchoStrings.add(text[startIndex:startIndex+sizeOfEchoString])
                if startIndex+2*sizeOfEchoString<=n-1:
                    rollingHash1 = (rollingHash1*d - ord(text[startIndex])*powMod + ord(text[startIndex+sizeOfEchoString]))%q
                    rollingHash2 = (rollingHash2*d - ord(text[startIndex+sizeOfEchoString])*powMod + ord(text[startIndex+2*sizeOfEchoString]))%q
                else: break
                startIndex += 1
            
        return len(setOfEchoStrings)