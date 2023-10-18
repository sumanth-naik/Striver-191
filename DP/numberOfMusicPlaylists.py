class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:

        MOD = 10**9+7
        @lru_cache(None)
        def recursion(n, unusableNumsCount, songsLeftToAdd):
            if songsLeftToAdd==0: return 1
            return ((n-unusableNumsCount)*recursion(n, min(k, unusableNumsCount+1), songsLeftToAdd-1))%MOD
        
        combinations = [1]
        for r in range(1, n+1):
            combinations.append((combinations[-1]*(n-r+1))//r)
        
        return sum(combinations[r]*((-1)**r)*recursion(n-r, 0, goal) for r in range(n+1))%MOD

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:

        MOD = 10**9+7
        @lru_cache(None)
        def recursion(n, songsLeftToAdd):
            if songsLeftToAdd==0: return 1
            return (n-min(k, goal-songsLeftToAdd))*recursion(n, songsLeftToAdd-1)%MOD
        
        combinations = [1]
        for r in range(1, n+1):
            combinations.append((combinations[-1]*(n-r+1))//r)
        
        return sum(combinations[r]*((-1)**r)*recursion(n-r, goal) for r in range(n+1))%MOD

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:

        MOD = 10**9+7
        @lru_cache(None)
        def recursion(numSongsInPlaylist, numUniqueSongsInPlaylist):
            if numUniqueSongsInPlaylist==0: return 1 if numSongsInPlaylist==0 else 0
            if numSongsInPlaylist<numUniqueSongsInPlaylist: return 0
            return ((n-numUniqueSongsInPlaylist+1)*recursion(numSongsInPlaylist-1, numUniqueSongsInPlaylist-1) + \
                max((numUniqueSongsInPlaylist-k)*recursion(numSongsInPlaylist-1, numUniqueSongsInPlaylist), 0))%MOD
        
        return recursion(goal, n)%MOD
    

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:

        MOD, dp = 10**9+7, [[0 for _ in range(n+1)] for _ in range(goal+1)]
        dp[0][0] = 1
        for numSongsInPlaylist in range(1, goal+1):
            for numUniqueSongsInPlaylist in range(1, min(n, numSongsInPlaylist)+1):
                dp[numSongsInPlaylist][numUniqueSongsInPlaylist] = ((n-numUniqueSongsInPlaylist+1)*dp[numSongsInPlaylist-1][numUniqueSongsInPlaylist-1] + \
                max((numUniqueSongsInPlaylist-k)*dp[numSongsInPlaylist-1][numUniqueSongsInPlaylist], 0))%MOD

        return dp[goal][n]%MOD
    

    

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:

        MOD = 10**9+7
        dpPrev = [0 for _ in range(n+1)]
        dpPrev[0] = 1
        for numSongsInPlaylist in range(1, goal+1):
            dpCurr = [0 for _ in range(n+1)]
            for numUniqueSongsInPlaylist in range(1, min(n, numSongsInPlaylist)+1):
                dpCurr[numUniqueSongsInPlaylist] = ((n-numUniqueSongsInPlaylist+1)*dpPrev[numUniqueSongsInPlaylist-1] + \
                max((numUniqueSongsInPlaylist-k)*dpPrev[numUniqueSongsInPlaylist], 0))%MOD
            dpPrev = dpCurr

        return dpPrev[n]%MOD
    
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9+7
        nFactorialMod = 1
        for i in range(2, n+1):
            nFactorialMod = (nFactorialMod*i)%MOD
        
        inverseFactorialMod = [1 for _ in range(n+1)]
        inverseFactorialMod[-1] = pow(nFactorialMod, MOD-2, MOD)
        for i in range(n-1, -1, -1):
            inverseFactorialMod[i] = (inverseFactorialMod[i+1]*(i+1))%MOD

        totalPlaylists = 0
        for i in range(k, n+1):
            temp = pow(i-k, goal-k, MOD)
            temp *= inverseFactorialMod[n-i]
            temp *= inverseFactorialMod[i-k]
            totalPlaylists += (-temp if (n-i)&1 else temp)
            totalPlaylists %= MOD
        
        return (totalPlaylists*nFactorialMod)%MOD
