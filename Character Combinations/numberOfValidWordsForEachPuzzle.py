# Key Idea: Create subsets of all combinations of last six chars of puzzle. Or with the first and check the counter
# Note: dont forget to include only first count

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:

        @cache
        def bitMap(word):
            return reduce(lambda acc, char: acc | (1<<(ord(char)-ord('a'))), word, 0)

        @cache
        def solve(puzzle):
            onlyFirst, countWithLastSix = bitMap(puzzle[0]), 0
            subsetOfLastSix = lastSix = bitMap(puzzle[1:])
            while subsetOfLastSix:
                countWithLastSix += wordsCounter[onlyFirst | subsetOfLastSix]
                subsetOfLastSix = (subsetOfLastSix - 1) & lastSix
            return wordsCounter[onlyFirst] + countWithLastSix # Note
        
        wordsCounter = Counter(bitMap(word) for word in words)
        return list(map(solve, puzzles))




'''Other Idea'''
# Key Idea: Use trie with insertion storing count. In search, use strictly take for first char, for other chars, both take/not-take

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.count = 0
    
    def insert(self, word):
        node = self
        for char in word:
            node = node.children[char]
        node.count += 1
    
    def search(self, node, word, index, firstChar):
        if index == len(word): return node.count
        count = 0
        if word[index] in node.children: # take
            count += self.search(node.children[word[index]], word, index+1, firstChar)
        if word[index]!=firstChar: # not take
            count += self.search(node, word, index+1, firstChar)
        return count
    
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        trie = Trie()
        for word in words: 
            trie.insert(sorted(set(word)))
        return [trie.search(trie, sorted(puzzle), 0, puzzle[0]) for puzzle in puzzles]

