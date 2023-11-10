# Key Idea 1: Dp was obvious. Instead of having a second index of "j", looping inside dp is simpler
# Key Idea 2: impValsDp uses a combo of hash map and count variable. Count variable removes need to iterate hashmap for populating impValsDp[i][j]

class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        impValsDp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            counter, count = defaultdict(int), 0
            for j in range(i, n):
                counter[nums[j]] += 1
                if counter[nums[j]]==2: count += 2
                elif counter[nums[j]]>2: count += 1
                impValsDp[i][j] = k + count

        @cache
        def dp(fromIndex):
            if fromIndex==n: return 0
            return min(impValsDp[fromIndex][toIndex] + dp(toIndex+1) for toIndex in range(fromIndex, n))

        return dp(0)