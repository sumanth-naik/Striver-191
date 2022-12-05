
s = " -2-11 + 2 +0 +  14 "

def adder(runningSum, numString, minus):
    if minus:
        return runningSum - int(numString)
    return runningSum + int(numString)

def noBracketsEval(s):
    runningSum = 0
    minus = False
    numString = "0"
    for ch in s:
        if ch==" ":
            continue
        elif ch=="+":
            runningSum = adder(runningSum, numString, minus)
            numString = "0"
            minus = False
        elif ch=="-":
            runningSum = adder(runningSum, numString, minus)
            numString = "0"
            minus = True
        else:
            numString+=ch
    runningSum = adder(runningSum, numString, minus)
    return runningSum

#print(noBracketsEval(s))





def withBracketEval(s, startIndex):
    runningSum = 0
    minus = False
    numString = "0"
    i = startIndex
    while(i<len(s)):
        if s[i]==" ":
            i += 1
            continue
        elif s[i]=="+":
            runningSum = adder(runningSum, numString, minus)
            numString = "0"
            minus = False
        elif s[i]=="-":
            runningSum = adder(runningSum, numString, minus)
            numString = "0"
            minus = True
        elif s[i]=="(":
            bracketVal,bracketEndIndex = withBracketEval(s, i+1)
            runningSum = adder(runningSum, str(bracketVal), minus)
            i = bracketEndIndex
            numString = "0"
            minus = False
        elif s[i]==")":
            runningSum = adder(runningSum, numString, minus)
            return runningSum, i
        else:
            numString += s[i]
        i += 1

    runningSum = adder(runningSum, numString, minus)
    return runningSum

s = " -(-2-1)-1"

print(withBracketEval(s,0))    



