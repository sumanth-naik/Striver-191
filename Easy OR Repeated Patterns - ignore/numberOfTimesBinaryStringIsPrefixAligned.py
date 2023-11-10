# Key Idea: We remove everything we see, thus we should see next number as first number
from sortedcontainers import SortedList
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        sortedList, count, index = SortedList(range(1, len(flips)+1)), 0, 1
        for num in flips:
            sortedList.remove(num)
            if not sortedList or sortedList[0]==index+1:
                count +=1
            index += 1
        return count

# Key Idea: Maintain invalidSet that we bookkeep. When there is not invalid num, inc count
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        invalidSet, count = set(), 0
        for index, num in enumerate(flips):
            if num>index+1:
                invalidSet.add(num)
            invalidSet.discard(index+1)
            count += len(invalidSet)==0
        return count

# Key Idea: We can't inc count if max num we see is greater than index+1
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxSeen, count = 0, 0
        for index, num in enumerate(flips):
            maxSeen = max(maxSeen, num)
            count += index+1==maxSeen
        return count