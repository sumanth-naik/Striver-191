class Solution:
    def wordBreak(self, s: str, wordDict):
        wordDict, ansArr, n  = set(wordDict), [], len(s)

        def recursion(i, j, currentStr):
            nonlocal ansArr
            if j==n:
                if i==j: ansArr.append(currentStr[:len(currentStr)-1])
            else:
                if s[i:j+1] in wordDict:
                    recursion(j+1, j+1, currentStr + s[i:j+1] + " ")
                recursion(i, j+1, currentStr)

        recursion(0, 0, "")
        return ansArr