pushed = [1,2,3,4,5]
popped = [4,5,3, 2,1]


def isValidStackOp(pushed, popped):
    stack = []
    poppingIndex = 0
    for i in range(0, len(pushed)):
        stack.append(pushed[i])
        while(len(stack) and stack[len(stack)-1] == popped[poppingIndex]):
            stack.pop()
            poppingIndex += 1
            
    if(poppingIndex==len(popped)):
        return True
    return False

print(isValidStackOp(pushed, popped))