'''
https://leetcode.com/problems/fair-distribution-of-cookies/solutions/2141573/dp-submask-enumeration-most-optimal-solution-100-faster-c/
#https://cp-algorithms.com/algebra/all-submasks.html#enumerating-all-submasks-of-a-given-mask

s := m       = 1010100
s-1          = 1010011
s := m & s-1 = 1010000    <- effectively, removing right most 1 and keeping others
s-1          = 1001111
m & s-2      = 1000100    <- effectively, removing right most 1 and keeping others

TC of subsetEnumeration(m) for m in range(1<<n) ->  O(3^n) 
'''
def subsetEnumeration(m):
    s = m
    while s>0:
        # ... you can use s ...
        s = (s-1) & m







'''
bitmask = 1010
MSB =     1000
'''
def getMSB(bitmask):
    msb = 0
    while bitmask:
        msb += 1
        bitmask >>= 1
    return 1<<(msb-1)





'''
bitmask = 1010
MSB =     0010
'''
def getLSB(x):
    return x & (-x)






'''
Idea : similar to subsetEnumeration but AND with subArrayMask 
bitmask = 10110
{10110, 10101 & 10110 = 10100, 10011 & 10100 = 10000}
10110 -> 00110
{00110, 00100}
00110 -> 00010
{00010}
'''
def subArrayEnumeration(bitmask):
    while bitmask:
        subArrayMask = bitmask
        while subArrayMask:
            yield subArrayMask
            subArrayMask = (subArrayMask-1) & subArrayMask
        bitmask &= ~getMSB(bitmask)