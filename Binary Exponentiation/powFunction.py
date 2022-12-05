
def power(x,n):
    if(n==1):
        return x
    if n==0:
        return 1
    if(n%2==0):
        return power(x*x,n/2)
    else:
        return x* power(x, n-1)

def pow(x,n):
    if(n<0):
        return 1/power(x,abs(n))
    else:
         return power(x,n)