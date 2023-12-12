# Key Idea: For each task, which session can I add it to?
# TC: O(n!) but with pruning -> Cant really give an estimate easily

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n, sessions, minSessions = len(tasks), [0], len(tasks)

        def dfs(index):
            if index==n: 
                nonlocal minSessions
                minSessions = min(minSessions, len(sessions))
                return

            if len(sessions) >= minSessions:
                return

            for sessionIndex in range(len(sessions)):
                if tasks[index]+sessions[sessionIndex] <= sessionTime:
                    sessions[sessionIndex] += tasks[index]
                    dfs(index+1)
                    sessions[sessionIndex] -= tasks[index]
                
            sessions.append(tasks[index])
            dfs(index+1)
            sessions.pop()
        
        dfs(0)
        tasks.sort(reverse=True)
        return minSessions
            
            
            
# Key Idea: In this session, what all tasks can I add?
# TC : O(2**n * sessionTime * n)

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        finalMask = (1<<n)-1

        @lru_cache(None)
        def bitmaskingDp(usedMask, timeLeftInCurrentSession):
            if usedMask==finalMask: return 0
            
            minSessionsNeeded = n
            for index in range(n):
                if not (usedMask & (1<<index)):
                    if tasks[index]<=timeLeftInCurrentSession:
                        minSessionsNeeded = min(minSessionsNeeded, bitmaskingDp(usedMask | (1<<index), timeLeftInCurrentSession-tasks[index]))
                    else:
                        minSessionsNeeded = min(minSessionsNeeded, 1 + bitmaskingDp(usedMask | (1<<index), sessionTime-tasks[index]))

            return minSessionsNeeded

        return 1 + bitmaskingDp(0, sessionTime)



            
# Key Idea: If the mask has what all tasks needs to be done, whats the best way to achieve it            
# TC: O(2**n * n)

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)

        @cache
        def dp(mask): # returns (minSessionsNeeded, timeLeftInLastSession)
            if not mask: return (0, 0)
            
            bestSessions, bestTime = n, 0
            for index in range(n):
                if mask & (1<<index):
                    minSessions, timeLeft = dp(mask & ~(1<<index))
                    if timeLeft<tasks[index]:
                        minSessions += 1
                        timeLeft = sessionTime
                    timeLeft -= tasks[index]
                    bestSessions, bestTime = min((bestSessions, bestTime), (minSessions, timeLeft), key = lambda x: (x[0], -x[1]))
            return bestSessions, bestTime

        return dp((1<<n)-1)[0]





