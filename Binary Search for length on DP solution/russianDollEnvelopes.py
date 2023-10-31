# Key Idea 1: We can pick only one envelope of a given width
# Key Idea 2: We sort by (x[0], -x[1]) to convert the question to LIS
#    Ex: [1,3],[3,5],[6,8],[6,7],[8,4], we work with [3,5,8,7,4] and look for LIS
#           Sorting height in desc order will ensure we only pick one env of same width

# Note: 3D variant (Maximum Height by Stacking Cuboids) needs proper DP

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        lisArr = []
        for width, height in sorted(envelopes, key=lambda x: (x[0], -x[1])):
            index = bisect_left(lisArr, height)
            if index==len(lisArr): lisArr.append(height)
            else: lisArr[index] = height
        return len(lisArr)


