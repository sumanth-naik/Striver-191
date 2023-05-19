class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        m, n, MOD = len(nums1), len(nums2), 10**9+7

        @lru_cache(None)
        def recursion(i, j, turn):
            if not turn:
                if i == m: return 0
                jNext = bisect_left(nums2, nums1[i], j, n)
                return max(nums1[i] + recursion(i + 1, j, turn), recursion(i + 1, jNext, not turn) if jNext < n and nums2[jNext] == nums1[i] else 0)
            else:
                if j == n: return 0
                iNext = bisect_left(nums1, nums2[j], i, m)
                return max(nums2[j] + recursion(i, j + 1, turn), recursion(iNext, j + 1, not turn) if iNext < m and nums1[iNext] == nums2[j] else 0)

        return max(recursion(0, 0, True), recursion(0, 0, False))%MOD

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        i = j = currSum1 = currSum2 = totalSum = 0
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                currSum1 += nums1[i]
                i+=1
            elif nums1[i]>nums2[j]:
                currSum2 += nums2[j]
                j+=1
            else:
                totalSum += (max(currSum1, currSum2) + nums1[i])%(10**9+7)
                i+=1
                j+=1
                currSum1 = currSum2 = 0

        currSum1 += sum(nums1[i:])
        currSum2 += sum(nums2[j:])
        return (totalSum + max(currSum1, currSum2))%(10**9+7)