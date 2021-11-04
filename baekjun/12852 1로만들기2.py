import sys
input = lambda:sys.stdin.readline().rstrip()
# input = lambda:open('input.txt', 'r').readline().rstrip()

def p(x):
    print(x, end=' ')
    if x == 1:
        return
    p(parent[x])

N = int(input())

dp = [float('inf')] * (max(3, N) + 1)
parent = [0] * (max(3, N) + 1)

dp[1] = 0
parent[1] = 1
dp[2] = 1
parent[2] = 1

def ans(N):
    for i in range(1, N + 1):
        if dp[i-1] + 1 <= dp[i]:
            dp[i] = dp[i-1] + 1
            parent[i] = i-1
        # if i == N:
        #     return
        j = i * 2
        while j < N + 1:
            if dp[j] >= dp[j//2] + 1:
                dp[j] = dp[j//2] + 1
                parent[j] = j//2
            # if j == N:
            #     return
            j *= 2
        j = i * 3
        while j < N + 1:
            if dp[j] >= dp[j//3] + 1:
                dp[j] = dp[j//3] + 1
                parent[j] = j//3
            # if j == N:
            #     return
            j *= 3

ans(N)

print(dp[N])
p(N)
