# 백준 2839 설탕 배달

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 1

if not INPUTMODE:
    f = open("input.txt","r")
    input = f.readline
################################   

# 3kg 봉지와 5kg 봉지 2종류가 있다.
# 최소의 봉지 수로 Nkg을 담아야 할 때 그 봉지 수를 출력
# 담을 수 없다면 -1

N = int(input())

def dp(N,memo):
    if N <= 5:
        return memo[N]
    for i in range(6,N+1):
        memo[i] = min(memo[i-3]+1,memo[i-5]+1)
    return memo[N]

memo = [5001 for _ in range(max(6,N+1))]
memo[3] = 1
memo[5] = 1

ans = dp(N,memo)

if ans >= 5001:
    print(-1)
else:
    print(ans)
