# Key Idea 1: Start from (1, 1) and draw out all the points
# Key Idea 2: You can go to every point (1, y) and (x, 1). 
# Key Idea 3: Every point (a, b) where gcd(a, b)==1 can be reached. Thus, Every point (pow(2, m) * a, pow(2, n) * b) also.
# Key Idea 4: Any point (a, b) where a, b arent multiples of 2 and gcd(a, b)!=1, cant be reached. Thus, Every point (pow(2, m) * a, pow(2, n) * b) also.

# Key Idea 3, 4 - Formal Proof: 
# gcd(x, y) == gcd(x, y - x) == gcd(x - y, y) holds when x and y are positive integers. <- No change in GCD
# gcd(x, y) = 2 * gcd(2x, y) = 2 * gcd(x, 2y) <- Only doubles GCD
# => gcd(a, b) will always be a two power

class Solution:
    def isReachable(self, x: int, y: int) -> bool:
        return gcd(x, y).bit_count() == 1