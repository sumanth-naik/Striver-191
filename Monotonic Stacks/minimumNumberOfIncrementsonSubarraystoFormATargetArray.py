class Solution:
    def minNumberOperations(self, target):
        stack, numOperations = [0], 0
        for num in target:
            if num>stack[-1]:
                numOperations += (num-stack[-1])
            while num<stack[-1]:
                stack.pop()
            stack.append(num)

        return numOperations
