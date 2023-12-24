# Key Idea 1: Use Largest Rectangle in Histogram Idea
# Key Idea 2: Use prefixSum approach to compute all histogram arrays

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        def solveHistogram(arr):
            arr = [0] + arr + [0]
            stack, maxArea = [], 0
            for index, height in enumerate(arr):
                while stack and stack[-1][1]>height:
                    _, midHeight = stack.pop()
                    maxArea = max(maxArea, (index - stack[-1][0] - 1)*(midHeight))
                stack.append((index, height))
            return maxArea

        m, n = len(matrix), len(matrix[0])
        histMat = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
        for j in range(n):
            for i in range(1, m):
                if histMat[i][j]: 
                    histMat[i][j] += histMat[i-1][j]
        return max(map(solveHistogram, histMat))