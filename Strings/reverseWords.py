s = "bl ue"
def reverseWords(s):
    ansString = ""
    currword = ""
    i = len(s) - 1
    while i>=0:
        if i!=len(s)-1 and s[i+1]!=" " and s[i]==" ":
            ansString += ((currword[::-1])+" ")
            currword = ""
        while s[i]==" ":
            i -= 1
        if i>=0:
            currword += s[i]
        i -= 1
    if currword:
        ansString += (currword[::-1])
    if currword[-1]==" ":
        return ansString[0:len(ansString)-1]
    return ansString
print(reverseWords(s))

