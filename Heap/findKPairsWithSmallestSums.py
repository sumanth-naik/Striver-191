import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minHeap, ansArr, visited, m, n = [(nums1[0]+nums2[0], 0, 0)], [], {(0,0)}, len(nums1), len(nums2)
        while len(ansArr)<k and minHeap:
            pairSum, i, j = heapq.heappop(minHeap)
            ansArr.append((nums1[i], nums2[j]))
            if i+1<m and (i+1, j) not in visited: 
                visited.add((i+1, j))
                heapq.heappush(minHeap, (nums1[i+1]+nums2[j], i+1, j))
            if j+1<n and (i, j+1) not in visited: 
                visited.add((i, j+1))
                heapq.heappush(minHeap, (nums1[i]+nums2[j+1], i, j+1))
        return ansArr

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

