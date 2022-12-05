



def countReversePairs(low, mid, high, arr, ans):
    i = low
    j = mid + 1    
    for i in range(low, mid + 1):
        while(j <= high and arr[i] > 2 * arr[j]):
            j = j + 1
        ans[0] = ans[0] + (j - (mid + 1))

def merge(low, mid, high, arr, temp):
    i = low
    j = mid + 1
    k = low
    while(i <= mid and j <= high):
        if(arr[i]<=arr[j]):
            temp[k] = arr[i]
            k = k + 1
            i = i + 1
        else:
            temp[k] = arr[j]
            k = k + 1
            j = j + 1
            
    while(i <= mid):
        temp[k] = arr[i]
        k = k + 1
        i = i + 1
        
    while(j <= high):
        temp[k] = arr[j]
        k = k + 1
        j = j + 1
        
    for x in range(low, high + 1):
        arr[x] = temp[x]


def mergeSortHelper(low, high, arr, temp, ans):
    if(low == high):
        return arr, ans
    
    mid = (low + high)//2
    
    mergeSortHelper(low, mid, arr, temp, ans)
    mergeSortHelper(mid + 1, high, arr, temp, ans)
    
    countReversePairs(low, mid, high, arr, ans)
    merge(low, mid, high, arr, temp)
    
    return arr, ans

def mergeSort(arr):
    temp = [None] * len(arr)
    return mergeSortHelper(0,len(arr)-1, arr, temp, [0])
    
    
    
arr = [3,2,1,4]
print(mergeSort(arr))
