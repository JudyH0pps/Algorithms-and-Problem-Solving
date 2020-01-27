# 백준 1010 다리 놓기

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt","r")
    input = f.readline
################################   



# f(N,M) = f(N-1,M-1) + f(N-1,M-2) + ... + f(N-1,0)
# N = M이라면 1
# N > M이라면 0

def dp(N,M):
    #print('call',N,M)
    global memoization

    if N == 1:
        return M
    elif N <= 0 or N > M:
        return 0
    elif memoization[N][M]:
        return memoization[N][M]

    summing = 0

    for i in range(M):
        summing += dp(N-1,i)

    
    memoization[N][M] = summing
    return summing

    
    
T = int(input())

for _ in range(T):

    N, M = map(int,input().split())
    memoization = [[0 for _ in range(M+1)] for _ in range(N+1)]
    
    #print(N,M)

    ans = dp(N,M)
    print(ans)
    #print()
   
