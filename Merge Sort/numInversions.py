arr = [2, 5, 1, 3, 4]


def merge(arr, left, right, temp, inversions):
    
    i = left
    mid = (left+right)//2
    j = mid + 1
    k = left
    
    while(i<=mid and j<=right):
        if(arr[i]<=arr[j]):
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1         
            inversions[0] = inversions[0] + (mid - i + 1)
            
    while(i<=mid):
        temp[k] = arr[i]
        k += 1
        i += 1
  
    while(j<=right):
        temp[k] = arr[j]
        k += 1
        j += 1 
        inversions[0] = inversions[0] + (mid - i + 1)

    for index in range(left, right+1):
        arr[index] = temp[index]
            

def mergeSort(arr, left, right, tempArr, inversions):
    
    if(left==right):
        return arr[left]
    
    mid = (left+right)//2
    
    mergeSort(arr, left, mid, tempArr, inversions)
    mergeSort(arr, mid+1, right, tempArr, inversions)
    
    merge(arr, left, right, tempArr, inversions)
    
    return arr



def countInversions(arr, n):
    inversions = [0]
    print(mergeSort(arr,0,n-1,[0 for x in range(0,n)],inversions))
    print(inversions[0])
    
countInversions(arr, len(arr)) 
    