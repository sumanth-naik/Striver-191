# Key Idea 1: Keep stack in increasing order
# Key Idea 2: If a smaller building is seen, pop all bigger ones. Note that current smaller building is the right end of popped building
# Key Idea 3: Element to left of popped one is the left end.

class Solution:
    def largestRectangleArea(self, histogramArr: List[int]) -> int:
        histogramArr = [0] + histogramArr + [0]
        stack, maxArea = [], 0

        for index, height in enumerate(histogramArr):
            while stack and stack[-1][1]>height:
                _, midHeight = stack.pop()
                maxArea = max(maxArea, (index - stack[-1][0] - 1)*(midHeight))
            stack.append((index, height))

        return maxArea

