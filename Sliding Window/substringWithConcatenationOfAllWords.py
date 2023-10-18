class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        lenOfS, lenOfWords, lenOfEachWord = len(s), len(words), len(words[0])
        wordsSet = set(words)
        wordsInSArr = []
        for index in range(lenOfS-lenOfEachWord+1):
            wordFromIndex = s[index:index+lenOfEachWord]
            wordsInSArr.append(wordFromIndex if wordFromIndex in wordsSet else None)
        
        counterOfWords = Counter(words)
        indicesWithValidPermutationsArr = []
        for slidingWindowIndex in range(lenOfS-lenOfWords*lenOfEachWord+1):
            currMap = defaultdict(int)
            for loopIndexForEachWord in range(slidingWindowIndex, slidingWindowIndex+lenOfWords*lenOfEachWord+1, lenOfEachWord):
                if loopIndexForEachWord==slidingWindowIndex+lenOfWords*lenOfEachWord: 
                    indicesWithValidPermutationsArr.append(slidingWindowIndex)
                else:
                    if not wordsInSArr[loopIndexForEachWord]: break
                    currMap[wordsInSArr[loopIndexForEachWord]] += 1
                    if currMap[wordsInSArr[loopIndexForEachWord]]>counterOfWords[wordsInSArr[loopIndexForEachWord]]: break
        return indicesWithValidPermutationsArr

# 30 min
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        lenOfS, lenOfWord, countOfWords = len(s), len(words[0]), len(words)
        counterOfWords, ansIndices = Counter(words), []
        for index in range(lenOfWord):
            wordsNeededMap = deepcopy(counterOfWords)
            countNeeded = countOfWords
            slidingWindowTailIndex = index

            for windowIndex in range(index, lenOfS, lenOfWord):
                
                currWord = s[windowIndex:windowIndex+lenOfWord]
                if currWord in wordsNeededMap:
                    wordsNeededMap[currWord] -= 1
                    if wordsNeededMap[currWord]>=0: countNeeded -= 1

                    if windowIndex-slidingWindowTailIndex>=lenOfWord*countOfWords: 
                        prevWord = s[slidingWindowTailIndex:slidingWindowTailIndex+lenOfWord]
                        if prevWord in wordsNeededMap:
                            wordsNeededMap[prevWord] += 1
                            countNeeded += 1
                        slidingWindowTailIndex += lenOfWord
                    if countNeeded==0: ansIndices.append(windowIndex-lenOfWord*(countOfWords-1))
                else:
                    wordsNeededMap = deepcopy(counterOfWords)
                    countNeeded = countOfWords
                    slidingWindowTailIndex = windowIndex + lenOfWord

        return ansIndices
    

# 8 min
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        lenOfS, lenOfWord, countOfWords = len(s), len(words[0]), len(words)
        counterOfWords, ansIndices = Counter(words), []
        for index in range(lenOfWord):
            left = right = index
            # keep freqOfWindowWords and countNeeded consistent by removing excess using the second while loop
            freqOfWindowWords, countNeeded = defaultdict(int), countOfWords
            while right+lenOfWord<=lenOfS:
                rightWord = s[right:right+lenOfWord]
                if rightWord not in counterOfWords:
                    freqOfWindowWords, countNeeded = defaultdict(int), countOfWords
                    left = right = right+lenOfWord
                else:
                    freqOfWindowWords[rightWord] += 1
                    countNeeded -= 1
                    while freqOfWindowWords[rightWord]>counterOfWords[rightWord]:
                        leftWord = s[left:left+lenOfWord]
                        freqOfWindowWords[leftWord] -= 1
                        countNeeded += 1
                        left += lenOfWord
                    if countNeeded==0: ansIndices.append(left)
                    right += lenOfWord
        return ansIndices



# 7 min
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        lenOfS, lenOfWord, countOfWords = len(s), len(words[0]), len(words)
        counterOfWords, ansIndices = Counter(words), []

        for left in range(lenOfWord):
            windowWordsFreqMap = defaultdict(int)
            for right in range(left, lenOfS-lenOfWord+1, lenOfWord):
                rightWord = s[right:right+lenOfWord]
                windowWordsFreqMap[rightWord] += 1
                # in case rightWord is not a valid word, we remove everything
                while windowWordsFreqMap[rightWord]>counterOfWords[rightWord]:
                    windowWordsFreqMap[s[left:left+lenOfWord]] -= 1
                    left += lenOfWord
                if left+lenOfWord*countOfWords==right+lenOfWord:
                    ansIndices.append(left)

        return ansIndices
