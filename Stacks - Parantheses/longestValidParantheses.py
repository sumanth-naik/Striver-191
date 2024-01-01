# Key Idea 1: Max Length ending at index will depend on max length ending before the current match
#            (())() => dp[5] depends on dp[3]
# Key Idea 2: Use stacks to keep track of unused '(' to match with ')' [in our example index 4]
# Key Idea 3: Stack top's index will be just right of prev ')' [in our example index 3]

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp, stack = [0] * (len(s)+1), []
        for index, char in enumerate(s):
            if char=='(':
                stack.append(index)
            else:
                if stack:
                    prevIndex = stack.pop()
                    dp[index+1] = dp[prevIndex] + (index - prevIndex + 1)
        return max(dp)