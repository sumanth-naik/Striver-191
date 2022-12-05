
def getMedianOfSortedArrays(arr1, arr2):
    if(len(arr1)>len(arr2)):
        return getMedianOfSortedArrays(arr2,arr1)
    m = len(arr1)
    n = len(arr2)
    minNumElemsFromArr1 = (m+n+1)//2 - n
    low = max(minNumElemsFromArr1-1, -1)
    maxNumElemsFromArr1 = (m+n+1)//2
    high = min(maxNumElemsFromArr1-1, m-1)
    while(True):
        mid = (low+high)//2
        l1 = arr1[mid] if (mid>=0) else -1e9
        r1 = arr1[mid+1] if mid+1<=m-1 else 1e9
        l2 = arr2[(m+n+1)//2 - mid - 2] if ((m+n+1)//2 - mid - 2)>=0 else -1e9
        r2 = arr2[(m+n+1)//2 - mid - 1] if ((m+n+1)//2 - mid - 1)<=n-1 else 1e9
        if(l1<=r2 and l2<=r1):
            if((m+n)%2==0):
                return (max(l1,l2) + min(r1,r2))/ 2
            else:
                return max(l1,l2)
        
        elif(l1>r2):
            high = mid
        
        else:
            low = mid + 1

    
arr1 = [2,3,4,5]
arr2 = [1]

print(getMedianOfSortedArrays(arr1, arr2))