class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # n, m = len(haystack), len(needle)
        # if m>n: return -1
        # hash_needle = 0
        # hash_haystack_i = 0
        # d, q = 26, 101
        # for i in range(m):
        #     hash_needle = (d*hash_needle + ord(needle[i]))%q
        #     hash_haystack_i = (d*hash_haystack_i + ord(haystack[i]))%q

        # powMod = pow(d,m)%q

        # for i in range(0, n-m+1):
        #     if hash_haystack_i==hash_needle:
        #         if haystack[i:i+m]==needle:
        #             return i
        #     #update
        #     if i+m<n:
        #         hash_haystack_i = (d*hash_haystack_i -ord(haystack[i])*(powMod) +ord(haystack[i+m]))%q
        # return -1
      
        n = len(haystack)
        m = len(needle)
        if m>n: return -1
        lpsArr = [0 for _ in range(m)]
        prevLpsLength = 0
        for index in range(1,m):
            while prevLpsLength!=0 and needle[prevLpsLength]!=needle[index]:
                prevLpsLength = lpsArr[prevLpsLength-1]
            if needle[prevLpsLength] == needle[index]:
                lpsArr[index] = prevLpsLength + 1
                prevLpsLength += 1
        lengthMatched = 0     
        for index in range(0,n):
            while lengthMatched!=0 and needle[lengthMatched] != haystack[index]:
                lengthMatched = lpsArr[lengthMatched-1]
            if needle[lengthMatched] == haystack[index]:
                lengthMatched += 1
                if lengthMatched == m:
                    return(index-lengthMatched+1)
        return -1