s = "ababbbabbaba"
reversedString = s[::-1]

n = len(s)
lpsArr = [0 for _ in range(n)]
prevLpsLength = 0
for i in range(1,n):
    while prevLpsLength!=0 and s[prevLpsLength]!=s[i]:
        prevLpsLength = lpsArr[prevLpsLength-1]
    if s[prevLpsLength]!=s[i]:
        lpsArr[i] = 0
    else:
        lpsArr[i] = prevLpsLength + 1
        prevLpsLength += 1

lengthMatched = 0
for i in range(0,n):
    while lengthMatched!=0 and reversedString[i]!=s[lengthMatched]:
        lengthMatched = lpsArr[lengthMatched-1]
    if reversedString[i]==s[lengthMatched]:
        lengthMatched += 1
        
print(s,reversedString,s[:lengthMatched],reversedString[:n-lengthMatched])
print(reversedString[:n-lengthMatched]+s)
        
    
    
        
        
        
        
        
        
        
        