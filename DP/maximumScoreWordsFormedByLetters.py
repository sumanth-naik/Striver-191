from collections import Counter
class Solution:
    def maxScoreWords(self, words, letters, score) -> int:
        scoreOfWords = [sum(score[ord(letter)-ord('a')] for letter in word) for word in words]
        wordsCounter, maxScoreSeen = list(map(Counter, words)), 0

        cumulativeSum = deepcopy(scoreOfWords) + [0]
        for i in range(len(scoreOfWords)-2, -1, -1): cumulativeSum[i]+=cumulativeSum[i+1]

        def backtrackingDFS(wordsIndex, remainingLettersCounter, scoreSoFar):
            nonlocal maxScoreSeen
            if scoreSoFar+cumulativeSum[wordsIndex]<=maxScoreSeen: return #pruning

            maxScoreSeen = max(maxScoreSeen, scoreSoFar) # update regardless of reaching the last index
            for index in range(wordsIndex, len(words)):
                if all(neededCountOfLetter<=remainingLettersCounter[letterOfWord] for letterOfWord, neededCountOfLetter in wordsCounter[index].items()):
                    backtrackingDFS(index+1, remainingLettersCounter-wordsCounter[index], scoreSoFar+scoreOfWords[index])

        backtrackingDFS(0, Counter(letters), 0)
        return maxScoreSeen