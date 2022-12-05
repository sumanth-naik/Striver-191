
def powMod(x, n, m):
    if n==0:
        return 1
    if n&1:
        return (powMod(x*x,n//2,m)*x)%m
    else:
        return (powMod(x*x, n//2,m))%m

x,n,m = 2,6,10
print(powMod(x,n,n))

def powModIterative(x, n, m):
    modVal = 1
    while n>0:
        if n&1:
            modVal = (modVal*x)%m
        x = (x*x)%m
        n = n//2
    return modVal
x,n,m = 3,2,4
print(powModIterative(x,n,n))

def powFuncIterative(x,n):
    powVal = 1
    while n>0:
        if n&1:
            powVal = powVal*x
        x = x * x
        n = n//2
    return powVal
x = 2
n = 10
print(powFuncIterative(x,n))