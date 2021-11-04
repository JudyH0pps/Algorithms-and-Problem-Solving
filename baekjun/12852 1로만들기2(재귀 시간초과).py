import sys
sys.setrecursionlimit(10 ** 7)
# input = lambda:sys.stdin.readline().rstrip()
input = lambda:open('input.txt', 'r').readline().rstrip()

def recur(x):
    # print('in', x)
    if dp[x] != float('inf'):
        return dp[x]
    a = float('inf')
    if x % 2 == 0:
        a = recur(x//2) + 1
        pa = x//2
    b = float('inf')
    if x % 3 == 0:
        b = recur(x//3) + 1
        pb = x//3
    c = recur(x-1) + 1
    pc = x-1
    dp[x] = min(a, b, c)
    if dp[x] == a:
        parent[x] = pa
    elif dp[x] == b:
        parent[x] = pb
    else:
        parent[x] = pc
    return dp[x]

def p(x):
    print(x, end=' ')
    if x == 1:
        return
    p(parent[x])

N = int(input())

dp = [float('inf')] * (N + 1)
parent = [-1] * (N + 1)
dp[1] = 0
parent[1] = 1
dp[2] = 1
parent[2] = 1

i = 2
cnt = 0
while i < N + 1:
    cnt += 1
    dp[i] = cnt
    parent[i] = i // 2
    i *= 2

i = 3
cnt = 0
while i < N + 1:
    cnt += 1
    dp[i] = cnt
    parent[i] = i // 3
    i *= 3

# for i in range(N+1):
#     print('%2d'%i, end=',')
# print()
# for i in range(N+1):
#     print('%2d'%dp[i], end=',')

# print(dp)
print(recur(N))
p(N)