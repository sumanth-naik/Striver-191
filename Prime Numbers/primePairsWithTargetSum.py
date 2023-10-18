from math import sqrt
class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:

        def primesTillN(n):
            primes = set(range(2, n+1))
            for num in range(2, int(sqrt(n))+1):
                if num not in primes: continue
                multiple = 2
                while num*multiple<=n:
                    primes.discard(num*multiple)
                    multiple += 1
            return primes

        primes = primesTillN(n)
        for num in range(2, n//2+1):
            if num in primes and n-num in primes: yield (num, n-num)


from math import sqrt
class Solution:

    def __init__(self) -> None:
        self.maxN = 10**6
        self.primes = set(range(2, self.maxN+1))
        self.sieveOfEratosthenes()
        self.sortedPrimes = sorted(list(self.primes))


    def sieveOfEratosthenes(self):
        for num in range(2, int(sqrt(self.maxN))+1):
            if num not in self.primes: continue
            multiple = 2
            while num*multiple<=self.maxN:
                self.primes.discard(num*multiple)
                multiple += 1


    def findPrimePairs(self, n: int) -> List[List[int]]:
        for num in self.sortedPrimes:
            if num>n-num: break
            if num in self.primes and n-num in self.primes: yield (num, n-num)


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        
        primes = [1 for _ in range(n+1)]
        primes[0] = primes[1] = 0
        for num in range(2, int(sqrt(n))+1):
            if primes[num]:
                for multiple in range(num**2, n+1, num): 
                    primes[multiple] = 0
        
        for num in range(2, n//2+1):
            if primes[num] and primes[n-num]: yield (num, n-num)