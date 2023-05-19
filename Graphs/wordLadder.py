from typing import List
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordsSet = set(wordList)
        queue = deque([(beginWord, 1)])
        while queue:
            elem, steps = queue.popleft()
            if elem==endWord: return steps
            
            for i in range(len(elem)):
                for j in range(26):
                    ch = elem[i]
                    if ord('a')+j != ord(ch):
                        newString = elem[:i] + chr(ord('a')+j) + elem[i+1:]
                        if newString in wordsSet:
                            queue.append((newString, steps+1))
                            wordsSet.remove(newString)
        return 0
    
# Meet in the middle
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordsSet = set(wordList)
        if endWord not in wordsSet: return 0
        queue = deque([(beginWord, 1), (endWord, 1)])
        beginVisitedMap, endVisitedMap = {}, {}
        beginVisitedMap[beginWord] = 1
        endVisitedMap[endWord] = 1

        while queue:
            elem, steps = queue.popleft()
            for i in range(len(elem)):
                leftPart, rightPart = elem[:i], elem[i+1:]
                for j in range(26):
                    if ord('a')+j != ord(elem[i]):
                        newString = leftPart + chr(ord('a')+j) + rightPart
                        if elem in beginVisitedMap and newString in endVisitedMap:
                            return beginVisitedMap[elem] + endVisitedMap[newString]
                        if elem in endVisitedMap and newString in beginVisitedMap:
                            return endVisitedMap[elem] + beginVisitedMap[newString]

                        if newString in wordsSet:
                            queue.append((newString, steps+1))
                            wordsSet.remove(newString)
                            if elem in beginVisitedMap: beginVisitedMap[newString] = steps+1
                            elif elem in endVisitedMap: endVisitedMap[newString] = steps+1
        return 0
    
