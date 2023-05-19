def longestPalindrome(s: str) -> str:
    
    longestPalindromeTuple = (0,0)
    n = len(s)
    for i in range(n):
        
        right = i+1
        while right<n and s[right-1]==s[right]:
            right += 1
        
        left = i-1
        while left>=0 and right<n and s[left]==s[right]:
            left -= 1
            right += 1
            
        if longestPalindromeTuple[1]-longestPalindromeTuple[0]+1 < right-left-1:
            longestPalindromeTuple = (left+1, right-1)
    
    return s[longestPalindromeTuple[0]:longestPalindromeTuple[1]+1]

# Binary search on answer with parity O(n^2 logn)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, startAndEndIndicesOfLongestPalindrome = len(s), (0,1)

        def getStartIndexWithPalindromeOfLength(length):
            for start in range(n-length+1):
                if s[start:start+length]==s[start:start+length][::-1]: return start
            return None

        for parity in [0,1]:
            low, high = 1, n
            if low%2!=parity: low+=1
            if high%2!=parity: high-=1
            while low<=high:
                mid = (low+high)//2
                if mid%2!=parity: mid+=1
                startIndex = getStartIndexWithPalindromeOfLength(mid)
                if startIndex is not None:
                    if startAndEndIndicesOfLongestPalindrome[1]-startAndEndIndicesOfLongestPalindrome[0]<mid:
                        startAndEndIndicesOfLongestPalindrome = (startIndex, startIndex+mid)
                    low = mid + 2
                else:
                    high = mid - 2

        return s[startAndEndIndicesOfLongestPalindrome[0]:startAndEndIndicesOfLongestPalindrome[1]]

