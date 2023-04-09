class Solution:
    def minimizeArrayValue(self, nums):
        # (ceil of avg, sum, count)
        stack = [(nums[-1], nums[-1], 1)]

        for index in range(len(nums)-2, -1, -1):
            if nums[index]<stack[-1][0]:
                _, sum, count = stack.pop()
                stack.append((ceil((sum + nums[index])/(count+1)), sum + nums[index], count+1))
                while len(stack)>1 and stack[-1][0]<stack[-2][0]:
                    _, sum1, count1 = stack.pop()
                    _, sum2, count2 = stack.pop()
                    stack.append((ceil((sum1 + sum2)/(count1 + count2)), sum1 + sum2, count1 + count2))
            else:
                stack.append((nums[index], nums[index], 1))
        return stack[-1][0]

class Solution:
    def minimizeArrayValue(self, nums):
        sum, maxAvgSeen = 0, 0
        for i, num in enumerate(nums):
            sum += num
            if ceil(sum/(i+1))>maxAvgSeen:
                maxAvgSeen = ceil(sum/(i+1))
        return maxAvgSeen