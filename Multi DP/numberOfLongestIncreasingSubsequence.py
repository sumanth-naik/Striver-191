class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lengthsOfLIS, countsOfLIS = [1 for _ in range(n)], [1 for _ in range(n)]

        for right in range(n):
            for left in range(right):
                if nums[left]<nums[right]:
                    if lengthsOfLIS[right]==lengthsOfLIS[left]+1:
                        countsOfLIS[right] += countsOfLIS[left]
                    elif lengthsOfLIS[right]<lengthsOfLIS[left]+1:
                        lengthsOfLIS[right] = lengthsOfLIS[left]+1
                        countsOfLIS[right] = countsOfLIS[left]
        
        return sum(count for length, count in zip(lengthsOfLIS,countsOfLIS) if length==max(lengthsOfLIS))
    
import bisect
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        decksArr = []

        for num in nums:
            deckIndex = bisect.bisect_left(decksArr, num, key=lambda deck:deck[-1][0])
            possibleLISEndingWithNum = 1
            if deckIndex>0:
                smallerNumIndexInPrevDeck = bisect.bisect_right(decksArr[deckIndex-1], -num, key=lambda x:-x[0])
                possibleLISEndingWithNum = sum(count for num, count in decksArr[deckIndex-1][smallerNumIndexInPrevDeck:])
                
            if deckIndex==len(decksArr):   
                decksArr.append([(num, possibleLISEndingWithNum)])
            else:
                decksArr[deckIndex].append((num, possibleLISEndingWithNum))
        return sum(count for num, count in decksArr[-1])
    
    
import bisect
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        decksArr, prefixSumsofDecks = [], []
        for num in nums:
            deckIndex = bisect.bisect_left(decksArr, num, key=lambda deck:deck[-1])
            possibleLISEndingWithNum = 1
            if deckIndex>0:
                smallerNumIndexInPrevDeck = bisect.bisect_right(decksArr[deckIndex-1], -num, key=lambda x:-x)
                if smallerNumIndexInPrevDeck==0:
                    possibleLISEndingWithNum = prefixSumsofDecks[deckIndex-1][-1]
                else:
                    possibleLISEndingWithNum = prefixSumsofDecks[deckIndex-1][-1] - prefixSumsofDecks[deckIndex-1][smallerNumIndexInPrevDeck-1]
            
            if deckIndex==len(decksArr):
                decksArr.append([num])
                prefixSumsofDecks.append([possibleLISEndingWithNum])
            else:
                decksArr[deckIndex].append(num)
                prefixSumsofDecks[deckIndex].append(prefixSumsofDecks[deckIndex][-1]+possibleLISEndingWithNum)
        
        return prefixSumsofDecks[-1][-1]

