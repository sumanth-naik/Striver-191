n = 3
k = 4


def getFactorialsArr(n):
    factsArr = [1]
    for i in range(1, n+1):
        factsArr.append(i * factsArr[i-1])
    return factsArr
        

def getKthPermutation(arr, k, factsArr):
    
    if(len(arr)==0):
        return ""
    
    currElemIndex = k//(factsArr[len(arr)-1])
    remainder = k%(factsArr[len(arr) - 1])
    
    elem = arr[currElemIndex]
    del arr[currElemIndex]
    
    return str(elem) + getKthPermutation(arr, remainder, factsArr)
    
    
print(getKthPermutation([i for i in  range(1,n+1)], k-1, getFactorialsArr(n)))