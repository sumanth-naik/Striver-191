s = "abacaba"

i = 0
j = 0
n = len(s)
maxCount = 0
while j<n:
    if j+1<n:
        if ord(s[j])==ord(s[j+1])-1:
            j += 1
        else:
            maxCount = max(maxCount,j-i+1)
            j += 1
            i = j
    else:
        maxCount = max(maxCount,j-i+1)
        j += 1
print(maxCount)