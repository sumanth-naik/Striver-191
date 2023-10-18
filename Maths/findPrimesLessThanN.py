
# Sieve of Eratosthenes
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def getPrimesLessThanN(n):
    flagArr, primes = [True]*n, []
    for i in range(2,n):
        if flagArr[i]:
            primes.append(i)
            for num in range(i*i, n, i):
                flagArr[num] = False
    return primes

print(getPrimesLessThanN(1000))      
    










