class Solution:
    def longestPalindrome(self, s: str) -> str:

        longestPalindromeTuple = (0, 0)
        n = len(s)
        for i in range(n):

            right = i + 1
            while right < n and s[right - 1] == s[right]:
                right += 1

            left = i - 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            if longestPalindromeTuple[1] - longestPalindromeTuple[0] + 1 < right - left - 1:
                longestPalindromeTuple = (left + 1, right - 1)

        return s[longestPalindromeTuple[0]:longestPalindromeTuple[1] + 1]


#         n = len(s)
#         dp1 = [1 for _ in range(n)]
#         dp2 = [1 for _ in range(n)]
#         dp3 = [0 for _ in range(n)]

#         longestPalindrome = (0,0)

#         for diffInIAndJ in range(1,n):
#             for row in range(0,n-diffInIAndJ):
#                 if s[row]==s[row+diffInIAndJ] and dp1[row+diffInIAndJ-1]:
#                    dp3[row+diffInIAndJ] = 1

#                    if longestPalindrome[1] - longestPalindrome[0]<diffInIAndJ:
#                        longestPalindrome = (row,row+diffInIAndJ)
#                 else:
#                     dp3[row+diffInIAndJ] = 0
#             dp3,dp2,dp1 = [0 for _ in range(n)],dp3,dp2

#         return s[longestPalindrome[0]:longestPalindrome[1]+1]


#         n = len(s)
#         dp = [[0 for _ in range(n)] for _ in range(n)]
#         for i in range(0,n-1):
#             dp[i][i] = 1
#             dp[i+1][i] = 1
#         dp[n-1][n-1] = 1

#         longestPalindrome = (0,0)

#         for diffInIAndJ in range(1,n):
#             for row in range(0,n-diffInIAndJ):
#                 if s[row]==s[row+diffInIAndJ] and dp[row+1][row+diffInIAndJ-1]:
#                    dp[row][row+diffInIAndJ] = 1

#                    if longestPalindrome[1] - longestPalindrome[0]<diffInIAndJ:
#                        longestPalindrome = (row,row+diffInIAndJ)


#         return s[longestPalindrome[0]:longestPalindrome[1]+1]


#         n = len(s)
#         dp = [[-1 for _ in range(n)] for _ in range(n)]
#         longestPalindrome = (0,0)
#         for i in range(n):
#             for j in range(i,n):
#                 if isPalindrome(s, i, j, dp) and longestPalindrome[1] - longestPalindrome[0] <j-i:
#                     longestPalindrome = (i,j)

#         return s[longestPalindrome[0]:longestPalindrome[1]+1]


# def isPalindrome(s,i,j, dp):
#     if i>=len(s) or j<0:
#         return True
#     if dp[i][j] == -1:
#         if i>=j:
#             dp[i][j] = True
#         else:
#             dp[i][j] = s[i]==s[j] and isPalindrome(s,i+1,j-1,dp)

#     return dp[i][j]


#         combinedReverseString = s + "#" + s[::-1]
#         longestPalindrome = ""
#         for index in range(len(s)):
#             length = lengthOfLongestPalindromeFromIndex(index, combinedReverseString)
#             if(len(longestPalindrome)<length):
#                 longestPalindrome = s[index:index+length]
#             if(length==len(s)-index):
#                 return longestPalindrome
#         return(longestPalindrome)


# def lengthOfLongestPalindromeFromIndex(index, combinedReverseString):
#     n = len(combinedReverseString) - 2*index
#     lpsArr = [0 for _ in range(n)]
#     prevLpsLength = 0
#     for i in range(1, n):
#         while prevLpsLength!=0 and combinedReverseString[index+prevLpsLength]!=combinedReverseString[i+index]:
#             prevLpsLength = lpsArr[prevLpsLength-1]
#         if combinedReverseString[index+prevLpsLength]!=combinedReverseString[i+index]:
#             lpsArr[i] = 0
#         else:
#             lpsArr[i] = prevLpsLength + 1
#             prevLpsLength += 1
#     return lpsArr[n-1]


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


# Manacher's Algo O(n)
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

