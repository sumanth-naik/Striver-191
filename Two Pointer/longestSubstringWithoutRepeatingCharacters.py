def lengthOfLongestSubstring(s: str) -> int:
    
    charSet = set()
    i,j  = 0,0
    n = len(s)
    if n==0: return 0
    maxLen = 1
    while(j<n):
        if s[j] in charSet:
            while s[i]!=s[j]:
                charSet.remove(s[i])
                i += 1
            i+= 1

        charSet.add(s[j])
        maxLen = max(maxLen,j-i+1)
        j += 1

    return maxLen
s = "abcabcbb"
print(lengthOfLongestSubstring(s))