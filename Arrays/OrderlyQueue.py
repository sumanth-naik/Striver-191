
s = "cbaabaaac"
k = 2
def getMinString(s,k):
    if k>1:
        return ''.join(sorted(s))
    else:
        minStringSoFar = s
        for i in range(len(s)):
            rotatedString = s[i:]+s[:i]
            if(rotatedString<minStringSoFar):
                minStringSoFar = rotatedString
        return minStringSoFar
    
print(getMinString(s,k))