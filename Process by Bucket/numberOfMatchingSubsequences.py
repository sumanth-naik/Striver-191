# Key Idea 1: If we use Trie we will search same subsequences in lower layers multiple times
# Key Idea 2: Use Hashmap from char to indices and update them while searching

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

        return len(words) - sum(map(len, buckets.values()))


# Key Idea 3: Storing indices in Process By Bucket technique instead of entire word   

class Solution:
    def numMatchingSubseq(self, s: str, words) -> int:
        buckets = defaultdict(list)
        for index, word in enumerate(words): 
            buckets[word[0]].append((index, 0))

        for char in s:
            if char in buckets:
                indexInWordsListAndCurrIndexInWord = buckets[char]
                del buckets[char]
                for indexInWordsList, currIndexInWord in indexInWordsListAndCurrIndexInWord:
                    if currIndexInWord+1!=len(words[indexInWordsList]):
                        buckets[words[indexInWordsList][currIndexInWord+1]].append((indexInWordsList, currIndexInWord+1))

        return len(words) - sum(map(len, buckets.values()))




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