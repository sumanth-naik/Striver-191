from collections import deque


def removeDuplicatesIfNecessary(dq, k):
    print(dq)
    if len(dq)<k:
        return
    lastChar = dq[-1]
    for index in range(-1,-k-1,-1):
        if dq[index] is not lastChar:
            return
    index = -1
    while dq and dq[index]==lastChar:
        dq.pop()
        

s = "deeedbbcccbdaa"
k = 3
def removeDuplicates(s: str, k: int) -> str:
    
    dq = deque()
    
    for char in s:
        if not dq or dq[-1]==char:
            dq.append(char)
        else:
            removeDuplicatesIfNecessary(dq, k)
            dq.append(char)
    removeDuplicatesIfNecessary(dq, k)
    return ''.join(dq)

#print(removeDuplicates(s, k))




s="pbbcggttciiippooaais"
k = 2

s="hhhiiibbbyyyeeebyeee"
k=2

def removeDuplicatesGreaterOrEqualToK(s: str, k: int) -> str:
    dq = deque()
    for char in s:        
        if dq and dq[-1][0] !=char and dq[-1][1]>=k:
            dq.pop()

        if dq and dq[-1][0]==char:
            top = dq.pop()
            dq.append((top[0],top[1]+1))
        else:
            dq.append((char,1))

    if dq[-1][1] >= k:
        dq.pop()  

    return(''.join([q[0]*q[1] for q in dq]))

        

print(removeDuplicatesGreaterOrEqualToK(s,k))




def removeDuplicatesOnlyK(s: str, k: int) -> str:
    
    dq = deque()
    for char in s:
        if not dq or not dq[-1][0]==char:
            dq.append((char,1))
        else:
            top = dq.pop()
            dq.append((top[0],top[1]+1))
        if dq[-1][1]==k:
            dq.pop()
        
    return(''.join([q[0]*q[1] for q in dq]))

print(removeDuplicatesOnlyK(s,k))






















