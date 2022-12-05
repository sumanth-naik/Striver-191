nums = [1,2,3,4,3]


def nextGreaterElement(nums):
    stack = [-1]
    for i in range(len(nums)-1,-1,-1):
        while len(stack)>1 and stack[-1]<=nums[i]:
            stack.pop()
        stack.append(nums[i])
    output = [0 for i in range(len(nums))]
    for i in range(len(nums)-1,-1,-1):
        while len(stack)>1 and stack[-1]<=nums[i]:
            stack.pop()
        output[i] = stack[-1]
        stack.append(nums[i])
    return output
print(nextGreaterElement(nums))