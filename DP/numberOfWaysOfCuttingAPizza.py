class Solution:
    def ways(self, pizza, k: int) -> int:
        m, n, MOD = len(pizza), len(pizza[0]), 10**9+7

        @lru_cache(None)
        def getMinRowAndColWithApple(i, j):
            minRowWithApple, minColWithApple = 1000, 1000
            for iIndex in range(i, m):
                for jIndex in range(j, n):  
                    if pizza[iIndex][jIndex]=='A': 
                        minRowWithApple = min(minRowWithApple, iIndex)
                        minColWithApple = min(minColWithApple, jIndex)
            return minRowWithApple, minColWithApple

        @lru_cache(None)
        def memoization(i, j, k):
            if i==m or j==n: return 0
            if k==1:
                for iIndex in range(i, m):
                    for jIndex in range(j, n):
                        if pizza[iIndex][jIndex]=='A': return 1
                return 0
            
            cutsPossible = 0
            minRowWithApple, minColWithApple = getMinRowAndColWithApple(i, j)
            for iIndex in range(minRowWithApple+1, m):
                cutsPossible = (cutsPossible+memoization(iIndex, j, k-1))%MOD
            for jIndex in range(minColWithApple+1, n):
                cutsPossible = (cutsPossible+memoization(i, jIndex, k-1))%MOD
            return cutsPossible
            
        return memoization(0,0,k)
    

class Solution:
    def ways(self, pizza, k: int) -> int:
        m, n, MOD = len(pizza), len(pizza[0]), 10**9+7

        minRowAndColWithAppleDpArr = [[[100,100] for _ in range(n)] for _ in range(m)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if pizza[i][j]=="A": minRowAndColWithAppleDpArr[i][j] = [i,j]
                if j+1<n: 
                    minRowAndColWithAppleDpArr[i][j][0] = min(minRowAndColWithAppleDpArr[i][j][0], minRowAndColWithAppleDpArr[i][j+1][0])
                    minRowAndColWithAppleDpArr[i][j][1] = min(minRowAndColWithAppleDpArr[i][j][1], minRowAndColWithAppleDpArr[i][j+1][1])
                if i+1<m: 
                    minRowAndColWithAppleDpArr[i][j][0] = min(minRowAndColWithAppleDpArr[i][j][0], minRowAndColWithAppleDpArr[i+1][j][0])
                    minRowAndColWithAppleDpArr[i][j][1] = min(minRowAndColWithAppleDpArr[i][j][1], minRowAndColWithAppleDpArr[i+1][j][1])

        pizzaCutsDp = [[[0 for _ in range(k+1)] for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if minRowAndColWithAppleDpArr[i][j][0]!=100: pizzaCutsDp[i][j][1] = 1
        
        for cutNum in range(2, k+1):
            for i in range(m):
                for j in range(n):
                    for iIndex in range(minRowAndColWithAppleDpArr[i][j][0]+1, m):
                        pizzaCutsDp[i][j][cutNum] = (pizzaCutsDp[i][j][cutNum]+pizzaCutsDp[iIndex][j][cutNum-1])%MOD
                    for jIndex in range(minRowAndColWithAppleDpArr[i][j][1]+1, n):
                        pizzaCutsDp[i][j][cutNum] = (pizzaCutsDp[i][j][cutNum]+pizzaCutsDp[i][jIndex][cutNum-1])%MOD
        return pizzaCutsDp[0][0][k]
    


class Solution:
    def ways(self, pizza, k: int) -> int:
        m, n, MOD = len(pizza), len(pizza[0]), 10**9+7

        minRowAndColWithAppleDpArr = [[[100,100] for _ in range(n)] for _ in range(m)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if pizza[i][j]=="A": minRowAndColWithAppleDpArr[i][j] = [i,j]
                if j+1<n: 
                    minRowAndColWithAppleDpArr[i][j][0] = min(minRowAndColWithAppleDpArr[i][j][0], minRowAndColWithAppleDpArr[i][j+1][0])
                    minRowAndColWithAppleDpArr[i][j][1] = min(minRowAndColWithAppleDpArr[i][j][1], minRowAndColWithAppleDpArr[i][j+1][1])
                if i+1<m: 
                    minRowAndColWithAppleDpArr[i][j][0] = min(minRowAndColWithAppleDpArr[i][j][0], minRowAndColWithAppleDpArr[i+1][j][0])
                    minRowAndColWithAppleDpArr[i][j][1] = min(minRowAndColWithAppleDpArr[i][j][1], minRowAndColWithAppleDpArr[i+1][j][1])

        pizzaCutsDpPrevK = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if minRowAndColWithAppleDpArr[i][j][0]!=100: pizzaCutsDpPrevK[i][j] = 1
        
        for _ in range(k-1):
            pizzaCutsDp = [[0 for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    for iIndex in range(minRowAndColWithAppleDpArr[i][j][0]+1, m):
                        pizzaCutsDp[i][j] = (pizzaCutsDp[i][j]+pizzaCutsDpPrevK[iIndex][j])%MOD
                    for jIndex in range(minRowAndColWithAppleDpArr[i][j][1]+1, n):
                        pizzaCutsDp[i][j] = (pizzaCutsDp[i][j]+pizzaCutsDpPrevK[i][jIndex])%MOD
            pizzaCutsDpPrevK = pizzaCutsDp
        return pizzaCutsDpPrevK[0][0]