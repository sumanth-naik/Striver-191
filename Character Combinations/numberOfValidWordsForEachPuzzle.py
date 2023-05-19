from typing import List
from collections import defaultdict

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:

        masksMapOfWords = defaultdict(int)
        for word in words:
            bitMaskOfWord = 0
            for char in set(word):
                bitMaskOfWord |= 1<<(ord(char)-ord('a'))
            masksMapOfWords[bitMaskOfWord] += 1

        counts = []
        for puzzle in puzzles:
            count = 0
            for bitMaskOfSubset in range(2**(len(puzzle)-1)):
                bitMaskOfPuzzle = (1<<(ord(puzzle[0])-ord('a')))
                for index, char in enumerate(puzzle[1:]):
                    if bitMaskOfSubset & (1<<(index)):
                        bitMaskOfPuzzle |= (1<<(ord(char)-ord('a')))
                count += masksMapOfWords[bitMaskOfPuzzle]
            counts.append(count)
        return counts  


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.count = 0
    
    def insert(self, chars):
        node = self
        for char in chars:
            node = node.children[char]
        node.count += 1
    
    def search(self, node, chars, index, firstChar):
        if index == len(chars): return node.count
        count = 0
        if chars[index] in node.children:
            count += self.search(node.children[chars[index]], chars, index+1, firstChar)
        if chars[index]!=firstChar:
            count += self.search(node, chars, index+1, firstChar)
        return count
    
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        trie = Trie()
        for word in words: 
            trie.insert(sorted(set(word)))
        counts = []
        for puzzle in puzzles: 
            counts.append(trie.search(trie, sorted(puzzle), 0, puzzle[0]))
        return counts

