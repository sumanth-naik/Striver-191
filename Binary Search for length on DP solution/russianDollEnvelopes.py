class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        lisArr = []
        for width, height in sorted(envelopes, key=lambda x: (x[0], -x[1])):
            index = bisect_left(lisArr, height)
            if index==len(lisArr): lisArr.append(height)
            else: lisArr[index] = height
        return len(lisArr)


