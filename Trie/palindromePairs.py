# MLE, TLE
# # Trie DP
# class Trie:
#     def __init__(self):
#         self.children = defaultdict(Trie)
#         self.indicesSet = set()
#         self.endIndicesSet = set()

#     def insert(self, word, index):
#         node = self
#         node.indicesSet.add(index)
#         for char in word:
#             node = node.children[char]
#             node.indicesSet.add(index)
#         node.endIndicesSet.add(index)

#     def isPalindrome(self, words, indexInWords, indexInWord, memo):
#         if (indexInWords, indexInWord) in memo: return memo[(indexInWords, indexInWord)]
#         left, right = indexInWord, len(words[indexInWords])-1
#         memo[(indexInWords, indexInWord)] = True
#         while left<right:
#             if not words[indexInWords][left]==words[indexInWords][right]:
#                 memo[(indexInWords, indexInWord)] = False
#                 break
#             left+=1
#             right-=1
#         return memo[(indexInWords, indexInWord)]

#     def getPadlindromeIndices(self, indexInWords, searchWords, trieWords, trieWordsMemo, searchWordsMemo):
#         word = searchWords[indexInWords]
#         node, palindromeWordsIndices = self, set()
#         for indexInWord, char in enumerate(word):
#             if node.endIndicesSet:
#                 # a word ends here
#                 if self.isPalindrome(searchWords, indexInWords, indexInWord, searchWordsMemo):
#                     palindromeWordsIndices |= node.endIndicesSet
#             if not char in node.children:
#                 return palindromeWordsIndices
#             node = node.children[char]
#         for wordIndex in node.indicesSet:
#             if self.isPalindrome(trieWords, wordIndex, len(word), trieWordsMemo):
#                 palindromeWordsIndices.add(wordIndex)

#         return palindromeWordsIndices




# class Solution:
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#         trie, reverseTrie = Trie(), Trie()
#         reverseWords = [word[::-1] for word in words]
#         memo, reversedMemo = {}, {}
#         resultArr = []
#         for index in range(len(words)):
#             for validIndex in reverseTrie.getPadlindromeIndices(index, words, reverseWords, reversedMemo, memo):
#                 resultArr.append([index, validIndex])
#             for validIndex in trie.getPadlindromeIndices(index, reverseWords, words, memo, reversedMemo):
#                 resultArr.append([validIndex, index])
#             trie.insert(words[index], index)
#             reverseTrie.insert(reverseWords[index], index)

#         return resultArr



# # worst case TC O(n*l^2), SC O(nl) but better in practice
# class Solution:
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#         reversedWordsToIndicesMap, resultArr = {}, []
#         for index, word in enumerate(words):
#             reversedWordsToIndicesMap[word[::-1]] = index # assuming no duplicates

#         for index, word in enumerate(words):
#             # generates "-abcdedc", "a-bcdedc", "ab-cdedc", "abc-dedc", "abcd-edc", "abcde-dc", "abcded-c"
#             for cut in range(len(word)):
#                 # cut=2: "ab-cdedc" and "ab" in reversedWordsToIndicesMap => "ba" in words => "ab-cdedc-ba" is palindrome
#                 if word[:cut] in reversedWordsToIndicesMap and word[cut:]==word[cut:][::-1]:
#                     resultArr.append([index, reversedWordsToIndicesMap[word[:cut]]])
#                     # "" case => add other way as well
#                     if cut==0: resultArr.append([reversedWordsToIndicesMap[word[:cut]], index])

#                 # cut=5: "cdedc-ab" and "ab" in reversedWordsToIndicesMap => "ba" in words => "ba-cdedc-ab" is palindrome
#                 if word[cut:] in reversedWordsToIndicesMap and word[:cut]==word[:cut][::-1]:
#                     resultArr.append([reversedWordsToIndicesMap[word[cut:]], index])

#         return [result for result in resultArr if result[0]!=result[1]]

# # Python slicing [start:stop:step]:
# # If step is positive, the defaults for start and end are 0 and len.
# # Else if step is negative, the defaults for start and end are -1 and -len - 1.

# O(const*n*l) TC, SC but slow in Real life, since const is taxing and well, Trie
from typing import List
from collections import defaultdict

class Trie:
    def __init__(self) -> None:
        self.children = {}
        self.wordIndicesWithPalindromeSuffixes = []
        # assuming distinct words, else use set
        self.endingWordIndex = None

    def insert(self, word, wordIndex, wordPalindromeIndices):
        node = self
        for index, char in enumerate(word):
            if index in wordPalindromeIndices:
                node.wordIndicesWithPalindromeSuffixes.append(wordIndex)
            if not char in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.endingWordIndex = wordIndex

    def getPalindromeIndicesFromTrie(self, searchWord, searchWordIndex, searchWordPalindromeIndices, palindromePairs):
        node = self
        for index, char in enumerate(searchWord):
            # short word in trie, long search word
            if node.endingWordIndex is not None and index in searchWordPalindromeIndices:
                palindromePairs.append([searchWordIndex, node.endingWordIndex])
            if char in node.children:
                node = node.children[char]
            else: 
                return 
            
        # equal length words
        if node.endingWordIndex is not None and node.endingWordIndex!=searchWordIndex:
            palindromePairs.append([searchWordIndex, node.endingWordIndex])

        # long word in trie, short searchWord
        for palindromeSuffixWordIndex in node.wordIndicesWithPalindromeSuffixes:
            palindromePairs.append([searchWordIndex, palindromeSuffixWordIndex])
    



class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        # Manacher's algo
        def getPalindromeIndicesWhichSpanTillLastCharacter(s):
            s = "$#" + ''.join(s[i]+"#" for i in range(len(s))) + "@"
            center, right, lpsArr = 0, 0, [0 for _ in range(len(s))]
            n, indicesSet = len(lpsArr), set()

            for index in range(1, len(s)-1):
                if right>index:
                    mirror = 2*center - index
                    lpsArr[index] = min(right-index, lpsArr[mirror])
                while s[index+lpsArr[index]+1]==s[index-lpsArr[index]-1]:
                    lpsArr[index]+=1
                currRight = index+lpsArr[index]
                if currRight>right:
                    center = index
                    right = currRight
                
                if currRight==n-2:
                    indicesSet.add((index-lpsArr[index])//2)
            return indicesSet
    
        trie, palindromePairs = Trie(), []
        for index, word in enumerate(words):
            reversedWord = word[::-1]
            trie.insert(reversedWord, index, getPalindromeIndicesWhichSpanTillLastCharacter(reversedWord))
        for index, word in enumerate(words):
            trie.getPalindromeIndicesFromTrie(word, index, getPalindromeIndicesWhichSpanTillLastCharacter(word), palindromePairs)
        del trie
        return palindromePairs
        
