chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

def stringCompression(chars):
    if(len(chars)<=1):
        return chars
    count = 0
    currentArrayIndex = 0
    prevChar = None
    for x in chars:
        if(prevChar==None):
            prevChar = x
            count = 1
            continue
        else:
            if(prevChar==x):
                count = count + 1
            elif(count==1):
                chars[currentArrayIndex] = prevChar
                currentArrayIndex += 1
                prevChar = x
                count = 1

            else:
                chars[currentArrayIndex] = prevChar
                currentArrayIndex += 1 
                prevChar = x
                countString = str(count)
                for num in countString:
                    chars[currentArrayIndex] = num
                    currentArrayIndex += 1 
                count=1
                
    
    if(count==1):
        chars[currentArrayIndex] = prevChar
        currentArrayIndex += 1
        prevChar = x
        count = 1

    else:
        chars[currentArrayIndex] = prevChar
        currentArrayIndex += 1 
        prevChar = x
        countString = str(count)
        for num in countString:
            chars[currentArrayIndex] = num
            currentArrayIndex += 1 

    return (chars[:currentArrayIndex])


print(stringCompression(chars))