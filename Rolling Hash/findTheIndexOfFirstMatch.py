
a = "abcd"
b = "cdababcd"



def rabinKarp(haystack,needle):
    n, m = len(haystack), len(needle)
    hash_needle = 0
    hash_haystack_i = 0
    d, q = 26, 101
    for i in range(m):
        hash_needle = (d*hash_needle + ord(needle[i]))%q
        hash_haystack_i = (d*hash_haystack_i + ord(haystack[i]))%q

    powMod = pow(d,m)%q
    
    for i in range(0, n-m+1):
        if hash_haystack_i==hash_needle:
            if haystack[i:i+m]==needle:
                return i
        #update
        if i+m<n:
            hash_haystack_i = (d*hash_haystack_i -ord(haystack[i])*(powMod) +ord(haystack[i+m]))%q
    return -1


print(rabinKarp(b,a))

