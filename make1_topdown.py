list = [ 0 for _ in range(10**6) ]

N = 11

def solve(n,lis):
    #print('현재 n : ',n,lis[n])
    if n<=1:
        lis[n] = 0
        return lis[n]
    
    if lis[n]>=1:
        return lis[n]
    
    lis[n] = 99999999
    if n % 3 == 0:
        lis[n] = solve(n//3,lis)+1
    elif n % 2 == 0:
        lis[n] = solve(n//2,lis)+1
        
    lis[n] = min(solve(n-1,lis)+1,lis[n])
    
    print(lis[:n])
    return lis[n]


    
print(solve(N,list))
