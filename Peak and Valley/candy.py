class Solution:
    def candy(self, ratings: List[int]) -> int:
        ratingToIndices = defaultdict(list)
        for index, rating in enumerate(ratings):
            ratingToIndices[rating].append(index)
        sortedRatings = sorted(ratingToIndices.keys())

        n = len(ratings)
        ansArr = [0 for _ in range(n)]
        for rating in sortedRatings:
            indexToValMap = defaultdict(int)
            for index in ratingToIndices[rating]:
                indexToValMap[index] = 1 + max((ansArr[index+1] if index+1<n else 0), (ansArr[index-1] if index-1>=0 else 0))
            for index, val in indexToValMap.items():
                ansArr[index] = val
        return sum(ansArr)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ansArr = [1 for _ in range(n)]
        for index in range(1, n):
            if ratings[index]>ratings[index-1]: ansArr[index] = ansArr[index-1]+1
        for index in range(n-2, -1, -1):
            if ratings[index]>ratings[index+1]: ansArr[index] = max(ansArr[index], ansArr[index+1]+1)
        return sum(ansArr)
        


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        # give 1 candy to each
        numCandies, index = n, 1

        while index<n:
            if ratings[index]==ratings[index-1]:
                index += 1
                continue

            # increasing slope
            peak = 0
            while index<n and ratings[index]>ratings[index-1]:
                peak += 1
                numCandies += peak
                index += 1

            # decreasing slope
            valley = 0
            while index<n and ratings[index]<ratings[index-1]:
                valley += 1
                numCandies += valley
                index += 1
                
            # deal with giving candies twice to peak
            numCandies -= min(peak, valley)
        return numCandies