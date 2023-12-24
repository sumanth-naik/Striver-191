# Key Idea: After MSB, every bit indicates the path to node. Point where path mismatches is LCA.
# a = 10 => b1010 => Path = Left, (Right, Left)   -> 2 different steps/edges
# b = 4 =>  b0100 => Path = Left, (Left)          -> 1 different step/edges   => ans = 2 + 1 + 1(new edge)
class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        def getCycleLength(pair):
            a, b = bin(pair[0])[3:], bin(pair[1])[3:]
            left = right = 0
            while left<len(a) and right<len(b) and a[left]==b[left]:
                left += 1
                right += 1
            return (len(a)-left) + (len(b)-right) + 1

        return list(map(getCycleLength, queries))


# Key Idea: Same as above but with bit manipulation
class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        for a, b in queries:
            a, b = max(a, b), min(a, b)
            lenA, lenB = a.bit_length(), b.bit_length()
            a >>= (lenA - lenB)
            yield 2*((a^b).bit_length()) + (lenA - lenB) + 1



# Key Idea: Imagine bubbling up larger number of a,b. They both will intersect at LCA.
# Note that its same as first idea, but bottom up
class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        for a, b in queries:
            count = 0
            while a!=b:
                a, b = min(a,b), max(a,b)>>1
                count += 1
            yield count + 1

