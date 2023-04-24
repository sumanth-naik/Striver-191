class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:

        @lru_cache(None)
        def getBinomialCoeffientsUsingPascalTriangle(degree):
            if degree==1: return [1, 1]
            prevCoeffs = getBinomialCoeffientsUsingPascalTriangle(degree-1)
            return [1] + [prevCoeffs[index]+prevCoeffs[index+1] for index in range(len(prevCoeffs)-1)] + [1]

        @lru_cache(None)
        def numBuckets(numPigs, numLives):
            if numLives==0 or numPigs==0: return 1
            binomialCoeffs = getBinomialCoeffientsUsingPascalTriangle(numPigs)
            return sum(numBuckets(numPigs-i, numLives-1)*binomialCoeffs[i] for i in range(len(binomialCoeffs)))
        
        numPigs, lives = 0, floor(minutesToTest/minutesToDie)
        while True:
            # numBuckets(numPigs, lives) turns out to be (lives+1)**numPigs
            if numBuckets(numPigs, lives)>=buckets: return numPigs
            numPigs += 1
            