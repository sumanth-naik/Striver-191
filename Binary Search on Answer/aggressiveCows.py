#codestudio
def aggressiveCows(stalls, k):
    stalls.sort()

    minDiff, n = 1e9, len(stalls)
    for i in range(n-1):
        minDiff = min(minDiff, stalls[i+1]-stalls[i])

    def canIAllocate(minDistance):
        lastCowPosition, numCowsAllocated = None, 0
        for stallPosition in stalls:
            if lastCowPosition==None: 
                lastCowPosition = stallPosition
                numCowsAllocated += 1
            elif stallPosition-lastCowPosition>=minDistance:
                lastCowPosition = stallPosition
                numCowsAllocated += 1
        return numCowsAllocated>=k
    
    low, high = minDiff, max(stalls)-min(stalls)
    while low<high:
        mid = (low+high+1)//2
        if canIAllocate(mid):
            low = mid
        else:
            high = mid - 1
    return low