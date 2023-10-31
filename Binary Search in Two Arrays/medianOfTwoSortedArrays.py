# Key Idea 1: Binary search on numElementsFromArr1, accordingly define low and high
# Key Idea 2: monotonicity is on l1<=r2 and l2<=r1 behaviour

# Note: Take care of odd and even case for median

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


            
            







