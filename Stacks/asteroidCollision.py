class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:
            stack.append(num)
            while len(stack)>=2 and stack[-1]<0 and stack[-2]>0:
                num1, num2 = -stack.pop(), stack.pop()
                if num1>num2: stack.append(-num1)
                elif num2>num1: stack.append(num2)
        return stack

