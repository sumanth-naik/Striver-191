class Solution:
    def maxAbsValExpr(self, arr1, arr2):
        summation1 = [arr1[i]+arr2[i]+i for i in range(len(arr1))]
        summation2 = [arr1[i]-arr2[i]+i for i in range(len(arr1))]
        summation3 = [-arr1[i]+arr2[i]+i for i in range(len(arr1))]
        summation4 = [-arr1[i]-arr2[i]+i for i in range(len(arr1))]

        return max(abs(max(summation1)-min(summation1)), abs(max(summation2)-min(summation2)), abs(max(summation3)-min(summation3)), abs(max(summation4)-min(summation4)))
