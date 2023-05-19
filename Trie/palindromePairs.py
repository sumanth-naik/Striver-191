# MLE, TLE
# Trie DP
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.indicesSet = set()
        self.endIndicesSet = set()

    def insert(self, word, index):
        node = self
        node.indicesSet.add(index)
        for char in word:
            node = node.children[char]
            node.indicesSet.add(index)
        node.endIndicesSet.add(index)

    def isPalindrome(self, words, indexInWords, indexInWord, memo):
        if (indexInWords, indexInWord) in memo: return memo[(indexInWords, indexInWord)]
        left, right = indexInWord, len(words[indexInWords])-1
        memo[(indexInWords, indexInWord)] = True
        while left<right:
            if not words[indexInWords][left]==words[indexInWords][right]:
                memo[(indexInWords, indexInWord)] = False
                break
            left+=1
            right-=1
        return memo[(indexInWords, indexInWord)]

    def getPadlindromeIndices(self, indexInWords, searchWords, trieWords, trieWordsMemo, searchWordsMemo):
        word = searchWords[indexInWords]
        node, palindromeWordsIndices = self, set()
        for indexInWord, char in enumerate(word):
            if node.endIndicesSet:
                # a word ends here
                if self.isPalindrome(searchWords, indexInWords, indexInWord, searchWordsMemo):
                    palindromeWordsIndices |= node.endIndicesSet
            if not char in node.children:
                return palindromeWordsIndices
            node = node.children[char]
        for wordIndex in node.indicesSet:
            if self.isPalindrome(trieWords, wordIndex, len(word), trieWordsMemo):
                palindromeWordsIndices.add(wordIndex)

        return palindromeWordsIndices




class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie, reverseTrie = Trie(), Trie()
        reverseWords = [word[::-1] for word in words]
        memo, reversedMemo = {}, {}
        resultArr = []
        for index in range(len(words)):
            for validIndex in reverseTrie.getPadlindromeIndices(index, words, reverseWords, reversedMemo, memo):
                resultArr.append([index, validIndex])
            for validIndex in trie.getPadlindromeIndices(index, reverseWords, words, memo, reversedMemo):
                resultArr.append([validIndex, index])
            trie.insert(words[index], index)
            reverseTrie.insert(reverseWords[index], index)

        return resultArr



# worst case TC O(n*l^2), SC O(nl) but better in practice
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        reversedWordsToIndicesMap, resultArr = {}, []
        for index, word in enumerate(words):
            reversedWordsToIndicesMap[word[::-1]] = index # assuming no duplicates

        for index, word in enumerate(words):
            # generates "-abcdedc", "a-bcdedc", "ab-cdedc", "abc-dedc", "abcd-edc", "abcde-dc", "abcded-c"
            for cut in range(len(word)):
                # cut=2: "ab-cdedc" and "ab" in reversedWordsToIndicesMap => "ba" in words => "ab-cdedc-ba" is palindrome
                if word[:cut] in reversedWordsToIndicesMap and word[cut:]==word[cut:][::-1]:
                    resultArr.append([index, reversedWordsToIndicesMap[word[:cut]]])
                    # "" case => add other way as well
                    if cut==0: resultArr.append([reversedWordsToIndicesMap[word[:cut]], index])

                # cut=5: "cdedc-ab" and "ab" in reversedWordsToIndicesMap => "ba" in words => "ba-cdedc-ab" is palindrome
                if word[cut:] in reversedWordsToIndicesMap and word[:cut]==word[:cut][::-1]:
                    resultArr.append([reversedWordsToIndicesMap[word[cut:]], index])

        return [result for result in resultArr if result[0]!=result[1]]

# Python slicing [start:stop:step]:
# If step is positive, the defaults for start and end are 0 and len.
# Else if step is negative, the defaults for start and end are -1 and -len - 1.