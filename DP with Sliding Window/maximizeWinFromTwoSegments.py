class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        prevBest, totalBest, n = 0, 0, len(prizePositions)
        for index, num in enumerate(prizePositions):
            if index!=0:
                if num==prizePositions[index-1]: continue
                prevBest = max(prevBest, index - bisect_left(prizePositions, prizePositions[index-1]-k, 0, index))
            totalBest = max(totalBest, prevBest+bisect_right(prizePositions, num+k, index, n)-index)
        return totalBest

class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        prevBest, totalBest, index, n = 0, 0, 0, len(prizePositions)
        while index<n:
            totalBest = max(totalBest, prevBest + bisect_right(prizePositions, prizePositions[index]+k, index, n)-index)
            index = bisect_right(prizePositions, prizePositions[index], index+1, n)
            prevBest = max(prevBest, index - bisect_left(prizePositions, prizePositions[index-1]-k, 0, index))
        return totalBest


class Solution:
    def maximizeWin(self, nums: List[int], k: int) -> int:
        dpOfBestWindowSeenBefore, totalBest, windowStart = [0]*(len(nums)+1), 0, 0
        for windowEnd, num in enumerate(nums):
            while nums[windowEnd]-nums[windowStart]>k: windowStart += 1
            dpOfBestWindowSeenBefore[windowEnd+1] = max(dpOfBestWindowSeenBefore[windowEnd], windowEnd-windowStart+1)
            totalBest = max(totalBest, windowEnd-windowStart+1 + dpOfBestWindowSeenBefore[windowStart]) # 2nd window ends now 
        return totalBest