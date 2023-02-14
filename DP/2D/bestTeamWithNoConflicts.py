class Solution:
    def bestTeamScore(self, scores, ages):
        scoresAndAges = [(scores[i], ages[i]) for i in range(len(scores))]
        scoresAndAges.sort(key=lambda x:(x[1],x[0]))
        maxScoreOfYoungerPerson, prevYoungerPersonAge, maxScoreSoFar = -1, -1, -1
        # print(scoresAndAges)
        memo = {}
        def maxScoreRecursiveDP(i, maxScoreOfYoungerPerson, maxScoreSoFar, prevYoungerPersonAge):
            # print(i, maxScoreOfYoungerPerson, maxScoreSoFar, prevYoungerPersonAge)
            if i==len(scores): return 0
            if (i, maxScoreOfYoungerPerson) in memo: return memo[(i, maxScoreOfYoungerPerson)]
            score, age = scoresAndAges[i][0], scoresAndAges[i][1]
            if prevYoungerPersonAge!=age:
                prevYoungerPersonAge = age
                maxScoreOfYoungerPerson = maxScoreSoFar
            maxScoreOfPlayersFromIndexI = 0
            if maxScoreOfYoungerPerson<=score:
                maxScoreOfPlayersFromIndexI = maxScoreRecursiveDP(i+1, maxScoreOfYoungerPerson, max(maxScoreOfYoungerPerson, score, maxScoreSoFar), prevYoungerPersonAge) + score
            maxScoreOfPlayersFromIndexI = max(maxScoreOfPlayersFromIndexI, maxScoreRecursiveDP(i+1, maxScoreOfYoungerPerson, maxScoreSoFar, prevYoungerPersonAge))
            
            memo[(i, maxScoreOfYoungerPerson)] = maxScoreOfPlayersFromIndexI
            return memo[(i, maxScoreOfYoungerPerson)]
        return maxScoreRecursiveDP(0, maxScoreOfYoungerPerson, prevYoungerPersonAge, maxScoreSoFar)

class Solution:
    def bestTeamScore(self, scores, ages):
        dp = [0 for i in range(max(ages)+1)]
        scoresAndAges = sorted(zip(scores, ages))
        for score,age in scoresAndAges:
            dp[age] = score + max(dp[:age+1])
        return max(dp)

