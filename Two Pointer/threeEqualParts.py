class Solution:
    def threeEqualParts(self, arr):
        n = len(arr)
        leftPointer, leftValue = 0, arr[0]
        rightPointer, rightValue = n-1, arr[n-1]
        midValue = int(''.join(str(arr[i]) for i in range(1, n-1)), 2)
        while midValue>=rightValue and leftPointer<rightPointer:
            if leftValue==midValue==rightValue:
                return [leftPointer, rightPointer]
            if leftValue > rightValue:
                rightValue += pow(2, n-rightPointer)*arr[rightPointer-1]
                midValue //= 2
                rightPointer -= 1
            else:
                leftValue = 2*leftValue + arr[leftPointer+1]
                midValue %= pow(2, rightPointer - leftPointer - 2)
                leftPointer += 1
        return [-1,-1] 

    def threeEqualParts(self, arr):
        numOnes, n = sum(arr), len(arr)
        if numOnes==0: return [0,n-1]
        if not numOnes%3==0: return [-1,-1]
        pointers = [-1,-1,-1]
        onesSeen = 0
        for index, num in enumerate(arr):
            if num==1:
                onesSeen += 1
                for i in range(3):
                    if (numOnes/3)*i+1 == onesSeen:
                        pointers[i] = index
        while pointers[2] < n and arr[pointers[0]] == arr[pointers[1]] == arr[pointers[2]]:
            for i in [0,1,2]:
                pointers[i] += 1
        if pointers[2] == n:
            return [pointers[0]-1, pointers[2]-1]

        return [-1, -1]