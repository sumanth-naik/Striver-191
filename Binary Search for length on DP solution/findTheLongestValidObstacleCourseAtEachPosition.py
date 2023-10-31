# Key Idea: Question screams Longest Increasing Subsequence

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        longestObstaclesArr = []
        for height in obstacles:
            index = bisect.bisect_right(longestObstaclesArr, height)
            if index==len(longestObstaclesArr): longestObstaclesArr.append(height)
            else: longestObstaclesArr[index] = height
            yield index+1