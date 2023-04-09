class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n==1:
             return ''.join([str(i) for i in range(k)])
        if k==1:
            return ''.join(["0" for i in range(n)])
        arrayOfArrays = [[str(i) for i in range(k)] for _ in range(k**(n-1))]
        smallestStr = ["0" for _ in range(n-1)]
        lastNMinusOneDigits = ''.join(smallestStr)
        i = 0
        while arrayOfArrays[i]:
            toAdd = arrayOfArrays[i].pop()
            smallestStr.append(toAdd)
            lastNMinusOneDigits = lastNMinusOneDigits[1:]+toAdd
            i = int(lastNMinusOneDigits, k)
        return ''.join(smallestStr)