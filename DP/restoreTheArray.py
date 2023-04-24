class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        m, n, indexToRemove = len(s), len(str(k)), 0

        slidingWindowNumber = 0
        for i in range(min(m,n)):
            slidingWindowNumber = slidingWindowNumber*10 + int(s[i])

        isSmallerOrEqualArr = [slidingWindowNumber<=k]

        while indexToRemove<m-n:
            indexToAdd = indexToRemove+n
            slidingWindowNumber = slidingWindowNumber*10 + int(s[indexToAdd])
            slidingWindowNumber = slidingWindowNumber%(10**n)
            isSmallerOrEqualArr.append(slidingWindowNumber<=k)
            indexToRemove += 1

        @lru_cache(None)
        def recursion(i):
            if i>=m or s[i]=="0": return 0
            count = 0
            if i>m-n or (i==m-n and isSmallerOrEqualArr[i]):
                count = 1
            elif isSmallerOrEqualArr[i]:
                count = recursion(i+n)
            return (count + sum(recursion(j) for j in range(i+1, i+n))) % (10**9+7)
        return recursion(0)