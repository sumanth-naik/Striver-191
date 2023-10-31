#codestudio
def aggressiveCows(stalls, k):
    stalls.sort()

    minDiff, n = 1e9, len(stalls)
    for i in range(n-1):
        minDiff = min(minDiff, stalls[i+1]-stalls[i])

    def canIAllocate(minDistance):
        lastCowPosition, numCowsAllocated = stalls[0], 1
        for index in range(1, n):
            if stalls[index]-lastCowPosition>=minDistance:
                lastCowPosition = stalls[index]
                numCowsAllocated += 1
        return numCowsAllocated>=k
    
    low, high = minDiff, stalls[-1]-stalls[0]
    while low<high:
        mid = (low+high+1)//2
        if canIAllocate(mid):
            low = mid
        else:
            high = mid - 1
    return low