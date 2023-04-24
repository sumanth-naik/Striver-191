#codestudio
def allocateBooks(arr, n, m):

    def canIAllocate(maxNumPages):
        runningSum, index, numStudents = 0, 0, 1
        while index<n:
            if runningSum+arr[index]>maxNumPages:
                runningSum = 0
                numStudents += 1
            runningSum += arr[index]
            index += 1
        return numStudents<=m
    
    low, high = max(arr), sum(arr)
    while low<high:
        mid = (low+high)//2
        if canIAllocate(mid): high = mid
        else: low = mid+1
    return low