class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        @lru_cache(None)
        def stoneGame(index, turn):
            if index==len(stoneValue): return 0
            if turn:
                return max([stoneGame(index+j, not turn)+sum(stoneValue[index:index+j]) for j in [1,2,3] if index+j<=len(stoneValue)])
            else:
                return min([stoneGame(index+j, not turn)-sum(stoneValue[index:index+j]) for j in [1,2,3] if index+j<=len(stoneValue)])
            
        return "Alice" if stoneGame(0, True)>0 else "Bob" if stoneGame(0, True)<0 else "Tie"

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        @lru_cache(None)
        def stoneGame(index):
            if index>=len(stoneValue): return 0
            return max([sum(stoneValue[index:index+j])-stoneGame(index+j) for j in [1,2,3]])
        
        return "Alice" if stoneGame(0)>0 else "Bob" if stoneGame(0)<0 else "Tie"
