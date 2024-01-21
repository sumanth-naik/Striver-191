# Key Idea 1: Similar to number of paths from (x1, y1) to (x2, y2) if we can only go right and down (m+n C n)
# Key Idea 2: We HAVE to go atleast abs(e-s) steps in the direction of endPos. 
# Key Idea 3: Of Remaining [k - abs(e-s)] steps, we have to equally distribute to towards and away.
#              => Total steps towards endPos = abs(e-s) + ([k - abs(e-s)]//2)
# Key Idea 3: Parity of (e-s) and k must be equal for any valid path.

class Solution:
    def numberOfWays(self, s: int, e: int, k: int) -> int:
        return comb(k, (k+abs(e-s))//2) % (10**9+7) if abs(s-e)&1 == k&1 else 0
    


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = (10**9)+7

        @cache
        def dp(currPos, kLeft):
            if kLeft==0: return currPos == endPos
            if abs(currPos - endPos)>kLeft: return 0
            return (dp(currPos-1, kLeft-1) + dp(currPos+1, kLeft-1)) % MOD
        
        return dp(startPos, k) if abs(startPos-endPos)&1 == k&1 else 0

