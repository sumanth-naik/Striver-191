def dailyTemperatures(temperature):
        
    stack = [(0,0)]
    n = len(temperatures)
    nextHigherTempArr = [0 for _ in range(n)]

    for i in range(n-1, -1, -1):
        
        while len(stack)>1 and temperatures[i] >= stack[len(stack)-1][0]:
            stack.pop()
        
        nextHigherTempArr[i] = max(0, stack[len(stack)-1][1] - i)
        
        stack.append((temperatures[i], i))
        
    return nextHigherTempArr
    
    
    
    
    
    
    
    
    
    
    
temperatures = [230,160,90]
print(dailyTemperatures(temperatures))