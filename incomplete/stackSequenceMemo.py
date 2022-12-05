




#pushString = "737 337 124 315 172 315 535 315 535 34 124 737 671 280 34 124 315 663 663 663 535 737 663 280 737 337 34 737 337 535 124 34 337 671 737 172 663 34 124 737 124 337 315 663 172 124 337 535 172 280 172 315 34 535 124 280 280 172 124 663 280 34 280 671 34 535 737 172 315 124 663 671 34 535 663 34 535 671 337 34 337 34 315 34 671 337 172 315 280 663 535 535 535 337 280 124 671 280 34 535 663 671 280 337 124 280 671 663 315 535 337 337 737 535 663 280 337 172 671 663 337 535 671 34 124 737 124 172 663 315 737 124 737 172 671 315 737 671 280 663 124 535 315 172 34 34 172 124 124 337 172 671 172 315 315 337 663 280 737 663 337 671 671 737 34 737 737 737 663 337 671 315 280 315 172 124 280 34 172 172 535 280 671 671 737 315 535 315 172 280"
#popString = "737 124 34 535 34 280 671 315 535 315 172 315 124 337 663 337 737 280 663 737 535 663 663 315 124 535 124 34 663 172 737 671 337 34 124 337 737 34 737 280 124 535 34 315 172 280 172 535 337 124 172 663 315 671 280 34 280 663 124 172 280 663 535 34 671 663 124 315 172 737 535 34 337 124 737 315 172 337 671 34 34 337 34 337 671 535 34 671 663 535 34 280 671 124 315 280 663 535 737 337 337 535 663 671 280 124 337 280 280 337 535 535 535 663 280 315 671 535 337 663 671 172 337 124 737 124 34 737 315 671 172 737 124 737 315 663 172 34 34 172 315 535 124 663 280 671 172 172 337 315 315 172 671 124 124 337 671 671 337 663 737 280 315 280 315 671 337 663 737 737 737 34 737 535 172 172 34 280 124 671 280 280 172 315 535 315 737 671 172 663"

#pushString = "737 337 124 315 172 315 535 315 535 34 124 737 671 280 34 124 315 663 663 663 535 737 663 280 737 337 34 737 337 535 124 34 337 671 737 172 663 34 124 737 124 337 315 663 172"
#popString = "737 124 34 535 34 280 671 315 535 315 172 315 124 337 663 337 737 280 663 737 535 663 663 315 124 535 124 34 663 172 737 671 337 34 124 337 737 34 737 280 124 535 34 315 172 280"


pushString = "737 337 124 315 172 315 535 315 535 34 124 737 671 280 34 124 315 663 663 663 535 737 663 280 737 337 34 737 337 535 124 34 337 671 737 172 663 34 124 737 124 337 315 663 172 124 337 535 172 280 172 315 34 535 124 280 280 172 124 663 280 34 280 671 34 535 737 172 315 124 663 671 34 535 663 34 535 671 337 34 337 34 315 34 671 337 172 315 280 663 535 "
popString = "737 124 34 535 34 280 671 315 535 315 172 315 124 337 663 337 737 280 663 737 535 663 663 315 124 535 124 34 663 172 737 671 337 34 124 337 737 34 737 280 124 535 34 315 172 280 172 535 337 124 172 663 315 671 280 34 280 663 124 172 280 663 535 34 671 663 124 315 172 737 535 34 337 124 737 315 172 337 671 34 34 337 34 337 671 535 34 671 663 535 34 280 "

#pushString = "1 2 3 4 5"
#popString = "2 2 3 4 5"

pushSequenceArr = pushString.split(" ")
popSequenceArr = popString.split(" ")

print(len(pushSequenceArr), len(popSequenceArr))
def memoKeyGiver(stack, pushSequenceIndex, popSequenceIndex):
    key = ""
    for s in stack:
        key = key + str(s) + "-"
    return key + ":" +str(pushSequenceIndex) + "-" + str(popSequenceIndex)
count = 0

def stackSequenceSolver(pushSequenceArr, pushSequenceIndex, popSequenceArr, popSequenceIndex, n, stack, ansArr, memo, count):
   
    if(len(stack)==0 or pushSequenceIndex%10==0):
        print(len(stack),pushSequenceIndex)
        
    memoKey = memoKeyGiver(stack, pushSequenceIndex, popSequenceIndex)
    if(memoKey in memo):
        count += 1
        if(count%10==0):
            print(count)
        return memo[memoKey]
    
    
    
    if(len(stack)==0 and pushSequenceIndex==n and popSequenceIndex==n):
        return True
        
    if popSequenceIndex<n and len(stack)>0 and stack[len(stack)-1]==popSequenceArr[popSequenceIndex]:
        popVal = stack.pop()
        ansArr.append("o_"+str(popVal))
        if(stackSequenceSolver(pushSequenceArr, pushSequenceIndex, popSequenceArr, popSequenceIndex+1, n, stack, ansArr, memo, count)):
            return True
        stack.append(popVal)
        ansArr.pop()
        
    if pushSequenceIndex<n:
        ansArr.append("p_"+str(pushSequenceArr[pushSequenceIndex]))
        stack.append(pushSequenceArr[pushSequenceIndex])
        if(stackSequenceSolver(pushSequenceArr, pushSequenceIndex+1, popSequenceArr, popSequenceIndex, n, stack, ansArr, memo, count)):
            return True
        ansArr.pop()
        stack.pop()
       
    memo[memoKeyGiver(stack, pushSequenceIndex, popSequenceIndex)] = False
    return False


ansArr = []
memo = {}
if(stackSequenceSolver(pushSequenceArr, 0, popSequenceArr, 0, len(pushSequenceArr), [], ansArr , memo, count)):
    print(ansArr)
else: 
    print("not possible")
    
print(memo)
    
    
def ansChecker(arr):
    stack = []
    for op in arr:
        if op[0] == 'p':
            stack.append(op[2:])
        else:
            if(op[2:]==stack[len(stack)-1]):
                stack.pop()
            else:
                print("WRONG ANSWER")
                
    if(stack==[]):
        print("RIGHT ANSWER")
    else:
        print("WRONG ANSWER")
        
        
ansChecker(ansArr)
    
    
    
    
    