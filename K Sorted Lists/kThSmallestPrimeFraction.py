# Key Idea: Same as K Sorted Lists

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        minHeap = [(arr[i]/arr[n-1], i, n-1) for i in range(n-1)] # frac, i, j
        heapify(minHeap)
        for _ in range(k):
            _, i, j = heappop(minHeap)
            if j-1>i: heappush(minHeap, (arr[i]/arr[j-1], i, j-1))
        return [arr[i], arr[j]]



# Key Idea: Realize that the numbers are sorted row wise and col wise as well

# Note 1: Its tricky to compute justLowerOrEqual
'''
arr   1   2   3   5

  i   0   1   2   3
j  
0    -/- 1/2 1/3 1/5
1        -/- 2/3 2/5
2            -/- 3/5
3                -/-
'''
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        def numFractionsSmallerThanOrEqual(frac):
            i, j = 0, 1
            count, justLowerOrEqual = 0, (0, 1)
            while i<n-1:
                while j<n and arr[i]/arr[j]>frac:
                    j += 1
                if j==n: break
                # if justLowerOrEqual[0]/justLowerOrEqual[1]<arr[i]/arr[j]: computers dont like floating point divs
                if justLowerOrEqual[0]*arr[j]<justLowerOrEqual[1]*arr[i]:
                    justLowerOrEqual = (arr[i],arr[j])
                count += n-j
                i += 1
            return count, justLowerOrEqual

        low, high = arr[0]/arr[-1], 1.0
        while True:
            mid = (low+high)/2
            # in case ans is 7/11 and we searched with 7/11 + 0.001, 
            # we get count as k and justLowerOrEqual (7, 11)
            count, justLowerOrEqual = numFractionsSmallerThanOrEqual(mid)
            if count==k:
                return justLowerOrEqual
            elif count>k:
                high = mid
            else:
                low = mid


# Key Idea: use bisect to create the border array. Compute justLowerOrEqual using border array.
# This works only when count can be exactly k, else wont termintate. In this case it will be k.
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        low, high, n = arr[0]/arr[-1], 1.0, len(arr)
        while True:
            mid = (low+high)/2
            # get all smallest j such that arr[i]/arr[j]<=mid
            # get all smallest j such that arr[j]>=arr[i]/mid
            border = [bisect_left(arr, arr[i]/mid) for i in range(n)]
            count = sum(n-j for j in border)
            if count<k:
                low = mid
            elif count>k:
                high = mid
            else:
                # get justLowerOrEqual fraction than mid using border
                return max([(arr[i], arr[j]) for i, j in enumerate(border) if j!=n], key = lambda x:x[0]/x[1])