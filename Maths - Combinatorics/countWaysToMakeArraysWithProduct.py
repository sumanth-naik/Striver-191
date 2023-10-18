class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        MOD = 10**9+7
        @lru_cache(None)
        def recursion(size, num):
            if size==1: return 1
            sqRoot = floor(sqrt(num))
            summation = sum(recursion(size-1, factor)+recursion(size-1, num//factor) for factor in range(1, sqRoot+1) if num%factor==0)%MOD                        
            if sqRoot*sqRoot==num:
                return (summation - recursion(size-1, sqRoot))%MOD
            else:
                return summation

        return [recursion(size, num) for size, num in queries]
        
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
MOD = 10**9+7
#https://leetcode.com/problems/count-ways-to-make-array-with-product/solutions/1035607/c-python-precompute/
'''
2,2,2,2
<_>, <_>, <_>, <_>
count = 4, buckets = 4
<2>, <2,2>, <_>, <2> -> [2,4,1,2]
num ways to arrange this is _ _ _ _ _ _ _ (7=count+buckets-1) places to put (4 = count) 
   2 _ 2 2 _ _ 2 (fill 2s first and then empty ones indicate partitions)
=> 2 | 2 2 | | 2 
=> <2>, <2,2>, <_>, <2>
combining diff factors
2|
|2
and
3|
|3
gives 
23|
2|3 
3|2
 |23
hence multiply in ways *= comb(buckets-1+count, count)
'''
class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        def solver(buckets, num):
            ways = 1
            for prime in primes:
                count = 0
                while num%prime==0:
                    count += 1
                    num //= prime
                ways *= comb(buckets-1+count, count)
            if num!=1: #num has a factor which is a big prime
                ways *= buckets # there are 4 number of ways to put [num,1,1,1], [1,num,1,1], [1,1,num,1], [1,1,1,num]
            return ways%MOD
        return [solver(buckets, num) for buckets, num in queries]