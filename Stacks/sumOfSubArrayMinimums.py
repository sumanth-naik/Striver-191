arr = [3,2,2,3,5,4]

def sumOfSubArrayMinimums(arr):
    stack = []
    stackSum = 0
    totalSum = 0
    for num in arr:
        numPops = 0
        while stack and stack[-1][0]>num:
            stackTop = stack.pop()
            stackSum -= stackTop[0]*stackTop[1]
            numPops += stackTop[1]
        if stack and stack[-1][0]==num:
            stack[-1] = (stack[-1][0], stack[-1][1]+numPops+1)
        else:
            stack.append((num, numPops+1))
        stackSum += stack[-1][0]*(numPops+1)

        totalSum += (stackSum%(10**9+7))
    return totalSum%(10**9+7)

print(sumOfSubArrayMinimums(arr))
