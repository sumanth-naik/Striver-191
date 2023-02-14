

def evaluateReversePolisNoataion(arr):
    stack = []
    for i in range(0, len(arr)):
        if arr[i].lstrip("-").isnumeric():
            stack.append(int(arr[i]))
        else:
            stack.append(arr[i])
        while len(stack)>=3 and (not type(stack[-1]) is int) and type(stack[-2]) is int:
            operator = stack.pop()
            right = stack.pop()
            left = stack.pop()
            if operator=="+":
                stack.append(left+right)
            elif operator=="-":
                stack.append(left-right)
            elif operator=="*":
                stack.append(left*right)
            elif operator=="/":
                stack.append(int(left/right))

    return stack[-1]


def evaluateReversePolisNoataionShort(arr):
    stack = []
    for i in range(0, len(arr)):
        if arr[i].lstrip("-").isnumeric():
            stack.append(arr[i])         
        else:
            operator = arr[i]
            right = stack.pop()
            left = stack.pop()
            stack.append(str(int(eval(left+operator+right))))
            # if operator=="+":
            #     stack.append(left+right)
            # elif operator=="-":
            #     stack.append(left-right)
            # elif operator=="*":
            #     stack.append(left*right)
            # elif operator=="/":
            #     stack.append(int(left/right))

    return int(stack[-1])

arr = ['4', '13', '5', '/', '+']


print(evaluateReversePolisNoataion(arr))
# print('-11'.isnumaric())
# print(int(-1/2))