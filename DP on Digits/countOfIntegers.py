# Range, validity based on digits -> Digit DP
# Key Idea 1: Iterate over digits till len(num)
# Key Idea 2: Have isDigitRestricted to tell if we can go to num[index] digit only or till 9 

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        
        def dpHelper(num):
            @cache
            def dp(index, isDigitRestricted, sumSoFar):
                if index==len(num): 
                    return int(min_sum<=sumSoFar<=max_sum)
                limit = int(num[index]) if isDigitRestricted else 9
                return sum(dp(index+1, isDigitRestricted and digit==limit, sumSoFar+digit) for digit in range(limit+1))
            return dp(0, True, 0)

        return (dpHelper(num2) - dpHelper(str(int(num1)-1))) % (10**9 + 7)