# Key Idea 1: Identify that sums form K sorted Lists
# Key Idea 2: We dont need to add first entire col to heap first. We can make i,j add i+1,j
 
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minHeap, ansArr, m, n = [(nums1[0]+nums2[0], 0, 0)], [], len(nums1), len(nums2)
        while len(ansArr)<k and minHeap:
            _, i, j = heapq.heappop(minHeap)
            ansArr.append((nums1[i], nums2[j]))
            if j==0 and i+1<m: heapq.heappush(minHeap, (nums1[i+1]+nums2[j], i+1, j)) # only first elems add below row elem to heap
            if j+1<n: heapq.heappush(minHeap, (nums1[i]+nums2[j+1], i, j+1)) # add right elem always. No need of visited set
        return ansArr
