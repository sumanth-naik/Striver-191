# Key Idea: At each index, find the middle portion and then expand

class Solution:
    def longestPalindrome(self, s: str) -> str:

        longestPalindromeTuple = (0, 0)
        n = len(s)
        for i in range(n):

            right = i + 1
            while right < n and s[right - 1] == s[right]: # middle portion
                right += 1

            left = i - 1
            while left >= 0 and right < n and s[left] == s[right]: # extend
                left -= 1
                right += 1

            if longestPalindromeTuple[1] - longestPalindromeTuple[0] + 1 < right - left - 1:
                longestPalindromeTuple = (left + 1, right - 1)

        return s[longestPalindromeTuple[0]:longestPalindromeTuple[1] + 1]


''' Other ways '''
# Key Idea: There is monotonicity in palindrome lengths, but in parity

# Binary search on answer with parity O(n^2 logn)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, startAndEndIndicesOfLongestPalindrome = len(s), (0, 1)

        def getStartIndexWithPalindromeOfLength(length):
            for start in range(n - length + 1):
                if s[start:start + length] == s[start:start + length][::-1]: return start
            return None

        for parity in [0, 1]:
            low, high = 1, n
            if low % 2 != parity: low += 1
            if high % 2 != parity: high -= 1
            while low <= high:
                mid = (low + high) // 2
                if mid % 2 != parity: mid += 1
                startIndex = getStartIndexWithPalindromeOfLength(mid)
                if startIndex is not None:
                    if startAndEndIndicesOfLongestPalindrome[1] - startAndEndIndicesOfLongestPalindrome[0] < mid:
                        startAndEndIndicesOfLongestPalindrome = (startIndex, startIndex + mid)
                    low = mid + 2
                else:
                    high = mid - 2

        return s[startAndEndIndicesOfLongestPalindrome[0]:startAndEndIndicesOfLongestPalindrome[1]]


# Key Idea: lpsArr in Manacher's stores the lengths of palindrome 

# Manacher's Algo
class Solution:
    def longestPalindrome(self, s: str) -> str:
        newStr = "$#" + ''.join(s[i]+"#" for i in range(len(s))) + "@"
        lpsArr = [0 for _ in range(len(newStr))]

        center, right = 0, 0
        for index in range(1, len(newStr)-1):
            if index<right:
                mirror = 2*center - index
                lpsArr[index] = min(right-index, lpsArr[mirror])

            while newStr[index+lpsArr[index]+1]==newStr[index-lpsArr[index]-1]:
                lpsArr[index]+=1

            if right<index+lpsArr[index]:
                center = index
                right = index+lpsArr[index]

        maxLen, centerIndex = max((l, i) for i,l in enumerate(lpsArr))
        return ''.join(newStr[index] for index in range(centerIndex-maxLen, centerIndex+maxLen) if newStr[index]!="#")

