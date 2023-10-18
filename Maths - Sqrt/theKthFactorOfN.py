class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors1, factors2 = [], []
        for i in range(1, int(sqrt(n))+1):
            if not n%i: 
                factors1.append(i)
                factors2.append(n//i)
        if factors1[-1]==factors2[-1]: factors1.pop()
        factors = factors1 + factors2[::-1]
        return factors[k-1] if k<=len(factors) else -1

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        root = int(sqrt(n))
        for num in range(1, root+1):
            if not n%num:
                k-=1
                if not k: return num
        
        for num in range(root if root*root!=n else root-1, 0, -1):
            if not n%num:
                k-=1
                if not k: return n//num

        return -1