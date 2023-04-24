
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


class Solution:
    def findMedianSortedArrays(self, arr1, arr2) -> float:
        # make sure first is smaller, because, its easier to define low and high.. if not you will have to 
        # calaulate whats the valid range of low and high
        if len(arr1)>len(arr2): return self.findMedianSortedArrays(arr2, arr1)
        
        m, n = len(arr1), len(arr2)
        # write code such that mid should point to number of numbers chosen from arr1
        # hence mid should be able to go to 0 and m
        # low and high indicates the minimum and maximum number of numbers to take respectively.
        low, high, isTotalOdd = 0, m, (m+n)%2
        while low<=high:
            numMembersFromArr1 = (low+high)//2
            # if odd total, left will have one lesser number, right will have one greater number
            numMembersFromArr2 = (m+n)//2 - numMembersFromArr1
            # if numMembersFromArr1 elems are chosen, that means elems till index numMembersFromArr1-1 are chosen
            l1 = arr1[numMembersFromArr1-1] if numMembersFromArr1-1>=0 else -1e9
            r1 = arr1[numMembersFromArr1] if numMembersFromArr1<m else 1e9
            l2 = arr2[numMembersFromArr2-1] if numMembersFromArr2-1>=0 else -1e9
            r2 = arr2[numMembersFromArr2] if numMembersFromArr2<n else 1e9
            # if odd, since right will have one greater number, choose from right side
            if l1<=r2 and l2<=r1: return min(r1, r2) if isTotalOdd else (max(l1, l2) + min(r1, r2))/2
            # we just verified that numMembersFromArr1 members wont work, so subtract this in binary search step
            elif l1>r2: high = numMembersFromArr1-1
            # we used mid to be (low+high)//2, so not subtracting this can result in inf loop when low+1==high
            else: low = numMembersFromArr1+1


            
            







