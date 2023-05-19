# Process by bucket
class Solution:
    def numMatchingSubseq(self, s: str, words) -> int:
        buckets, numMatchingSubsequences = defaultdict(list), 0
        for word in words: 
            buckets[word[0]].append((word, 0))

        for char in s:
            if char in buckets:
                wordsWithIndices = buckets[char]
                del buckets[char]
                for word, index in wordsWithIndices:
                    if index+1==len(word):
                        numMatchingSubsequences += 1
                    else:
                        buckets[word[index+1]].append((word, index+1))

        return numMatchingSubsequences
    
class Solution:
    def numMatchingSubseq(self, s: str, words) -> int:
        buckets = defaultdict(list)
        for word in words: 
            buckets[word[0]].append((word, 0))

        for char in s:
            if char in buckets:
                wordsWithIndices = buckets[char]
                del buckets[char]
                for word, index in wordsWithIndices:
                    if not index+1==len(word):
                        buckets[word[index+1]].append((word, index+1))

        return len(words) - sum(len(wordsWithIndices) for wordsWithIndices in buckets.values())
    

# Binary Search on Subsequence matching
# https://leetcode.com/problems/number-of-matching-subsequences/solutions/1289406/python-binary-search-solution-explained/?orderBy=most_votes
import bisect
class Solution:
    def numMatchingSubseq(self, s: str, words) -> int:
        charToIndicesMap = defaultdict(list)
        for index, char in enumerate(s):
            charToIndicesMap[char].append(index)
        
        def isSubsequence(word):
            indexInS = 0
            for char in word:
                indexInCharIndicesList = bisect.bisect_left(charToIndicesMap[char], indexInS)
                if indexInCharIndicesList==len(charToIndicesMap[char]): return False
                indexInS = charToIndicesMap[char][indexInCharIndicesList] + 1
            return True
        
        return sum(isSubsequence(word) for word in words)