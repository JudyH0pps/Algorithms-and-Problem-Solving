from collections import deque

q = deque()
endlevel = 10
def firstchk(chk):
    for i,e in enumerate(chk):
        if not e:
            return i
    return -1

chk = [0 for _ in range(endlevel)]
q.append(([],chk,0))

while q:
    #print(st)
    nums, chk, level = q.popleft()
    if level == endlevel:
        #print(nums)
        continue
    for i,e in enumerate(chk):
        if e:
            continue
        #rint(i,e)
        nnums = nums[:]
        nchk = chk[:]
        nchk[i] = 1
        nnums.append(i)
        q.append((nnums,nchk,level+1))

    
    
    
        
            
            
    
        
    
    
