

s = "level"

lpsArr = [0 for i in range(len(s))]
prevLpsLength = 0

for i in range (1, len(s)):
    while prevLpsLength!=0 and s[prevLpsLength] != s[i]:
        prevLpsLength = lpsArr[prevLpsLength-1]
    if s[prevLpsLength] != s[i]:
        lpsArr[i] = 0
    else:
        lpsArr[i] = prevLpsLength + 1
        prevLpsLength += 1

print(lpsArr)



s = "level"

lpsArr = [0 for i in range(len(s))]
prevLpsLength = 0
for i in range (1, len(s)):
    while prevLpsLength!=0 and s[prevLpsLength] != s[i]:
        prevLpsLength = lpsArr[prevLpsLength-1]
    if s[prevLpsLength] != s[i]:
        lpsArr[i] = 0
    else:
        lpsArr[i] = prevLpsLength + 1
        prevLpsLength += 1


print("" if lpsArr[len(s)-1]==0 else s[:lpsArr[len(s)-1]])




haystack = "sadbutsad"
needle = "sad"
n = len(haystack)
m = len(needle)
lpsArr = [0 for _ in range(m)]
prevLpsLength = 0
for index in range(1,m):
    while prevLpsLength!=0 and needle[prevLpsLength]!=needle[index]:
        prevLpsLength = lpsArr[prevLpsLength-1]
    if needle[prevLpsLength] != needle[index]:
        lpsArr[prevLpsLength] = 0
    else:
        lpsArr[i] = prevLpsLength + 1
        prevLpsLength += 1
print(lpsArr)   
lengthMatched = 0     
for index in range(0,n):
    while lengthMatched!=0 and needle[lengthMatched] != haystack[index]:
        lengthMatched = lpsArr[lengthMatched-1]
    if needle[lengthMatched] == haystack[index]:
        lengthMatched += 1
        if lengthMatched == m:
            print(index-lengthMatched+1)
            break
print("-1")
    



















