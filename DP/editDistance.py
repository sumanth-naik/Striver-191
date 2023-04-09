class Solution:
    def minDistance(self, word1Original, word2Original):
        memo = {}
        # word1 has to be larger
        def recursiveDP(index1, index2, word1, word2, swapped):
            if (index1, index2, swapped) in memo:
                return memo[(index1, index2, swapped)]
            elif (index2, index1, not swapped) in memo:
                return memo[(index2, index1, not swapped)]
            
            if index2==len(word2):
                return len(word1) - index1
            
            if len(word1)-index1<len(word2)-index2: 
                memo[(index1, index2, swapped)] = recursiveDP(index2, index1, word2, word1, not swapped)
        
            elif word1[index1]==word2[index2]:
                memo[(index1, index2, swapped)] = recursiveDP(index1+1, index2+1, word1, word2, swapped)
            else:
                memo[(index1, index2, swapped)] = 1 + min(recursiveDP(index1+1, index2+1, word1, word2, swapped), recursiveDP(index1+1, index2, word1, word2, swapped), recursiveDP(index1, index2+1, word1, word2, swapped))
            
            return memo[(index1, index2, swapped)]
        
        return recursiveDP(0, 0, word1Original, word2Original, False)
    

"gyfknmhafznyazxokbwjfzphaoucgbzjizdxytgwrgmzxhnlqylgkwsoqatknorvueghuyccokxlytzklgzmxaoqnvngjmlypfpjwilovhciqouultzddxdzpkdpboqfiwalpddlbglidxghjlxydlrvblrrxzfguudaprkiiqxhfacphkqpzwmibuwvngmhcetcfodjszpeouaalovoqrtiodccbbmwsvyfflguzzgshwqhxafwcxttjrkupzntptlrkrpweacxzhhztzzhkrwrtjuscmtsvqnprxhwskeldltkajiwwqcunnwscrpdnqnylztsbamkaowwjpsgzhpwzwlmfqdrxmcapsttbvuzykhkukgfsiqmzgagzhiotpiheddqlofsyipplvwpglrgkmfafphamrosyfsaqmgeffevmcifqhepquzzusexvxhnnstpokfokarrcsdtsjvncijyyugspjysuaxcfbohqqsejpvz"
"vnosnidwxfkjkempzfgswlydmqulxpbjbbyxcsqzwkjjdepbttbtsgddihcmseiaxpxzuxryfkljnwpvbdcyxqbmlickscaqzifqfsqiqfbnldubannuipdtuizunogxhyaifytajecrahvgbaofqyrhhslhknplzchpyiuahwravozyusppnvbopgvcelgreyofcwlxenddmxotozmzlwwjvahaekrcebdgsudabbjdgndwlxzvyjfbcxmmdbzticunqblhkphycayotiivnnkbsffeasnegkoaiwdbgueozlfzfumtbzpaycasrjrsilyhbkpyudqayaqkmztqgzyacgaabwsqkpoprfojrfqjcupykgbsatsfqrdxeazlbacduyhuwakoxssqmfberwsedryqnyqceintrtajhadiegihaeldakiqnbtildhiycdwbbcsvnjkigelrrbcwwfnpqfiwlmbhosmqjduroljpawstydv"


class Solution:
    def minDistance(self, word1, word2):
        memo = {}
        def recursiveDP(index1, index2):
            if (index1, index2) in memo:
                return memo[(index1, index2)]
            
            if index2==len(word2):
                return len(word1) - index1
            if index1==len(word1):
                return len(word2) - index2
        
            if word1[index1]==word2[index2]:
                memo[(index1, index2)] = recursiveDP(index1+1, index2+1)
            else:
                memo[(index1, index2)] = 1 + min(recursiveDP(index1+1, index2+1), recursiveDP(index1+1, index2), recursiveDP(index1, index2+1))
            
            return memo[(index1, index2)]
        
        return recursiveDP(0, 0)
    
class Solution:
    def minDistance(self, word1, word2):
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for j in range(len(word2)+1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1)+1):
            dp[i][len(word2)] = len(word1) - i

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i]==word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j+1], dp[i+1][j], (dp[i][j+1]))
        return dp[0][0]
    
        
class Solution:
    def minDistance(self, word1, word2):
        dp0 = [0 for _ in range(len(word2)+1)]
        dp1 = [0 for _ in range(len(word2)+1)]

        for i in range(len(word1), -1, -1):
            for j in range(len(word2), -1, -1):
                if i==len(word1):
                    dp0[j] = len(word2) - j
                elif j==len(word2):
                    dp0[j] = len(word1) - i
                elif word1[i]==word2[j]:
                    dp0[j] = dp1[j+1]
                else:
                    dp0[j] = 1 + min(dp1[j+1], dp1[j], (dp0[j+1]))
            dp0, dp1 = dp1, dp0
        return dp1[0]