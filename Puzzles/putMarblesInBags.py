class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k==1: return 0
        sortedPairSums = sorted([weights[i]+weights[i+1] for i in range(len(weights)-1)])
        return sum(sortedPairSums[len(sortedPairSums)-k+1:]) - sum(sortedPairSums[:k-1])
    
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pairSums = [weights[i]+weights[i+1] for i in range(len(weights)-1)]
        return sum(nlargest(k-1, pairSums)) - sum(nsmallest(k-1, pairSums))
    

    
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        pairSums = [weights[i]+weights[i+1] for i in range(len(weights)-1)]
        n, k = len(pairSums), k-1

        def quickSelect(k):
            nonlocal pairSums
            if k==0: return pairSums
            low, pivot = 0, n-1
            while low<=pivot:
                swapPointer = low
                for index in range(low, pivot):
                    if pairSums[index]<pairSums[pivot]:
                        pairSums[swapPointer], pairSums[index] = pairSums[index], pairSums[swapPointer]
                        swapPointer += 1
                
                pairSums[swapPointer], pairSums[pivot] = pairSums[pivot], pairSums[swapPointer]
                numberOfNumbersSmallerOrEqualToPivotNumber = swapPointer-low+1

                if numberOfNumbersSmallerOrEqualToPivotNumber==k:
                    return pairSums
                elif numberOfNumbersSmallerOrEqualToPivotNumber<k:
                    k -= numberOfNumbersSmallerOrEqualToPivotNumber
                    low = swapPointer + 1
                else:
                    pivot = swapPointer - 1 

        return sum(quickSelect(n-k)[n-k:])-sum(quickSelect(k)[:k])

