
# Sieve of Eratosthenes
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def getPrimesLessThanN(n):
    flagArr = [1 for i in range(n)]
    primes = []
    for i in range(2,n):
        if(flagArr[i]==1):
            primes.append(i)
            for num in range(i*i, n, i):
                flagArr[num] = 0
    return primes

print(getPrimesLessThanN(1000))      
    










