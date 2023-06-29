class Solution:
    def maxJump(self, stones: List[int]) -> int:
        maxJump = stones[1] - stones[0]
        for i in range(len(stones)-2):
            maxJump = max(maxJump, stones[i+2]-stones[i])
        return maxJump
    

class Solution:
    def maxJump(self, stones: List[int]) -> int:

        def isValidMaxJumpHelper(maxJump, stones):
            startIndex, endIndex, usedStones = 0, 0, set()
            while startIndex<len(stones)-1:
                while endIndex+1<len(stones) and stones[endIndex+1]-stones[startIndex]<=maxJump:
                    endIndex += 1
                if startIndex==endIndex: 
                    return False, []
                startIndex = endIndex
                usedStones.add(stones[startIndex])
            return True, usedStones
        
        def isValidMaxJump(maxJump):
            jumpsPossible, usedStones = isValidMaxJumpHelper(maxJump, stones)
            if not jumpsPossible: return False
            return isValidMaxJumpHelper(maxJump, [0] + [stone for stone in stones if stone not in usedStones] + [stones[-1]])[0]
        
        low, high = 1, max(stones)
        while low<high:
            mid = (low+high)//2
            if isValidMaxJump(mid):
                high = mid
            else:
                low = mid+1
        return low