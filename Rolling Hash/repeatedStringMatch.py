
def powModFunc(d,m,q):
    if m==0:
        return 1
    if m&1:
        return (powModFunc(d*d, m//2, q) * d)%q
    else:
        return (powModFunc(d*d, m//2, q))%q


def rabinKarp(haystack, needle):
    n, m  = len(haystack), len(needle)
    hash_haystack_i = 0
    hash_needle = 0
    d, q = 26, 101
    powMod = powModFunc(d,m,q)

    for i in range(m):
        hash_haystack_i = (d*hash_haystack_i + ord(haystack[i]))%q
        hash_needle = (d*hash_needle + ord(needle[i]))%q
    

    for i in range(0, n-m+1):
        if hash_haystack_i==hash_needle:
            if haystack[i:i+m]==needle:
                return True
        if i+m<n:
            hash_haystack_i = (d*hash_haystack_i - ord(haystack[i])*powMod + ord(haystack[i+m]))%q
import math

def repeatedStringMatch(a, b):
    lenA = len(a)
    lenB = len(b)
    minMult = math.ceil(lenB/lenA)
    if rabinKarp(a*minMult, b):
        return minMult
    if rabinKarp(a*(minMult+1), b):
        return minMult+1
    return -1

a = "abcd"
b = "cdabcdab"
print(repeatedStringMatch(a,b))