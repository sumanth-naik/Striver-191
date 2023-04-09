class Solution:
    def waysToBuildRooms(self, prevRoom):
        n = len(prevRoom)
        childList = [[] for _ in range(n)]
        for node, parent in enumerate(prevRoom):
            if node:
                childList[parent].append(node)

        n, MOD = len(prevRoom), 10**9 + 7
        factorialsArr = [1 for _ in range(n+1)]
        for i in range(2, n+1):
            factorialsArr[i] = (factorialsArr[i-1]*i)%(MOD)
        
        factorialsInverseArr = [1 for _ in range(n+1)]
        factorialsInverseArr[-1] = pow(factorialsArr[-1], MOD-2, MOD)
        for i in range(n-1, 1, -1):  
            factorialsInverseArr[i] = (factorialsInverseArr[i+1]*(i+1))%(MOD)


        # (n_1 + n_2 + n_3 + ......... + n_k)!
        # ------------------------------------
        #  n_1!  *  n_2! * .........  *  n_k!
        #  ---      ---                  ---
        # topo_1   topo_2               topo_k   

        def dfs(node):
            sumOfSizesOfSubTrees = 0
            denominator = 1
            numerator2 = 1
            for neigh in childList[node]:
                sizeOfSubTree, numTopoSortsOfSubTree = dfs(neigh)
                sumOfSizesOfSubTrees += sizeOfSubTree
                denominator = (denominator * factorialsInverseArr[sizeOfSubTree])%MOD
                numerator2 = (numerator2 * numTopoSortsOfSubTree)%MOD
            return sumOfSizesOfSubTrees+1, ((factorialsArr[sumOfSizesOfSubTrees] * numerator2) * denominator)%MOD
        
        return dfs(0)[1]


