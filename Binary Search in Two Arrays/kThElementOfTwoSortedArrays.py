
class Solution:
    def kthElement(self, arr1, arr2, n, m, k):
        if len(arr1)>len(arr2): return self.kthElement(arr2, arr1, m, n, k)

        # lowest number of numbers to take and highest to take
        # in lowest.. take everything from second arr... see what we need to take at minimum
        # in highest.. take everything from first arr
        low, high = max(0, k-m), min(n,k)
        while low<=high:
            numElementsFromArr1 = (low+high)//2
            numElementsFromArr2 = k - numElementsFromArr1
            
            l1 = arr1[numElementsFromArr1-1] if numElementsFromArr1-1>=0 else -1e9
            l2 = arr2[numElementsFromArr2-1] if numElementsFromArr2-1>=0 else -1e9
            r1 = arr1[numElementsFromArr1] if numElementsFromArr1<n else 1e9
            r2 = arr2[numElementsFromArr2] if numElementsFromArr2<m else 1e9

            if l1<=r2 and l2<=r1: return max(l1, l2)
            elif l1>r2: high = numElementsFromArr1-1
            else: low = numElementsFromArr1+1
