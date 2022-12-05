import copy

def pprint(arr):
    for x in arr:
        print(x)
    print("////")
def ppprint(arr):
    for x in arr:
        for y in x:
            print(y)
        print("--")
    print(".........")
    
    
def isValidIndex(i, j, m, n):
    if(i<0 or i>=m):
        return False
    if(j<0 or j>=n):
        return False
    return True

def isValid(arr, i, j):
        
    m = len(arr)
    n = len(arr[0])
    
    for x in range(0, len(arr)):
        #col check
        if(arr[x][j])==1:
            return False
        #left diagonal on top left side (bottom right not required)
        if(isValidIndex(i-x, j-x, m, n) and arr[i-x][j-x]==1):
            return False
        #right diagonal on top right side (bottom left not required)
        if(isValidIndex(i-x, j+x, m, n) and arr[i-x][j+x]==1):
            return False
            
    return True       
            

def nQueens(arr, i, possibleArrangements):

    if(i==len(arr)):
        possibleArrangements.append(copy.deepcopy(arr))
        return 1
    
    count = 0
    for j in range(0, len(arr)):
        if(isValid(arr, i, j)):
            arr[i][j] = 1
            count += nQueens(arr, i+1, possibleArrangements)
            arr[i][j] = 0
            
    return count
    


def mirrorArr(arr):    
    for row in arr:
        row.reverse()

def transpose(arr):
    for i in range(1, len(arr)):
        for j in range(0, i):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    
def leftRotateArr(arr):
    mirrorArr(arr)
    transpose(arr)
    return arr

def isNewArrangement(arr, possibleDistinctArrangements):
    arrCopy = copy.deepcopy(arr)
    
    if(leftRotateArr(arrCopy) in possibleDistinctArrangements
       or leftRotateArr(arrCopy) in possibleDistinctArrangements
       or leftRotateArr(arrCopy) in possibleDistinctArrangements
       or leftRotateArr(arrCopy) in possibleDistinctArrangements):
        return False
    
    mirrorArr(arrCopy)
    if(arrCopy in possibleDistinctArrangements):
        return False
    if(leftRotateArr(arrCopy) in possibleDistinctArrangements
       or leftRotateArr(arrCopy) in possibleDistinctArrangements
       or leftRotateArr(arrCopy) in possibleDistinctArrangements):
        return False

    return True

def nQueensDistinct(arr, i, possibleDistinctArrangements):

    if(i==len(arr)):
        if(isNewArrangement(arr, possibleDistinctArrangements)):
            possibleDistinctArrangements.append(copy.deepcopy(arr))
            return 1
            
    count = 0
    for j in range(0, len(arr)):
        if(isValid(arr, i, j)):
            arr[i][j] = 1
            count += nQueensDistinct(arr, i+1, possibleDistinctArrangements)
            arr[i][j] = 0
            
    return count
    



for n in range(1,10):
    print("n = ",n)
    arr = [[0 for x in range(0, n)] for y in range(0,n)]
    possibleArrangements = []
    count = nQueens(arr, 0, possibleArrangements)
    
    stringsArr = []
    for x in possibleArrangements:
        stringArr = []
        for y in x:
            s = ""
            for z in y:
                if z==1:
                    s = s + "Q"
                else:
                    s = s + "."
            stringArr.append(s)
        stringsArr.append(stringArr)
            
    print(count)
    #ppprint(possibleArrangements)
    
    arr = [[0 for x in range(0, n)] for y in range(0,n)]
    possibleDistinctArrangements = []
    count = nQueensDistinct(arr, 0, possibleDistinctArrangements)
    print(count)
    
    # https://math.stackexchange.com/questions/1872444/how-many-solutions-are-there-to-an-n-by-n-queens-problem

