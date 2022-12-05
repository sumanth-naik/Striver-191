import copy

def getPermutations(arr, startIndex, allPermsArr):
    
    if(startIndex==len(arr)):
        allPermsArr.append(copy.deepcopy(arr))
    
    for i in range(startIndex, len(arr)):
        arr[i], arr[startIndex] = arr[startIndex], arr[i]
        getPermutations(arr, startIndex + 1, allPermsArr)
        arr[i], arr[startIndex] = arr[startIndex], arr[i]
       
        
arr = [1,2,3]
allPermsArr = []
getPermutations(arr, 0, allPermsArr)
print(allPermsArr)