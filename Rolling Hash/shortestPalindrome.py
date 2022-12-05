
s = "aabaabcd"
def shortestPalindrome(s):
    rollingHashesSet = set()
    rollingHash = 0
    n = len(s)
    d, q = 26, 101
    for i in range(0, n):
        rollingHash = (rollingHash*d+ord(s[i]))%q
        rollingHashesSet.add(rollingHash)
    print(rollingHashesSet)

    powerModMap = [1 for _ in range(n)]
    for i in range(1,n):
        powerModMap[i] = (powerModMap[i-1]*d)%q
    print(powerModMap)

    reverseRollingHash = 0
    maxLenPalindrome = 0
    revString = s[::-1]
    for i in range(n-1,-1,-1):
        reverseRollingHash = (reverseRollingHash + powerModMap[n-1-i]*ord(revString[i]))%q
        if reverseRollingHash in rollingHashesSet:
            if s[:n-i]==revString[i:]:
                maxLenPalindrome = max(maxLenPalindrome, n-i)
    return (revString[:n-maxLenPalindrome]+s)
    
print(shortestPalindrome(s))

def shortestPalindromeBest(s):
    n = len(s)
    d, q = 26, 101
    powMod = 1
    hashS = 0
    hashReverseS = 0
    reverseS = s[::-1]
    maxIndex = 0
    for i in range(n):
        hashS = (d*hashS + ord(s[i]))%q
        hashReverseS = (hashReverseS + ord(s[i])*powMod)%q
        if hashS==hashReverseS:
            if s[:i+1] == reverseS[n-i-1:]:
                maxIndex = max(maxIndex, i)
        powMod = (powMod*d)%q
    return reverseS[:n-maxIndex-1]+s
print(shortestPalindromeBest(s))




